import json
from schema import Schema, And, Use,Optional
class User:
    ID = '_id'
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    USER_NAME = 'user_nanme'
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
    CATEGORY = 'category'
    IMAGE = 'image'
    SUB_CATEGORY = 'sub_category'
    INTEREST='interest'
    
    VALIDATOR = Schema(And(Use(json.loads), {
    Optional(ID):object,
    CATEGORY:basestring,
    SUB_CATEGORY:basestring,
    IMAGE:basestring
    }))