from bottle import route, run, static_file
from app.service import UserService
from app.utils import RestResponse
from app.config import logging
import httplib


# Static Routes
@route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='ui/templates/static/js')

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='ui/templates/static/css')

@route('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='ui/templates/static/image')

@route('/<filename:re:.*\.(otf|eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='ui/templates/static/fonts')

@route('/login/<username>/<password>')
def login(username,password):
    user = __user_service.login(username, password)
    if user is None:
        return RestResponse(data={}, status = httplib.UNAUTHORIZED, 
                            messages="user_name or password is incorrect", success = False).to_json()
    return RestResponse(user).to_json()


if __name__=="__main__":
    __user_service  = UserService()
    run(host='0.0.0.0', port=8889, server='waitress')
    logging.info("server running....")




