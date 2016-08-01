import hashlib
import httplib
import json,os,urllib

salt = "swblackbird"

def encrypt_password(password):
    '''
    encrypt password by using md5
    '''
    md5_checksum = hashlib.md5()
    md5_checksum.update(salt+password)
    return md5_checksum.hexdigest()

class RestResponse:
    __entity = {}

    def __init__(self, data={}, status = httplib.OK, messages=None, success = True):
        '''
        
        :param data: Response data of Rest call.
        :param status: Response status of Rest call , default is 1 means success.
        :param messages: Response message of Rest call , default is None.
        '''
        self.__entity['data'] = data
        self.__entity['status'] = status
        self.__entity['messages'] = messages
        self.__entity['success'] = success
    def to_json(self):
        '''
        :return json-encoded.
        '''
        return json.dumps(self.__entity)
    
    
def download_images_locally(url):
    
    cwd = os.getcwd()
    if not os.path.exists('templates/images'):
        os.makedirs('templates/images')
    filename = url.split('/')[-1]+".jpg"
    os.chdir('templates/images')
    urllib.urlretrieve(url, filename)
    os.chdir(cwd)
    return filename

def remove_image(image_name):
    cwd = os.getcwd()
    os.chdir('templates/images')
    if os.path.exists(image_name):
        os.remove(image_name)
    else:
        print "file not exist in templates/images directory."
    os.chdir(cwd)
    
class TestDataBuilderService:
    
    def build_interest(self):
        self.__create_new_interest()
    
    def build_category(self):
        self.__create_new_category()
    
    
    def build_story(self):
        self.__create_new_story()
        
    def __create_new_interest(self):
        pass
         
    
