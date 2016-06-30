import hashlib
import httplib
import json

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