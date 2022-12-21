import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
import certifi
import os
ca = certifi.where()

class MongoClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                # mongo_db_url = "mongodb+srv://Vinit21592:vins21592@cluster0.dl9uoq9.mongodb.net/?retryWrites=true&w=majority"
                MongoClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e
