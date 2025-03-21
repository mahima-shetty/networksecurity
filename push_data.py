import os  # Importing the os module to interact with the operating system
import sys  # Importing the sys module 
import json  # Importing the json module

from dotenv import load_dotenv
import pymongo.mongo_client  # Importing the load_dotenv function from the dotenv package
load_dotenv()  # Loading environment variables from a .env file

# Fetching the MongoDB connection URL from the environment variables
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

# Printing the MongoDB connection URL (this may expose sensitive data if printed in production)
print(MONGO_DB_URL)

import certifi

ca = certifi.where()

import pandas as pd
import numpy as np

import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract():
    
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def cv_to_json_converter(self, file_path):
        """
        Converts a CSV file to a list of JSON records.
        
        Parameters:
        file_path (str): The path to the CSV file.
        
        Returns:
        list: A list of JSON records converted from the CSV file.
        
        Raises:
        NetworkSecurityException: If an error occurs while processing the CSV file.
        """
        try: 
            data = pd.read_csv(file_path)  # Reading the CSV file using pandas
            data.reset_index(drop=True, inplace=True)  # Resetting the index of the DataFrame
            records = list(json.loads(data.T.to_json()).values())  # Converting DataFrame to JSON and extracting values as a list
            return records  # Returning the JSON records
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)  # Raising a custom exception if an error occurs
    
    import pymongo  # Importing pymongo to interact with MongoDB

    def insert_data_mongodb(self, records, database, collection):
        """
        Inserts multiple records into a MongoDB collection.

        Parameters:
        records (list): A list of dictionaries representing the documents to insert.
        database (str): The name of the MongoDB database.
        collection (str): The name of the MongoDB collection.

        Returns:
        int: The number of records inserted into the collection.

        Raises:
        NetworkSecurityException: If an error occurs during the insertion process.
        """
        try:
            # Storing the parameters as instance variables (though unnecessary in a function)
            self.database = database
            self.collection = collection
            self.records = records

            # Establishing a connection to the MongoDB server
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            # Incorrect usage: `self.mongo_client(database)` should be `self.mongo_client[database]`
            self.database = self.mongo_client[self.database]  # Accessing the database
            self.collection = self.database[self.collection]  # Accessing the collection

            # Inserting multiple records into the collection
            self.collection.insert_many(self.records)

            # Returning the number of inserted records
            return len(self.records)

        except Exception as e:
            # Raising a custom exception in case of any failure
            raise NetworkSecurityException(e, sys)


if __name__ == '__main__':
    FILE_PATH = "Network_Data\Phishing_Legitimate_full.csv"
    DATABASE = "MahimaShetty"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_converter(file_path=FILE_PATH)
    no_of_records=networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(no_of_records)
    