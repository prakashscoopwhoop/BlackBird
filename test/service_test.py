import unittest

from app import config

class BaseTest(unittest.TestCase):
    
    def setUp(self):
        client =  config.client
        config.db = client.test_blackbird
        
    def tearDown(self):
        config.client.drop_database("test_blackbird")
        


