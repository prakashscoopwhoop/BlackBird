from app.validator import User, Interest, Story
from app.utils import encrypt_password
from app import config
from app.config import PAGE_SIZE
from bson.objectid import ObjectId
import json


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
        user_dto =[]
        users =  self.db().find()
        for user in users:
            entity ={}
            entity[User.ID]= str(user[User.ID])
            entity[User.FIRST_NAME]= user[User.FIRST_NAME]
            entity[User.LAST_NAME] = user[User.LAST_NAME]
            entity[User.USER_NAME] = user[User.USER_NAME]
            user_dto.append(entity)
        return user_dto
    
    def find_users_by_pagination(self, page=0, size=PAGE_SIZE):
        user_dto =[]
        users =  self.db().find(skip=page * size, limit=size)
        for user in users:
            entity ={}
            entity[User.ID]= str(user[User.ID])
            entity[User.FIRST_NAME]= user[User.FIRST_NAME]
            entity[User.LAST_NAME] = user[User.LAST_NAME]
            entity[User.USER_NAME] = user[User.USER_NAME]
            user_dto.append(entity)
        return user_dto
    
    def find_user_interests(self,user_id):
        user = self.find_user(user_id)
        if user is not None:
            return InterestService().find_my_interests(user[User.INTEREST])
        else:
            return
    
    def update_user(self,user):
        user = json.loads(user)
        if User.ID not in user:
            return
        existing_user = self.find_user(user[User.ID])
        if existing_user is not None:
            existing_user.update(user)
            user_id = self.db().save(existing_user)
            user[User.ID]= str(user_id)
            return user
        else:
            return
        
    def remove_user(self,user_id):
        user = self.find_user(user_id)
        if user is None:
            return False
        self.db().remove(user[User.ID])
        return True 
           
    def add_user_interest(self,user_id,interest):
        user = self.find_user(user_id)
        if user is not None:
            for inst_id in interest:
                if str(inst_id) not in user[User.INTEREST]:
                    user[User.INTEREST].append(str(inst_id))
            user_id = self.db().save(user)
            user[User.ID] = str(user_id)
            return user
        else:
            return
        
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
    
    def find_interest(self,interest_id):
        if interest_id is not isinstance(interest_id, ObjectId):
            interest_id = ObjectId(interest_id)
        return self.db().find_one(interest_id)
    
  
    def find_my_interests(self,interests):
        interest_data = []
        for ins_id in interests:
            interest = self.find_interest(ins_id)
            if interest is not None:
                interest_data.append(interest)
        return interest_data
    
    def find_all_categories(self):
        all_categories = []
        categories = self.db().find()
        for category in categories:
            if category[Interest.CATEGORY] not in all_categories:
                all_categories.append(category[Interest.CATEGORY])
        return all_categories


class StoryService:

    def db(self):
        return config.db['stories']

    def save_story(self,story):
        if self.db().find_one({Story.UUID:story[Story.UUID]}) is None :
            story_id = self.db().save(story)
            story[Story.ID] = str(story_id)
            return story
        else:
            return