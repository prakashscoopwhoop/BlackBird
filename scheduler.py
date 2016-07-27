import json
import time
from datetime import datetime
import re
from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import requests
from app.service import StoryService, CategoryService, InterestService
import domparser


def watching_stories(domain_list):
    """
    watching stories of competitors
    :param domain_list: targeted competitors domain names
    :return:
    """
    db_category_list = __category_service.find_all_categories()
    db_interest_list = __interest_service.find_all_interests()
    for domain in domain_list:
        r = requests.get("https://api.newswhip.com/v1/publisher/" + domain + "/1?key="+newswhip_key)
        # r = requests.get("https://api.newswhip.com/v1/region/india/sports/24?key="+newswhip_key)
        response = json.loads(r.text)
        for item in response['articles']:
            article_info = domparser.element_picker(item['link'].encode('utf-8'))
            if article_info['title'] is not None or article_info['feature_image'] is not None or article_info['url'] is not None:
                article = {'title': '', 'url': '', 'description': '', 'keywords': '', 'feature_image': '','New_score': '',
                        'max_new_score': '', 'fb_like': '', 'tweet_count': '', 'publisher': '', "uuid": '', 'published': '',
                           'category': [], 'interest': [], 'fetch': ''}
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
                    article['keywords'] = item['keywords']

                if item['image_link'] is None:
                    article['feature_image'] = article_info['feature_image']
                else:
                    article['feature_image'] = item['image_link']
                article['New_score'] = item['nw_score']
                article['max_new_score'] = item['max_nw_score']
                article['fb_like'] = item['fb_data']['like_count']
                article['tweet_count'] = item['tw_data']['tw_count']
                article['publisher'] = item['source']['publisher']
                article['uuid'] = item['uuid']
                article['published'] = time.strftime('%Y-%m-%d %H:%M', time.localtime(item['publication_timestamp']/1000.0))
                article['fetch'] = datetime.strftime(datetime.now(), "%Y-%m-%d")

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

                    if len(article['interest'])<=0:
                        article['category'] = article_info['category']
                    else:
                        article['category'] = []
                        for int_item in article['interest']:
                            current_interest = filter(lambda member:int_item == member['interest'],db_interest_list)
                            if len(current_interest) == 1:
                                current_category = filter(lambda member: current_interest[0]['category_id'] == member['_id'], db_category_list)
                            if len(current_category) == 1:
                                article['category'].append(current_category[0]['category'])

                else:
                    if article_info['keywords'] is not None:
                        for interest in db_interest_list:
                            rx = r'\b{0}\b'.format(interest['interest'].lower())
                            pattern = re.compile(rx)
                            match_group = pattern.findall(''.join(map(str, (article_info['keywords'][0]).lower())))
                            if match_group:
                                if interest not in article['interest']:
                                    article['interest'].append(interest['interest'])
                    article['category'] = article_info['category']

                if article['interest']:
                    article['status'] = True
                else:
                    article['status'] = False
                __story_service.save_story(article)

if __name__ == "__main__":
    __story_service = StoryService()
    __category_service = CategoryService()
    __interest_service = InterestService()
    with open('credentials.json', 'r') as credential_file:
        data = json.load(credential_file)
        newswhip_key = data["key"]
        competitors = data["competitors"]
        watching_stories(competitors)
