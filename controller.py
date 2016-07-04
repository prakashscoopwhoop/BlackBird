from bottle import route, run, static_file, template
from app.service import UserService,InterestService
from app.utils import RestResponse
from app.config import logging
import httplib


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


@route('/<filename:re:.*\.(otf|eot|ttf|woff|svg)>')
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

@route('/interest/<category>')
def category_wise_interest(category):
    interests = __interest_service.find_interests_by_category(category)
    return RestResponse(interests).to_json()

@route('/my_interest/<user_id>')
def user_interest(user_id): 
    interest = __user_service.find_user_interests(user_id)
    return RestResponse(interest).to_json()

@route('/all_category')
def get_all_categories():
    all_categories =__interest_service.find_all_categories()
    return RestResponse(all_categories).to_json()
    
if __name__ == "__main__":
    __user_service = UserService()
    __interest_service = InterestService()
    run(host='0.0.0.0', port=8889, server='waitress')
    logging.info("server running....")




