from pymongo import MongoClient
import logging

# logger
logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename='blackbird.log',
            filemode='w')

# connect to the running mongod instance
client = MongoClient('mongodb://127.0.0.1', 27017)
#switch to the UKM database, if not exist then create new db.
db = client.blackbird

# default page size
PAGE_SIZE = 1000

