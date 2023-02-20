# Python CRUD Module
# Joey Paul E. Haynes

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://aacuser:aacuser123@localhost:44278/?authSource=AAC')
        self.database = self.client['AAC']
        # Animals collection
        self.collection = self.database.animals

    def create(self, data):
        """
        Method inserts a document into the MongoDB collection
        Input: data, a dictionary (key/value pairs) for MongoDB API call
        Returns: True if insert is successful, otherwise returns False
        """
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(e)
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query, exclusions):
        """
        Method queries for documents from the MongoDB collection
        Input: query, a dictionary (key/value pair) for MongoDB API call
        Input: exclusions, a dictionary to specify fields to be excluded
        Returns: cursor if successful, otherwise returns error message
        """
        try:
            queryResult = self.collection.find(query, exclusions)
            return queryResult
        except Exception as e:
            print(e)
            return e

    def update(self, query, data):
        """
        Method queries for and changes one or more documents in the collection
        Input: query, a dictionary (key/value pair) for MongoDB API call
        Input: data, a dictionary (key/value pair) that will be used to update collection
        Returns: JSON format if successful, otherwise returns error message
        """
        try:
            self.collection.update_many(query, {"$set": data})
            return {"update status": "success"}
        except Exception as e:
            print(e)
            return e

    def delete(self, query):
        """
        Method queries for and removes one or more documents in the collection
        Input: query, a dictionary (key/value pair) for MongoDB API call
        Returns: JSON format if successful, otherwise returns error message
        """
        try:
            self.collection.delete_many(query)
            return {"delete status": "success"}
        except Exception as e:
            print(e)
            return e

