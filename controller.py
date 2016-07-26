from bottle import route, run, static_file, template, error,request
from app.service import UserService,InterestService, CategoryService,\
    StoryService
from app.utils import RestResponse
from app.config import logging
import httplib
from app.validator import User,Interest


#Error handler
@error(404)
def error404(error):
    return template('templates/error.html')


# Static Routes
@route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='templates/js')


@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='templates/css')


@route('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='templates/images')


@route('/fonts/<filename:re:.*\.(otf|eot|ttf|woff|woff2|svg)>')
def fonts(filename):
    return static_file(filename, root='templates/fonts')


@route('/login/<username>/<password>')
def login(username,password):
    user = __user_service.login(username, password)
    if user is None:
        return RestResponse(data={}, status = httplib.UNAUTHORIZED,
                            messages="Username or Password is incorrect!!", success = False).to_json()
    return RestResponse(user).to_json()


@route('/')
def index():
    return template('templates/login.html')


@route('/interest')
def interest_page():
    return template('templates/interest.html')


@route('/interest/<category_id>')
def category_wise_interest(category_id):
    interests = __interest_service.find_interests_by_category(category_id)
    return RestResponse(interests).to_json()


@route('/my_interest/<user_id>')
def get_user_interest(user_id):
    interest = __user_service.find_user_interests(user_id)
    if interest is not None:
        return RestResponse(interest).to_json()
    else:
        return RestResponse(data={}, status = httplib.NOT_FOUND,
                            messages="user is not found!!", success = False).to_json()


@route('/set_interest/<user_id>/<ur_interest>',method='PUT')
def set_user_interest(user_id,ur_interest):
    ur_interest = ur_interest.split(',')
    user = __user_service.add_user_interest(user_id, ur_interest)
    if user is not None:
        return RestResponse(user).to_json()
    else:
        return RestResponse(data={}, status = httplib.NOT_FOUND,
                            messages="user is not found!!", success = False).to_json()


@route('/all_category')
def get_all_categories():
    all_categories =__category_service.find_all_categories()
    return RestResponse(all_categories).to_json()


@route('/createUser')
def create_user():
    return template('templates/createUser.html')


@route('/editUser')
def edit_user():
    return template('templates/editUser.html')

@route('/dashboard')
def dashboard():
    return template('templates/dashboard.html')

@route('/createInterest')
def add_interest_page():
    return template('templates/createInterest.html')


@route('/save_user/<user>', method='POST')
def register_user(user):
    try:
        user = User.VALIDATOR.validate(user)
        saved_user = __user_service.register(user)
        if saved_user is None:
            return RestResponse(data={}, status = httplib.CONFLICT,
                            messages="Username already exists!!", success = False).to_json()
        return RestResponse(saved_user).to_json()
    except Exception as e:
        logging.error(e)
        return RestResponse(data={}, status = httplib.BAD_REQUEST,
                            messages="Enter Invalid Inputs ", success = False).to_json()


@route('/update_user/<user>', method='POST')
def update_user(user):
    try:
        updated_user = __user_service.update_user(user)
        if updated_user is None:
            return RestResponse(data={}, status = httplib.NOT_FOUND,
                            messages="user is not exists!!", success = False).to_json()
        return RestResponse(updated_user).to_json()
    except Exception as e:
        logging.error(e)
        return RestResponse(data={}, status = httplib.BAD_REQUEST,
                            messages="Enter Invalid Inputs ", success = False).to_json()


@route('/all_users')
def get_all_users():
    users = __user_service.find_all_users()
    return RestResponse(users).to_json()


@route('/remove_user/<user_id>',method='DELETE')
def remove_user(user_id):
    status =__user_service.remove_user(user_id)
    if status:
        return RestResponse(data={}, status = httplib.OK,
                            messages="user is removed successfully", success = True).to_json()
    else:
        return RestResponse(data={}, status = httplib.NOT_FOUND,
                            messages="user is not found", success = False).to_json()


@route('/add_interest/', method='POST')
def set_interest():
    try:
        interest = request.json
        interest = Interest.VALIDATOR.validate(interest)
        saved_interest = __interest_service.save_interest(interest)
        if saved_interest is None:
            return RestResponse(data={}, status = httplib.CONFLICT,
                            messages="interest already exists or relative category not exists !!", success = False).to_json()
        return RestResponse(saved_interest).to_json()
    except Exception as e:
        logging.error(e)
        return RestResponse(data={}, status = httplib.BAD_REQUEST,
                            messages="Enter Invalid Inputs ", success = False).to_json()
     
     
@route('/get_article/<interest_id>')                       
def get_article_by_interest_wise(interest_id):
    interest_id = interest_id.split(',')
    articles = __story_service.get_stories(interest_id)
    return RestResponse(articles).to_json()


@route('/all_interest')
def get_all_interests():
    all_interest = __interest_service.find_all_interests()
    return RestResponse(all_interest).to_json()

@route('/editInterest')
def edit_interest_page():
    return template('templates/editInterest.html')

@route('/get_interest/<interest_id>')
def get_interest(interest_id):
    interest = __interest_service.find_interest(interest_id)
    if interest is not None:
        interest["_id"] = str( interest["_id"])
        return RestResponse(interest).to_json()
    else:
        return RestResponse(data={}, status = httplib.NOT_FOUND,
                            messages="user is not found", success = False).to_json()
                            
@route('/add_interest/', method='PUT')                            
def edit_interest():
    try:
        interest = request.json
        interest = Interest.VALIDATOR.validate(interest)
        updated_interest = __interest_service.update_interest(interest)
        if updated_interest is None:
            return RestResponse(data={}, status = httplib.CONFLICT,
                            messages="interest already exists or relative category not exists !!", success = False).to_json()
        return RestResponse(updated_interest).to_json()
    except Exception as e:
        logging.error(e)
        return RestResponse(data={}, status = httplib.BAD_REQUEST,
                            messages="Enter Invalid Inputs ", success = False).to_json()
    


if __name__ == "__main__":
    __user_service = UserService()
    __interest_service = InterestService()
    __category_service = CategoryService()
    __story_service = StoryService()
    
    run(host='0.0.0.0', port=8889, server='waitress')
    logging.info("server running....")
