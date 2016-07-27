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
    