from os import abort
from Extras.helpers import generate_22char_uuid
from application import app,api
from models import yelp_businesses, yelp_reviews, yelp_checkins
from flask import jsonify, request, Response
from flask_mongoengine import MongoEngine
from flask_restx import Resource

@api.route('/')
class Home(Resource):
    def get():
        return "<h1> Restaurant Finder <h1>"

@api.route('/restaurants/<city_name>')
class GetBusinessesByCity(Resource):
    def get(self,city_name):
        return jsonify(yelp_businesses.objects(city = city_name))

@api.route('/restaurant/<r_id>')
class GetBusinessesById(Resource):
    def get(self,r_id):
        return jsonify(yelp_businesses.objects(business_id = r_id))

@api.route('/reviews/<r_id>')
class GetReviewsByRestaurantId(Resource):
    def get(self,r_id):
        return jsonify(yelp_reviews.objects(business_id = r_id))
    
    def post(self,r_id):
        data = api.payload
        data["business_id"] = r_id
        data["review_id"] = generate_22char_uuid()
        data["user_id"] = generate_22char_uuid()
        print(str(data))
        review = yelp_reviews(**data)
        res = review.save()
        return jsonify(res)

@api.route('/del_short_reviews/<char_count>')
class DeleteShortReviews(Resource):
    # use get call, add reviews to a list that don't meet a minimum, and then remove them
    # look for reviews that don't exceed a character count
    def delete(self, char_count):
        review_objs = yelp_reviews.objects()
        shortReviews = []

        for review in review_objs:
            text = review["text"]
            if len(text) < char_count:
                shortReviews.append(review["review_id"])

        for r_id in shortReviews:
            delete_obj = yelp_reviews.objects(review_id = r_id)
            delete_obj.delete()

# note: the trust rating is the 'elite' attribute. add the current year if it hasn't
# been added already
# @api.route('/user_trust/<rev_count>')
# class UpdateUserTrustRating(Resource):
#     def put(self,rev_count):
#         user_objs = yelp_users.objects()
#         users = []

#         for user in user_objs:
#             if user["review_count"] > rev_count:
#                 users.append(user["user_id"])

#         for user in users:
#             # update trust rating
#             print("trust rating updated")

@api.route('/user_useful_rev')
class GetUsersWithMaxUsefulReviews(Resource):
    def get(self):
        user_objs = yelp_users.objects().rder_by('-useful')
        print(user_objs)
        return jsonify(user_objs)


@api.route('/restaurants_user_match/<user_input>')
class GetRestaurantsBasedOnUserInput(Resource):
    # fetch all reviews of restaurant and do substring match and substring comes from url. pass as a query param
    def get(self,userinput):
        business_objs = yelp_businesses.objects()
        restaurants = []
        for restaurant in business_objs:
            # check if user input in the restaurant name
            if userinput in restaurant["name"]:
                restaurants.append(restaurant)
            
            # if not, check if the input is a certain category
            else:
                for i in restaurant["categories"]:
                    if userinput in i:
                        restaurants.append(restaurant["business_id"])
                        break
        
        return jsonify(restaurants)
    

@api.route('/insert_restaurant')
class InsertNewRestaurant(Resource):
    def post(self):
        data = api.payload
        data["business_id"] = generate_22char_uuid()
        print(str(data))

        business = yelp_businesses(**data)
        res = business.save()
        return jsonify(res)

@api.route('/update_review/<review_id>')
class UpdateRestaurantReview(Resource):
    # do a .save and pass a review id. change text but not the id
    def put(self, review_id):
        content = api.payload
        review_obj = yelp_reviews.objects(review_id = review_id)
        review_obj.update(text=content['text'])
        
        review = yelp_reviews(**review_obj)
        res = review.save()
        return jsonify(res)



@api.route('/add_checkin/<business_id>')
class AddCheckIn(Resource):
    def put(self,business_id):
        data = api.payload
        checkin_obj = yelp_checkins.objects(business_id = business_id)
        checkin_dates = checkin_obj["date"]
        checkin_new = checkin_dates + data['date']
        checkin_obj.update(date=checkin_new)

        checkin = yelp_checkins(**checkin_obj)
        res = checkin.save()
        return jsonify(res)
