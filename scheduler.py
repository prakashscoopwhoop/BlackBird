import json
import time
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
        r = requests.get("https://api.newswhip.com/v1/publisher/" + domain + "/1?key="+newswhip_key)
        response = json.loads(r.text)
        for item in response['articles']:
            print item['link'].encode('utf-8')
            domparser.element_picker(item['link'].encode('utf-8'))
            comp_art = {'title': item['headline'].encode('utf-8'), 'url': item['link'].encode('utf-8'),
                        'description': item['excerpt'], 'keywords': item['keywords'],'feature_image':item['image_link'],
                        'New_score': item['nw_score'], 'max_new_score': item['max_nw_score'],
                        'fb_like': item['fb_data']['like_count'], 'tweet_count': item['tw_data']['tw_count'],
                        'publisher': item['source']['publisher'],"uuid": item['uuid'],
                        'published': time.strftime('%d %b %H:%M',time.localtime(item['publication_timestamp'] / 1000.0))}
            # __story_service.save_story(comp_art)

if __name__ == "__main__":
    with open('credentials.json', 'r') as credential_file:
        data = json.load(credential_file)
        newswhip_key = data["key"]
        competitors = data["competitors"]
        __story_service = StoryService()
        watching_stories(competitors)
