from app.validator import User, Interest
from app.utils import encrypt_password
from app import config
from app.config import PAGE_SIZE
from bson.objectid import ObjectId


class UserService:
    
    def db(self):
        return config.db['users']
    
    def register(self,user):
        '''
        register a new user
        '''
        
        if self.db().find_one({User.USER_NAME:user[User.USER_NAME]}) is None :
            user[User.PASSWORD]= encrypt_password( user[User.PASSWORD])
            if 'role' not in user:
                user[User.ROLE]= 'member'
            if 'interest' not in user:
                user[User.INTEREST]=[]
            user_id = self.db().save(user)
            user[User.ID]= str(user_id)
            return user
        else:
            return
    
    def login(self,username, password):
        '''
        login via user name
        '''
        en_password = encrypt_password(password)
        user = self.db().find_one({User.USER_NAME:username, User.PASSWORD:en_password})
        if user is None:
            return
        user[User.ID]= str(user[User.ID])
        return user
    
    def change_user_role(self,user_id,role):
        '''
        change user role
        '''
        if user_id is not isinstance(user_id, ObjectId):
            user_id = ObjectId(user_id)
        user = self.db().find_one(user_id)
        if user is not None:
            user['role']=role
            return self.db().save(user)
        else:
            return 
        
    def find_user(self,user_id):
        if user_id is not isinstance(user_id, ObjectId):
            user_id = ObjectId(user_id)
        return self.db().find_one(user_id)
    
    def find_all_users(self):
        return self.db.find()
    
    def find_by_pagination(self, page=0, size=PAGE_SIZE):
        return self.db().find(skip=page * size, limit=size)
    
    def find_user_interests(self,user_id):
        if user_id is not isinstance(user_id, ObjectId):
            user_id = ObjectId(user_id)
        user = self.db().find_one(user_id)
        if user is not None:
            return user[User.INTEREST]
        return
    
class InterestService:
    
    def db(self):
        return config.db['interests']
    
    def save_interest(self,interest):
        interest_id = self.db().save(interest)
        interest[Interest.ID]= str(interest_id)
        return interest
    
    def find_interests_by_category(self,category):
        return self.db().find({Interest.CATEGORY:category})
  
    def find_interests_by_sub_category(self,sub_category):
        return self.db().find({Interest.SUB_CATEGORY:sub_category})
    