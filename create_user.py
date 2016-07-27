from app.validator import User
from app.utils import encrypt_password
from app.service import UserService

if __name__ == "__main__":
    __user_service = UserService()
    user = {}
    user[User.FIRST_NAME] = 'kumar'
    user[User.LAST_NAME] = 'mrigendra'
    user[User.USER_NAME] = 'kumar'
    user[User.PASSWORD] = encrypt_password("1234")
    user[User.INTEREST] = ["Internet", "Science", "Music", "Logic"]
    __user_service.db().save(user)
    print "User created successfully"