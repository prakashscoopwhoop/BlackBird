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
        user_interest = []
        if user_id is not isinstance(user_id, ObjectId):
            user_id = ObjectId(user_id)
        user = self.db().find_one(user_id)
        if user is not None:
            for interest in user[User.INTEREST]:
                for sub_category in InterestService().find_interests_by_sub_category(interest):
                    user_interest.append(sub_category)
        return user_interest
    
class InterestService:
    
    def db(self):
        return config.db['interests']
    
    def save_interest(self,interest):
        interest_id = self.db().save(interest)
        interest[Interest.ID]= str(interest_id)
        return interest
    
    def find_interests_by_category(self,category):
        catagory_data = []
        interests = self.db().find({Interest.CATEGORY:category})
        for interest in interests:
            interest[Interest.ID]= str(interest[Interest.ID])
            catagory_data.append(interest)
        return catagory_data
    
  
    def find_interests_by_sub_category(self,sub_category):
        sub_catagory_data = []
        interests = self.db().find({Interest.SUB_CATEGORY:sub_category})
        for interest in interests:
            interest[Interest.ID]= str(interest[Interest.ID])
            sub_catagory_data.append(interest)
        return sub_catagory_data
    
    def find_all_categories(self):
        all_categories = []
        categories = self.db().find()
        for category in categories:
            if category[Interest.CATEGORY] not in all_categories:
                all_categories.append(category[Interest.CATEGORY])
        return all_categories
    