import tweepy
import json
from app.service import TwitterService


def get_twitter():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    __twitter_service.remove_twitter()
    for idx, place in enumerate(locationID):
        get_trend = api.trends_place(str(place))
        data = get_trend[0]["trends"]
        for idxx, trend in enumerate(data):
            new_dict = {"url": (trend["url"].encode('utf-8')+"&src=typd").replace("http://", "https://"), "query": (trend["query"]).replace('%23', '#').replace('%22', '"').encode('utf-8'), "location":location[idx], "name": trend["name"].encode('utf-8')}
            __twitter_service.save_twitter(new_dict)


if __name__ == "__main__":
    __twitter_service = TwitterService()
    with open('credentials.json', 'r') as credential_file:
        json_obj = json.load(credential_file)
        consumer_key = json_obj['twitter']['TW_CONSUMER_KEY']
        consumer_secret = json_obj['twitter']['TW_CONSUMER_SECRET']
        access_token = json_obj['twitter']['TW_ACCESS_TOKEN']
        access_token_secret = json_obj['twitter']['TW_ACC_TOKEN_SECRET']
        location = json_obj['twitter']['location']
        locationID = json_obj['twitter']['locationID']
        get_twitter()