from bottle import route, run, static_file
from app.service import UserService
from app.utils import RestResponse
import httplib

@route(':filename#.*#')
def static_file_serve(filename):
    return static_file(filename, root='../ui/templates/static')

@route('/login/<user_name>/<password>')
def login(user_name,password):
    user = __user_service.login(user_name, password)
    if user is None:
        return RestResponse(data={}, status = httplib.UNAUTHORIZED, 
                            messages="user_name or password is incorrect", success = False)
    return RestResponse(user).to_json()

if __name__=="__main__":
    __user_service  = UserService()
    run(host='0.0.0.0', port=8889, server='waitress')




