from app.schema import User
from app.utils import encrypt_password
from app import config
from app.config import PAGE_SIZE


class UserService:
    
    def db(self):
        config.db['users']
    
    def register(self,user):
        '''
        register a new user
        '''
        
        if self.db().find_one({User.USER_NAME:user[User.USER_NAME]}) is None :
            user[User.PASSWORD]= encrypt_password( user[User.PASSWORD])
            if 'role' not in user:
                user[User.ROLE]= 'member'
            user_id = self.db().save(user)
            user[User.ID]= user_id
            return user
        else:
            return
    
    def login(self,username,password):
        '''
        login via user name
        '''
        en_password = encrypt_password(password)
        user = self.db().find_one({User.USER_NAME:username,User.PASSWORD:en_password})
        if user is None:
            return
        return user
    
    def change_user_role(self,user_id,role):
        '''
        change user role
        '''
        user = self.db().find_one(user_id)
        if user is not None:
            user['role']=role
            return self.db().save(user)
        else:
            return 
        
    def find_user(self,user_id):
        return self.db().find({User.ID:user_id})
    
    def find_all_users(self):
        return self.db.find()
    
    def find_by_pagination(self, page=0, size=PAGE_SIZE):
        return self.db().find(skip=page * size, limit=size)
        
