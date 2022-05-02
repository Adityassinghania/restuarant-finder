from hashlib import new
import pymongo
import json
from pymongo import MongoClient, InsertOne
# connection
try:
    client = pymongo.MongoClient("ec2-44-202-81-95.compute-1.amazonaws.com:27017")
    print("connection successful!")
except:
    print("Could not connect!!")

db = client.test
collection = db.yelp_reviews
business_collection = db.yelp_businesses

# get all reviews for a particular business
def get_reviews():
    reviews = []
    for x in collection.find({"business_id":"SZU9c8V2GuREDN5KgyHFJw"},{}):
        reviews.append(x)
    for r in reviews:
        print(r)

# insert a new review
def insert_review():
    new_review = {"business_id":"SZU9c8V2GuREDN5KgyHFJw", 
    "user_id":"Ha3iJu77CxlrFm-vQRs_8g", "stars":4, "useful":0, 
    "text":"This is one of the most amazing places we have been to!"}

    result = collection.insert_one(new_review)

    if result:
        print("---------------------------------------------inserted new review: "+str(result.inserted_id))
    return result.inserted_id

# update the new review when useful vote is given
def update_review(review_id):
    result = collection.update_one(
            {"_id":review_id},
            {"$inc":{"useful" : 1}}
            )
    print("-------------------------------Update successful: "+str(result))

#delete the review
def delete_review(review_id):
   result =  collection.delete_one({"_id":review_id})
   print(str(result))

if __name__ == '__main__':
# get_reviews()
# review_id = insert_review()
# update_review(review_id)
# get_reviews()
# delete_review(review_id)
# get_reviews()

    result = business_collection.find({"city":"Santa Barbara"},{})
    for x in result:
        print(x)
