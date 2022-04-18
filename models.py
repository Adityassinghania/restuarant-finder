import flask
from application import db

class yelp_reviews(db.Document):
    
    review_id =  db.StringField(unique = True, max_length = 22)

    # string, 22 character unique user id, maps to the user in user.json
    user_id =  db.StringField(unique = True, max_length = 22)
    # string, 22 character business id, maps to business in business.json
    business_id = db.StringField(max_length = 22)

    # // integer, star rating
    stars =  db.IntField(default=0, max_value = 5)

    # // string, date formatted YYYY-MM-DD
    date = db.StringField()

    # // string, the review itself
    text = db.StringField()
    # // integer, number of useful votes received
    useful = db.IntField(default=0)

    # // integer, number of funny votes received
    funny = db.IntField(default=0)

    # // integer, number of cool votes received
    cool =db.IntField(default=0)