from pymongo import MongoClient
import logging

# logger
logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename='black_bird.log',
            filemode='w')

# connect to the running mongod instance
client =  client = MongoClient()
#switch to the UKM database, if not exist then create new db.
db = client.black_bird

# default page size
PAGE_SIZE = 1000

