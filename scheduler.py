import json
import time
import requests
from app.service import StoryService


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
            comp_art = {'Article Title': item['headline'].encode('utf-8'), 'URL': item['link'].encode('utf-8'),
                        'excerpt': item['excerpt'], 'keywords': item['keywords'],'feature_image':item['image_link'],
                        'New_Score': item['nw_score'], 'Max_New_Score': item['max_nw_score'],
                        'FB_Like': item['fb_data']['like_count'], 'Tweet_Count': item['tw_data']['tw_count'],
                        'Publisher': item['source']['publisher'],"uuid": item['uuid'],
                        'Country_Code': item['source']['country_code'],
                        'Published': time.strftime('%d %b %H:%M',time.localtime(item['publication_timestamp'] / 1000.0))}
            __story_service.save_story(comp_art)

if __name__ == "__main__":
    with open('credentials.json', 'r') as credential_file:
        data = json.load(credential_file)
        newswhip_key = data["key"]
        competitors = data["competitors"]
        __story_service = StoryService()
        watching_stories(competitors)
