from pymongo import MongoClient

# connect to the running mongod instance
client =  client = MongoClient()
#switch to the UKM database, if not exist then create new db.
db = client.black_bird

# default page size
PAGE_SIZE = 1000

