import pymongo
import json
from pymongo import MongoClient, InsertOne

# MONGOS server client
client = pymongo.MongoClient("mongodb://ec2-18-205-105-6.compute-1.amazonaws.com:27017")
db = client.test

# loading RESTAURANTS
requesting = []
collection = db.yelp_businesses
with open(r"./dataset/yelp_academic_dataset_business.json") as biz_file:
    for jsonObj in biz_file:
        myDict = json.loads(jsonObj)
        categories = myDict['categories']
            
        # only append if it's a restaurant
        if "Restaurants" in categories or "Food" in categories:
            requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)

# load REVIEWS
requesting = []
collection = db.yelp_reviews
with open(r"./dataset/yelp_academic_dataset_review.json") as rev_file:
    for jsonObj in rev_file:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)

# load USERS
requesting = []
collection = db.yelp_users
with open(r"./dataset/yelp_academic_dataset_user.json") as usr_file:
    for jsonObj in usr_file:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)

# load CHECKIN
requesting = []
collection = db.yelp_checkins
with open(r"./dataset/yelp_academic_dataset_checkin.json") as check_file:
    for jsonObj in check_file:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)

client.close()
print("done loading")
