import pymongo
import json
from pymongo import MongoClient, InsertOne

# MONGOS server client
client = pymongo.MongoClient("mongodb://ec2-54-210-106-126.compute-1.amazonaws.com:27020")
db = client.test

# loading RESTAURANTS
requesting = []
collection = db.yelp_businesses
no_category = 0
not_restaurant = 0
print('collecting restaurants now...')
with open(r"./dataset/yelp_academic_dataset_business.json") as biz_file:
    i = 0
    for jsonObj in biz_file:
        myDict = json.loads(jsonObj)
        categories = myDict['categories']
            
        # only append if it's a restaurant
        if type(categories) is str and ("Restaurants" in categories or "Food" in categories):
            requesting.append(InsertOne(myDict))
        elif type(categories) is not str:
            no_category += 1
        else:
            not_restaurant += 1

print('loading', i, 'restaurants into db...')
result = collection.bulk_write(requesting)
print('loaded', i, 'restaurants')
print(no_category, 'businesses with no category')
print(not_restaurant, 'non-restaurant businesses')

# load REVIEWS
requesting = []
collection = db.yelp_reviews
print('\ncollecting reviews now...')
with open(r"./dataset/yelp_academic_dataset_review.json") as rev_file:
    i = 0
    for jsonObj in rev_file:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))
        i += 1

print('loading', i, 'reviews into db...')
result = collection.bulk_write(requesting)
print('loaded', i, 'reviews')

# load USERS
requesting = []
collection = db.yelp_users
print('\ncollecting users now...')
with open(r"./dataset/yelp_academic_dataset_user.json") as usr_file:
    i = 0
    for jsonObj in usr_file:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))
        i += 1

print('loading', i, 'users into db...')
result = collection.bulk_write(requesting)
print('loaded', i, 'users')

# load CHECKIN
requesting = []
collection = db.yelp_checkins
print('\ncollecting checkins now...')
with open(r"./dataset/yelp_academic_dataset_checkin.json") as check_file:
    i = 0
    for jsonObj in check_file:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))
        i += 1

print('loading', i, 'checkins into db...')
result = collection.bulk_write(requesting)
print('loaded', i, 'checkins')

client.close()
print("done loading")
