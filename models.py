import flask
from application import db

class yelp_reviews(db.Document):
    
    review_id =  db.StringField(unique = True, max_length = 22)

    # string, 22 character business id, maps to business in business.json
    business_id = db.StringField(max_length = 22)

    # string, 22 character unique user id, maps to the user in user.json
    user_id =  db.StringField(max_length = 22)

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

class attributes(db.EmbeddedDocument):
    RestaurantsTakeOut  = db.BooleanField()
    BusinessParking  = db.DictField()
    RestaurantsDelivery = db.BooleanField()
    BikeParking = db.BooleanField()
    OutdoorSeating = db.BooleanField()
    ByAppointmentOnly = db.BooleanField()
    RestaurantsPriceRange2 = db.StringField()
    BusinessAcceptsCreditCards = db.BooleanField()
    WiFi = db.BooleanField()
    Caters = db.BooleanField()
    Alcohol = db.BooleanField()
    WheelchairAccessible = db.BooleanField()
    GoodForKids = db.BooleanField()
    HasTV = db.BooleanField()
    CoatCheck = db.BooleanField()
    RestaurantsReservations = db.BooleanField()
    HappyHour = db.BooleanField()
    Ambience = db.BooleanField()
    DogsAllowed = db.BooleanField()
    RestaurantsTableService = db.BooleanField()
    DriveThru = db.BooleanField()
    RestaurantsGoodForGroups = db.BooleanField()
    RestaurantsAttire = db.BooleanField()
    NoiseLevel = db.BooleanField()
    GoodForMeal = db.BooleanField()
    BusinessAcceptsBitcoin = db.BooleanField()
    Smoking = db.BooleanField()
    Music = db.BooleanField()
    GoodForDancing = db.BooleanField()
    BestNights = db.BooleanField()
    BYOB = db.BooleanField()
    Corkage = db.BooleanField()
    BYOBCorkage = db.BooleanField()
    AcceptsInsurance = db.BooleanField()
    RestaurantsCounterService = db.BooleanField()
    Open24Hours = db.BooleanField()
    AgesAllowed = db.BooleanField()
    DietaryRestrictions = db.BooleanField()
    HairSpecializesIn = db.BooleanField()

class yelp_businesses(db.Document):
    # // string, 22 character unique string business id
    business_id = db.StringField(unique= True, max_length = 22)

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
    is_open  = db.IntField()

    # // object, business attributes to values. note = some attribute values might be objects
    attributes  = db.EmbeddedDocumentField(attributes)

    # // an array of strings of business categories
    categories  = db.ListField(db.StringField(), default=["Restaurants"])

    # // an object of key day to value hours, hours are using a 24hr clock
    hours  = db.DictField()

class yelp_users(db.Document):
    # // string, 22 character unique user id, maps to the user in user.json
    user_id = db.StringField(unique = True, max_length = 22)
    # // string, the user's first name
    name = db.StringField()
    # // integer, the number of reviews they've written
    review_count = db.IntField()
    # // string, when the user joined Yelp, formatted like YYYY-MM-DD
    yelping_since = db.StringField()
    # // array of strings, an array of the user's friend as user_ids
    friends = db.StringField()
    # // integer, number of useful votes sent by the user
    useful = db.IntField(default=0)
    # // integer, number of funny votes sent by the user
    funny = db.IntField(default=0)
    # // integer, number of cool votes sent by the user
    cool = db.IntField(default=0)
    # // integer, number of fans the user has
    fans = db.IntField(default=0)
    # // array of integers, the years the user was elite
    elite = db.StringField()
    # // float, average rating of all reviews
    average_stars = db.FloatField(default=0)
    # // integer, number of hot compliments received by the user
    compliment_hot = db.IntField(default=0)
    # // integer, number of more compliments received by the user
    compliment_more = db.IntField(default=0)
    # // integer, number of profile compliments received by the user
    compliment_profile = db.IntField(default=0)
    # // integer, number of cute compliments received by the user
    compliment_cute = db.IntField(default=0)
    # // integer, number of list compliments received by the user
    compliment_list = db.IntField(default=0)
    # // integer, number of note compliments received by the user
    compliment_note = db.IntField(default=0)
    # // integer, number of plain compliments received by the user
    compliment_plain = db.IntField(default=0)
    # // integer, number of cool compliments received by the user
    compliment_cool = db.IntField(default=0)
    # // integer, number of funny compliments received by the user
    compliment_funny = db.IntField(default=0)
    # // integer, number of writer compliments received by the user
    compliment_writer = db.IntField()
    # // integer, number of photo compliments received by the user
    compliment_photos = db.IntField()

class yelp_checkins(db.Document):
    # // string, 22 character business id, maps to business in business.json
    business_id = db.StringField(unique= True, max_length = 22)

    # // string which is a comma-separated list of timestamps for each checkin, each with format YYYY-MM-DD HH:MM:SS
    date = db.StringField()