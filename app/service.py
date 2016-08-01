from app.validator import User, Interest, Story,Category, Fetch
from app.utils import encrypt_password, download_images_locally, remove_image
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
        user = self.db().find_one(user_id)
        return user
    
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
        interest[Interest.INTEREST] = interest[Interest.INTEREST].lower()
        
        if self.db().find_one({Interest.INTEREST:interest[Interest.INTEREST]}) is None:
            category = CategoryService().find_category(interest[Interest.CATEGORY_ID])
            if category is not None:
                if Interest.KEYWORDS not in interest:
                    interest[Interest.KEYWORDS] = []
                interest[Interest.IMAGE]=download_images_locally(interest[Interest.IMAGE])
                interest_id = self.db().save(interest)
                interest[Interest.ID]= str(interest_id)
                return interest
            else:
                return
        else:
            return
        
    def update_interest(self,interest):
        existing_interest = self.find_interest(interest[Interest.ID])
        if existing_interest is not None:
            if interest[Interest.IMAGE] == existing_interest[Interest.IMAGE]:
                pass
            elif (interest[Interest.IMAGE] != existing_interest[Interest.IMAGE] ) and ("http" or "https" in interest[Interest.IMAGE]):
                remove_image(existing_interest[Interest.IMAGE])
                interest[Interest.IMAGE] = download_images_locally(interest[Interest.IMAGE])
            else:
                pass
            if interest[Interest.ID]  is not isinstance(interest[Interest.ID], ObjectId) :
                interest[Interest.ID] = ObjectId(interest[Interest.ID])
            interest_id = self.db().save(interest)
            interest[Interest.ID]= str(interest_id)
            return interest
        else:
            return 
        
    def find_interests_by_category(self,category_id):
        catagory_data = []
        interests = self.db().find({Interest.CATEGORY_ID:category_id})
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
                interest[Interest.ID] = str(interest[Interest.ID])
                interest_data.append(interest)
        return interest_data

    def find_all_interests(self):
        all_interests = []
        interests = self.db().find()
        for interest in interests:
            interest[Interest.ID] = str(interest[Interest.ID])
            all_interests.append(interest)
        return all_interests


class CategoryService:
    
    def db(self):
        return config.db['categories']
    
    def find_all_categories(self):
        all_categories = []
        categories = self.db().find()
        for category in categories:
            category[Category.ID] = str(category[Category.ID])
            all_categories.append(category)
        return all_categories 
    
    def save_category(self, category):
        if self.db().find_one({Category.CATEGORY:category[Category.CATEGORY]}) is None:
            category_id = self.db().save(category)
            category[Category.ID]= str(category_id)
            return category
        else:
            return 
        
    def find_category_by_name(self,name):
        category = self.db().find_one({Category.CATEGORY:name})
        if category is not None:
            category[Category.ID] = str(category[Category.ID])
            return category
        return
    
    def find_category(self,category_id):
        if category_id is not isinstance(category_id, ObjectId):
            category_id = ObjectId(category_id)
        return self.db().find_one(category_id)
    
    def remove_category(self,category_id):
        categoty = self.find_category(category_id)
        if categoty is None:
            return False
        self.db().remove(categoty[Category.ID])
        return True 
    def remove(self):
        remove_image("_2s_OBbqQ-O348BjcTF13Q.jpg")
    

class StoryService:
    
    def db(self):
        return config.db['stories']

    def save_story(self,story):
        if self.db().find_one({Story.UUID:story[Story.UUID]}) is None:
            story_id = self.db().save(story)
            story[Story.ID] = str(story_id)
            return story
        else:
            return
        
    def get_stories(self,interest_name):
        articles = []
        stories = self.db().find({"interest":{"$in":interest_name}})
        for story in stories:
            story["_id"] = str(story["_id"])
            articles.append(story)
        return articles
        
    def find_latest_stories(self):  #, from_time, end_time
        all_stories = []
        fetched = FetchService().get_fetch()
        stories = self.db().find({"fetch": {"$gte": fetched['start_time'], "$lt": fetched['end_time']}})
        for story in stories:
            story[Story.ID] = str(story[Story.ID])
            all_stories.append(story)
        return all_stories


class FetchService:

    def db(self):
        return config.db['fetch']

    def save_fetch(self, fetch):
        if self.db().find().count() > 0:
            self.db().remove()
        fetch_id = self.db().save(fetch)
        fetch[Fetch.ID] = str(fetch_id)
        return fetch

    def get_fetch(self):
        fetch = self.db().find_one()
        if fetch is not None:
            fetch[Fetch.ID] = str(fetch[Fetch.ID])
            return fetch