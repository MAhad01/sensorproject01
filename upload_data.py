from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri="mongodb+srv://ahad:ahad@cluster0.tb4jr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create new client and connect to server
client=MongoClient(uri)

#create database and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"

df=pd.read_csv("notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0", axis=1)

json_records=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)