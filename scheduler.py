import json
import time
from datetime import datetime, timedelta
import re
import requests
from app.service import StoryService, CategoryService, InterestService, FetchService
import domparser
from textrank import extractKeyphrases
from collections import Counter
import math
from app.config import logging


def reset_story_group():
    __story_service.reset_group()


def fetch_time_line():
    time_frame = {"start_time": 0, "end_time": 0}
    c_time = datetime.now() + timedelta(hours=-5)
    start_time = (c_time.year, c_time.month, c_time.day, c_time.hour, 0, 1, 0, 0, 0)
    start_epoch = int(time.mktime(start_time))
    c_time = c_time + timedelta(hours=5)
    end_time = (c_time.year, c_time.month, c_time.day, c_time.hour, 59, 59, 0, 0, 0)
    end_epoch = int(time.mktime(end_time))
    time_frame['start_time'] = start_epoch
    time_frame['end_time'] = end_epoch
    return time_frame


def current_epoch_time(now):
    """
    Calculating epoch time in secs
    :param now: Article fetch time
    :return: Epoch time in secs
    """
    t = (now.year, now.month, now.day, now.hour, now.minute, now.second, 0, 0, 0)
    secs = int(time.mktime(t))
    return secs


def checking_interest(article_keywords):
    article_interests = []
    article_category_ids = []
    for interest in __interest_service.find_all_interests():
        rx = r'({0})'.format(interest['interest'].lower())
        pattern = re.compile(rx)
        match_group = pattern.findall(''.join(map(str, article_keywords)))
        if match_group:
            if interest not in article_interests:
                article_interests.append(str(interest['interest']))
                article_category_ids.append(str(interest['category_id']))
    return article_interests, article_category_ids


def watching_stories(domain_list):
    """
    watching stories of competitors
    :param domain_list: targeted competitors domain names
    :return:
    """
    fetch = fetch_time_line()
    db_category_list = __category_service.find_all_categories()
    db_interest_list = __interest_service.find_all_interests()
    for domain in domain_list:
        r = requests.get("https://api.newswhip.com/v1/publisher/" + domain + "/1?key="+newswhip_key)
        response = json.loads(r.text)
        logging.info("Domain: " + domain + " & No of Articles: " + str(len(response['articles'])))
        for item in response['articles']:
            try:
                article_info = domparser.element_picker(item['link'].encode('utf-8'))
                if article_info['title'] is not None or article_info['feature_image'] is not None or article_info['url'] is not None:
                    article = {'title': '', 'url': '', 'description': '', 'keywords': '', 'feature_image': '','New_score': '',
                            'max_new_score': '', 'fb_like': '', 'tweet_count': '', 'publisher': '', "uuid": '', 'published': '',
                               'category': [], 'interest': [], 'fetch': '', 'created_keys':[]}
                    if item['headline'] is None:
                        article['title'] = article_info['title']
                    else:
                        article['title'] = item['headline'].encode('utf-8')

                    if item['link'] is None:
                        article['url'] = article_info['url']
                    else:
                        article['url'] = item['link'].encode('utf-8')

                    if item['excerpt'] is None:
                        article['description'] = article_info['description']
                    else:
                        article['description'] = item['excerpt']

                    if item['keywords'] is None:
                        article['keywords'] = article_info['keywords']
                    else:
                        article['keywords'] = (item['keywords']).split(',')

                    if item['image_link'] is None:
                        article['feature_image'] = article_info['feature_image']
                    else:
                        article['feature_image'] = item['image_link']
                    if 'new_score' in item:
                        article['New_score'] = item['nw_score']
                    else:
                        article['New_score'] = 0
                    if 'max_new_score' in item:
                        article['max_new_score'] = item['max_nw_score']
                    else:
                        article['max_new_score'] = 0
                    if 'total_engagement_count' in item['fb_data']:
                        article['fb_like'] = item['fb_data']['total_engagement_count']
                    else:
                        article['fb_like'] = 0
                    if 'tw_count' in item['tw_data']:
                        article['tweet_count'] = item['tw_data']['tw_count']
                    else:
                        item['tw_data']['tw_count'] = 0
                    if 'publisher' in item['source']:
                        article['publisher'] = item['source']['publisher']
                    else:
                        article['publisher'] = "None"
                    if 'uuid' in item:
                        article['uuid'] = item['uuid']
                    else:
                        article['uuid'] = 'None'
                    if 'publication_timestamp' in item:
                        article['published'] = time.strftime('%Y-%m-%d %H:%M', time.localtime(item['publication_timestamp']/1000.0))
                    else:
                        article['published'] = "None"
                    article['fetch'] = current_epoch_time(datetime.now())

                    dummy_category = []
                    for i in article_info['category']:
                        split_list = i.split(',')
                        for itr in split_list:
                            if itr not in dummy_category:
                                dummy_category.append(itr.lower())

                    article_info['category'] = dummy_category
                    if not any(category['category'] in article_info['category'] for category in db_category_list):
                        for category_item in article_info['category']:
                            for interest in db_interest_list:
                                if category_item == interest['interest']:
                                    if category_item not in article['interest']:
                                        article['interest'].append(category_item)

                        if len(article['interest']) <= 0:
                            article['category'] = article_info['category']
                        else:
                            article['category'] = []
                            for int_item in article['interest']:
                                current_interest = filter(lambda member:int_item == member['interest'], db_interest_list)
                                if len(current_interest) == 1:
                                    current_category = filter(lambda member: current_interest[0]['category_id'] == member['_id'], db_category_list)
                                if len(current_category) == 1:
                                    article['category'].append(current_category[0]['category'])

                    else:
                        if article['keywords'] is not None:
                            (article['interest'], return_category_ids) = checking_interest(article['keywords'])
                        article['category'] = article_info['category']

                    key_phrases_list = []
                    raw_key_phrases_list = []
                    interest_category_id = []
                    if article_info['keywords']:
                        keywords_key_phrases = (''.join(map(str, ((article_info['keywords'][0]).decode('ascii', 'ignore')).lower()))).split(",")
                        key_phrases_list += keywords_key_phrases
                        raw_key_phrases_list += keywords_key_phrases
                    if article_info['title']:
                        title_key_phrases = extractKeyphrases(article_info['title'].decode('ascii', 'ignore'))
                        key_phrases_list += list(title_key_phrases)
                        raw_key_phrases_list.append(str(article_info['title'].decode('ascii', 'ignore')))
                    if article_info['description']:
                        description_key_phrases = extractKeyphrases(article_info['description'].decode('ascii', 'ignore'))
                        key_phrases_list += list(description_key_phrases)
                        raw_key_phrases_list.append(str(article_info['description'].decode('ascii', 'ignore')))
                    d = Counter(key_phrases_list)
                    keys_to_remove = ['', ' ', '%', 'an', 'a', ',', 'ii', 'r', 'so', 'is', 'in', 'the', 'nbt', 'us', 'them', 's', '|', 'eisamay', 'navbharat', '-navbharat', 'navbharat times', 'samay', 'india']
                    refactor_key_list = []
                    for key in list(d.keys()):
                        if (key.strip()).lower() not in keys_to_remove and (key.strip()).lower() not in refactor_key_list:
                            refactor_key_list.append((key.strip()).lower())
                    article['created_keys'] = refactor_key_list
                    if article['created_keys'] is not None:
                        (created_interest, interest_category_id) = checking_interest(raw_key_phrases_list)
                        if created_interest is not None:
                            article['interest'] += created_interest
                        if interest_category_id is not None:
                            cat_dict = Counter(interest_category_id)
                            top_order_category = ''
                            top = 0
                            for index, cat_item in enumerate(cat_dict.keys()):
                                if cat_dict[cat_dict.keys()[index]] >= top:
                                    top_order_category = cat_dict.keys()[index]
                                    top = cat_dict[cat_dict.keys()[index]]
                            if top_order_category:
                                supposed_category = __category_service.find_category(top_order_category)
                                article['category'].append(supposed_category['category'])

                    if article['interest']:
                        article['status'] = True
                    else:
                        article['status'] = False
                    __story_service.save_story(article)
                    __fetch_service.save_fetch(fetch)

            except Exception as ex:
                logging.info("Runtime Error: " + ex)

class Grouping:
    __story_service = StoryService()

    def get_cosine_similarity(self, vector1, vector2):
        '''
        calculate cosine distance between two lists of string
        '''
        vec1 = Counter(vector1)
        vec2 = Counter(vector2)
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])
        sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
        sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)
        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    def get_smlr_category_score(self, categories_first=[], categories_second=[]):
        '''
        Checks for similar category in both lists and
        returns score accordingly  '''

        similar_category_score = 0.0
        if any(map(lambda v: v in categories_first, categories_second)):
            similar_category_score = 0.01
            return similar_category_score
        return similar_category_score

    def get_articles_for_grouping(self, gp_count):
        articles = self.__story_service.find_latest_stories()
        for article in articles:
            if "group" not in article:
                gp_count = gp_count + 1
                self.process_grouping(article, gp_count)
                if self.__story_service.db().find({"group":"group"+str(gp_count)}).count() == 0:
                    gp_count = gp_count - 1
            else:
                pass

    def process_grouping(self, p_article, gp_count):
        articles = self.__story_service.find_latest_stories()
        for article in articles:
            if article["_id"] != p_article["_id"]:
                article_cosine_smlr_score = self.get_cosine_similarity(p_article["created_keys"],
                                                                       article["created_keys"])
                similar_category_score = self.get_smlr_category_score(p_article["category"], article["category"])
                article_cosine_smlr_score = article_cosine_smlr_score + similar_category_score

                if article_cosine_smlr_score >= 0.5:
                    article["group"] = "group" + str(gp_count)
                    self.__story_service.update_story(article)


if __name__ == "__main__":
    while True:
        logging.info("Scheduler initialize....")
        logging.info("Start time: " + str(datetime.now()))
        __story_service = StoryService()
        __category_service = CategoryService()
        __interest_service = InterestService()
        __fetch_service = FetchService()
        with open('credentials.json', 'r') as credential_file:
            data = json.load(credential_file)
            newswhip_key = data["key"]
            competitors = data["competitors"]
            watching_stories(competitors)
        stories = __story_service.find_latest_stories()
        if len(stories) > 100:
            logging.info("Grouping initialize....")
            __story_service.reset_group()
            gp_count = 0
            Grouping().get_articles_for_grouping(gp_count)
            logging.info("Grouping completed.")
        logging.info("End time: " + str(datetime.now()))
        time.sleep(3600)
