from sensor.configuration.mongo_db_connection import MongoClient

if __name__ == '__main__':
    mongodb_client = MongoClient()
    print("collection name:",mongodb_client.database.list_collection_names())