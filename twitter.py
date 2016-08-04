import tweepy
import json
from app.service import TwitterService, TweetService


def get_top_tweets(query, location):
    for tweet in tweepy.Cursor(api.search, q=query, result_type="mixed", include_entities=True, lang="en").items(5):
        tweet_dict = {"query": query, "location": location, "screen_name": tweet.user.screen_name, "user_name": tweet.user.name.encode('utf-8'), "text": tweet.text.encode('utf-8'), "id_str": tweet.id_str}
        __tweet_service.save_tweet(tweet_dict)


def get_twitter():
    __twitter_service.remove_twitter()
    __tweet_service.remove_tweet()
    for idx, place in enumerate(locationIDs):
        get_trend = api.trends_place(str(place))
        data = get_trend[0]["trends"]
        for trend in data[0:5]:
            new_dict = {"url": (trend["url"].encode('utf-8')+"&src=typd").replace("http://", "https://"), "query": (trend["query"]).replace('%23', '#').replace('%22', '"').encode('utf-8'), "location":locations[idx], "name": trend["name"].encode('utf-8')}
            __twitter_service.save_twitter(new_dict)
            get_top_tweets(new_dict['query'], new_dict['location'])


if __name__ == "__main__":
    __twitter_service = TwitterService()
    __tweet_service = TweetService()
    with open('credentials.json', 'r') as credential_file:
        json_obj = json.load(credential_file)
        consumer_key = json_obj['twitter']['TW_CONSUMER_KEY']
        consumer_secret = json_obj['twitter']['TW_CONSUMER_SECRET']
        access_token = json_obj['twitter']['TW_ACCESS_TOKEN']
        access_token_secret = json_obj['twitter']['TW_ACC_TOKEN_SECRET']
        locations = json_obj['twitter']['location']
        locationIDs = json_obj['twitter']['locationID']
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        get_twitter()