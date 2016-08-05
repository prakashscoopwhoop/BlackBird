import json
from schema import Schema, And, Use,Optional
class User:
    ID = '_id'
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    USER_NAME = 'username'
    PASSWORD = 'password'
    INTEREST = 'interest'
    ROLE = 'role'
    
    VALIDATOR = Schema(And(Use(json.loads), {
    Optional(ID):object,
    FIRST_NAME:basestring,
    LAST_NAME:basestring,
    USER_NAME:basestring,
    PASSWORD:basestring,
    Optional(INTEREST):list,
    Optional(ROLE):basestring
    }))

class Interest:
    ID = '_id'
    CATEGORY_ID = 'category_id'
    IMAGE = 'image'
    INTEREST = 'interest'
    KEYWORDS = 'keywords'
    
    VALIDATOR = Schema({
    Optional(ID):object,
    CATEGORY_ID:basestring,
    INTEREST:basestring,
    IMAGE:basestring,
    Optional(KEYWORDS):[]
    })

class Story:
    ID = '_id'
    TITLE = 'title'
    URL = 'url'
    DESCRIPTION = 'description'
    KEYWORDS = 'keywords'
    FEATURE_IMAGE = 'feature_image'
    NEW_SCORE = 'new_score'
    MAX_NEW_SCORE = 'max_new_score'
    FB_LIKE = 'fb_like'
    TWEET_COUNT = 'tweet_count'
    PUBLISHER = 'publisher'
    UUID = 'uuid'
    PUBLISHED = 'published'
    FETCH = 'fetch'
    CATEGORY = 'category'
    STATUS = 'status'

    VALIDATOR = Schema(And(Use(json.loads), {
    Optional(ID):object,
    TITLE:basestring,
    URL:basestring,
    DESCRIPTION:basestring,
    KEYWORDS:basestring,
    FEATURE_IMAGE:basestring,
    NEW_SCORE:basestring,
    MAX_NEW_SCORE:basestring,
    FB_LIKE:basestring,
    TWEET_COUNT:basestring,
    PUBLISHER:basestring,
    UUID:basestring,
    PUBLISHED:basestring,
    FETCH:basestring,
    CATEGORY:basestring,
    STATUS:bool
    }))
    
class Category:
    ID = '_id'
    CATEGORY = "category"
    
    VALIDATOR = Schema(And(Use(json.loads), {
    Optional(ID):object,
    CATEGORY: basestring
    }))


class Fetch:
    ID = '_id'
    START_TIME = 'start_time',
    END_TIME = 'end_time'

    VALIDATOR = Schema({
        Optional(ID): object,
        START_TIME: int,
        END_TIME: int})


class Twitter:
    ID = '_id'
    URL = 'url'
    NAME = 'name'
    LOCATION = 'location'
    QUERY = 'query'

    VALIDATOR = Schema({
        Optional(ID): object,
        URL: basestring,
        NAME: basestring,
        LOCATION: basestring,
        QUERY:basestring
    })


class Tweet:
    ID = '_id'
    SCREEN_NAME = 'screen_name'
    USER_NAME = 'user_name'
    ID_STR = 'id_str'
    QUERY = 'query'
    LOCATION = 'location'
    TEXT = 'text'

    VALIDATOR = Schema({
        Optional(ID): object,
        SCREEN_NAME: basestring,
        USER_NAME: basestring,
        ID_STR: int,
        QUERY:basestring,
        LOCATION: basestring,
        TEXT: basestring
    })