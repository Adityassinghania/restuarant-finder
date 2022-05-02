from os import abort
from Extras.helpers import generate_22char_uuid
from application import api
from models import yelp_businesses, yelp_reviews, yelp_checkins, yelp_users
from flask import jsonify, request, Response
from flask_mongoengine import MongoEngine
from flask_restx import Resource
from datetime import datetime

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

@api.route('/del_review/')
class DeleteReview(Resource):
    def delete():
        data = api.payload
        review = yelp_reviews.objects(review_id = data["review_id"])
        if(review["user_Id"] == data["token"]):
            res = yelp_reviews.delete(review)
        else:
            res = "invalid token"
        return jsonify(res) 

# NEEDS FIXING
@api.route('/del_short_reviews/<word_count>')
class DeleteShortReviews(Resource):
    # use get call, add reviews to a list that don't meet a minimum, and then remove them
    # look for reviews that don't exceed a character count
    def delete(self, char_count):
        review_objs = yelp_reviews.objects(review_id = char_count)
        delete_count = 0
        deleted_reviews = []
        deleted_reviews.append(review_objs)
        yelp_reviews.delete(review_objs)

        # for review in review_objs:
        #     text = review["text"]
        #     if len(text) < char_count:
        #         delete_count += 1
        #         deleted_reviews.append(review)
        #         review.delete()
            
        #     if delete_count == 100:
        #         break

        # print('deleted', delete_count, 'short reviews')
        return jsonify(deleted_reviews)

@api.route('/user_trust/<rev_count>')
class UpdateUserTrustRating(Resource):
    def put(self,rev_count):
        review_threshold = int(rev_count)
        # get user with review count greater than equal to threshold
        user_objs = yelp_users.objects(review_count__gte = review_threshold)
        year = datetime.now().year
        # upadte yearn in their elite field
        for user in user_objs:
                if int(year) not in user["elite"]:
                    user["elite"].append(int(year))
        res = user.save()
        return jsonify(res)

@api.route('/user_useful_rev/<b_id>')
class GetUsersWithMaxUsefulReviews(Resource):
    def get(self,b_id):
        # get reviews for a specific business
        rev_objs = yelp_reviews.objects(business_id=b_id).order_by("useful")
        number_of_reviews = len(rev_objs) if len(rev_objs) < 10 else 10
        # get top 10 most useful reviews
        review_users = [rev_objs[i]["user_id"] for i in range(number_of_reviews)]

        # get users that reviewed that business
        user_objs = yelp_users.objects(user_id__in = review_users)

        return jsonify(user_objs)


@api.route('/restaurants_user_match/<user_input>')
class GetRestaurantsBasedOnUserInput(Resource):
    # fetch all reviews of restaurant and do substring match and substring comes from url. pass as a query param
    def get(self,user_input):
        business_objs = yelp_businesses.objects()
        restaurants = []
        for restaurant in business_objs:
            # check if user input in the restaurant name
            if user_input.casefold() in restaurant["name"].casefold():
                restaurants.append(restaurant)
            
            # # if not, check if the input is a certain category
            # else:
            #     for i in restaurant["categories"]:
            #         if user_input in i:
            #             restaurants.append(restaurant)
            #             break
    
        return jsonify(restaurants)
    
# NEEDS FIXING
@api.route('/insert_restaurant')
class InsertNewRestaurant(Resource):
    def post(self):
        data = api.payload
        data["business_id"] = generate_22char_uuid()
        business = yelp_businesses(**data)
        res = business.save()
        return jsonify(res)

@api.route('/edit_review')
class UpdateRestaurantReview(Resource):
    def put(self, review_id):
        data = api.payload
        review_obj = yelp_reviews.objects(review_id = data["review_id"])
        if review_obj["user_id"] == data["token"]:
            review_obj["text"] = data["text"]
            res = yelp_reviews.save(review_obj)
        else:
            res = "invalid review or invalid token"

        return jsonify(res)

@api.route('/add_checkin/<b_id>')
class AddCheckIn(Resource):
    def put(self,b_id):
        data = api.payload
        checkin_ob = yelp_checkins.objects(business_id = b_id)
        checkin_ob["date"] += datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        res = yelp_checkins.save(checkin_ob)
        return jsonify(res)
