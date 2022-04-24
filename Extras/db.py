import pymongo
import json
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient("mongodb://ec2-18-205-105-6.compute-1.amazonaws.com:27017")
db = client.test

DOCUMENT_COUNT = 150

requesting = []
collection = db.yelp_reviews
with open(r"./yelp_academic_dataset_review.json") as f:
    for jsonObj in f:
        if len(requesting) < DOCUMENT_COUNT:
            myDict = json.loads(jsonObj)
            requesting.append(InsertOne(myDict))
        else:
            break

result = collection.bulk_write(requesting)

requesting = []
collection = db.yelp_users
with open(r"./yelp_academic_dataset_user.json") as f:
    for jsonObj in f:
        if len(requesting) < DOCUMENT_COUNT:
            myDict = json.loads(jsonObj)
            requesting.append(InsertOne(myDict))
        else:
            break

result = collection.bulk_write(requesting)

requesting = []
collection = db.yelp_businesses
with open(r"./yelp_academic_dataset_business.json") as f:
    for jsonObj in f:
        if len(requesting) < DOCUMENT_COUNT:
            myDict = json.loads(jsonObj)
            requesting.append(InsertOne(myDict))
        else:
            break

result = collection.bulk_write(requesting)

client.close()

print("done")
