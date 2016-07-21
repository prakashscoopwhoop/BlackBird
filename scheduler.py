import json
import time
from datetime import datetime
from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import requests
from app.service import StoryService
import domparser

def page_info(url):
    """
    Fetching  category and author name from DOM
    :param url: Article page path
    :return: Author Name & Category
    """
    author = ""
    title = ""
    categories = []
    response = urllib2.urlopen(url)
    source = response.read()
    soup = BeautifulSoup(source, 'html.parser')
    for meta in soup.find_all('meta'):
        if 'category' == meta.get('property'):
            categories.append(str(meta.get('content')))
        if 'article:author' == meta.get('property'):
            author = str(meta.get('content'))
        if 'og:title' == meta.get('property'):
            title = str(meta.get('content').encode('utf-8'))
    return title, author, categories


def watching_stories(domain_list):
    """
    watching stories of competitors
    :param domain_list: targeted competitors domain names
    :return:
    """
    for domain in domain_list:
        r = requests.get("https://api.newswhip.com/v1/publisher/" + domain + "/48?key="+newswhip_key)
        response = json.loads(r.text)
        print domain
        for item in response['articles'][1:2]:
            print "item exists"
            # print item['link'].encode('utf-8')
            article_info = domparser.element_picker(item['link'].encode('utf-8'))
            article = {'title': '', 'url': '', 'description': '', 'keywords': '', 'feature_image': '','New_score': '',
                    'max_new_score': '', 'fb_like': '', 'tweet_count': '', 'publisher': '', "uuid": '', 'published': ''}

            # comp_art1 = {'title': item['headline'].encode('utf-8'), 'url': item['link'].encode('utf-8'),
            #             'description': item['excerpt'], 'keywords': item['keywords'],'feature_image':item['image_link'],
            #             'New_score': item['nw_score'], 'max_new_score': item['max_nw_score'],
            #             'fb_like': item['fb_data']['like_count'], 'tweet_count': item['tw_data']['tw_count'],
            #             'publisher': item['source']['publisher'],"uuid": item['uuid'],
            #             'published': time.strftime('%d %b %H:%M',time.localtime(item['publication_timestamp'] / 1000.0))}
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
            article['category'] = article_info['category']
            article['interest'] = article_info['interest']
            __story_service.save_story(article)

if __name__ == "__main__":
    with open('credentials.json', 'r') as credential_file:
        data = json.load(credential_file)
        newswhip_key = data["key"]
        competitors = data["competitors"]
        __story_service = StoryService()
        watching_stories(competitors)
