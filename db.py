import pymongo
import json
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient("mongodb://ec2-18-205-105-6.compute-1.amazonaws.com:27017")
db = client.test
collection = db.yelp_reviews
requesting = []

with open(r"./yelp_academic_dataset_review.json") as f:
    for jsonObj in f:
        if len(requesting) < 30:
            myDict = json.loads(jsonObj)
            requesting.append(InsertOne(myDict))
        else:
            break

result = collection.bulk_write(requesting)
client.close()

print("done")
