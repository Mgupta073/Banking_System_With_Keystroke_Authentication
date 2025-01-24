import pymongo

__author__ = "krish"


class Database:
    URI = "mongodb+srv://krishjain2468:Krish123@cluster0.0l97h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["Bank"]

    @staticmethod
    def insert(collection, data):
        # Use insert_one for inserting a single document
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        # Print collection and query for debugging purposes
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def find_collection(collection):
        return Database.DATABASE[collection].find()

    @staticmethod
    def update(collection, query, values):
        # Use update_one for updating a single document
        Database.DATABASE[collection].update_one(query, values)
        return Database.DATABASE[collection]

    @staticmethod
    def delete_one_record(collection, query):
        return Database.DATABASE[collection].delete_one(query)

    @staticmethod
    def delete_many_record(collection, query):
        return Database.DATABASE[collection].delete_many(query)