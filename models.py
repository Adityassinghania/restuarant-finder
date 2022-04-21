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


class yelp_business(db.Document):
    # // string, 22 character unique string business id
    business_id = db.StringField(max_length = 22)

    # // string, the business's name
    name = db.StringField()

    # // string, the full address of the business
    address = db.StringField()

    # // string, the city
    city = db.StringField()

    # // string, 2 character state code, if applicable
    state = db.StringField(max_length=2)

    # // string, the postal code
    postal_code = db.StringField(max_length=5)

    # // float, latitude
    latitude = db.FloatField()

    # // float, longitude
    longitude  = db.FloatField()

    # // float, star rating, rounded to half-stars
    stars  = db.FloatField()

    # // integer, number of reviews
    review_count  = db.IntField()

    # // integer, 0 or 1 for closed or open, respectively
    is_open  = db.IntFiled()

    # // object, business attributes to values. note = some attribute values might be objects
    attributes  = db.EmbeddedDocumentField(attributes)

    # // an array of strings of business categories
    categories  = db.ListField(db.StringField(), default=["Restaurants"])

    # // an object of key day to value hours, hours are using a 24hr clock
    hours  = db.DictField()

class attributes(db.EmbeddedDocument):
    RestaurantsTakeOut  = db.BooleanField()
    BusinessParking  = db.DictField()