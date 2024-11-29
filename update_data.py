from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri= "mongodb+srv://nileshsinha16:nileshsinha@cluster0.qlyxo.mongodb.net/?retryWrites=true&w=majority"


#create a new client and connect to server
client = MongoClient(uri)


#create database name and collection name
DATABASE_NAME= "sensor"
COLLECTION_NAME = "waterfault"

##Read the CSV file
df=pd.read_csv("C:\Users\NILESH SINHA\OneDrive\Documents\ML Project\Sencor Project\notebooks\wafer_23012020_041211.csv")

df.head()

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

json_record

##UPload the database on Mongo server
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)