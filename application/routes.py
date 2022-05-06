from os import abort
import re
from Extras.helpers import generate_22char_uuid
from application import api
from models import yelp_businesses, yelp_reviews, yelp_users, yelp_checkins
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


@api.route('/del_short_reviews/<char_count>')
class DeleteShortReviews(Resource):
    # this works, but it takes awhile
    def delete(self, char_count):
        pattern = '^[a-zA-Z]{1,' + char_count + '}'
        review_objs = yelp_reviews.objects(text__regex = re.compile(pattern))
        deleted = 0
        for rev in review_objs:
            deleted += 1
            rev.delete()
        res = review_objs
        
        if deleted == 0:
            res = "No reviews found to delete!"
        return jsonify(res)

@api.route('/user_trust/<rev_count>')
class UpdateUserTrustRating(Resource):
    def put(self,rev_count):
        review_threshold = int(rev_count)
        # get user with review count greater than equal to threshold
        user_objs = yelp_users.objects(review_count__gte = review_threshold)
        year = datetime.now().year
        # update year in user
        for user in user_objs:
            # i had to change "elite" to just String type, ListField(stringfield) wasn't working for some reason
            # same for other attributes previously that were ListFields
            if str(year) not in user["elite"]:
                user["elite"] += ', ' + str(year)
                user.save()
        res = user_objs
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

@api.route('/restaurants_user_match/<city_name>/<user_input>')
class GetRestaurantsBasedOnUserInput(Resource):
    # fetch all reviews of restaurant and do substring match and substring comes from url. pass as a query param
    def get(self,city_name,user_input):
        # look for businesses in city
        business_objs = yelp_businesses.objects(city = city_name)
        # get list of business ids
        restaurants = [business["business_id"] for business in business_objs]
        # get reviews where business id is in restaurants array and user input is in a review
        reviews = yelp_reviews.objects(business_id__in = restaurants, text__icontains = user_input)
        return jsonify(reviews)
    
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
    def put(self):
        data = api.payload
        review_obj = yelp_reviews.objects(review_id = data["review_id"])
        if review_obj[0]["user_id"] == data["token"]:
            for rev in review_obj:
                rev["text"] = data["text"]
                res = rev.save()
        else:
            res = "invalid review or invalid token"

        return jsonify(res)

@api.route('/delete_review')
class UpdateRestaurantReview(Resource):
    def put(self):
        data = api.payload
        review_obj = yelp_reviews.objects(review_id = data["review_id"])
        if review_obj[0]["user_id"] == data["token"]:
            for rev in review_obj:
                rev["text"] = data["text"]
                res = rev.delete()
        else:
            res = "invalid review or invalid token"

        return jsonify(res)

@api.route('/add_checkin/<b_id>')
class AddCheckIn(Resource):
    def put(self,b_id):
        checkin_obj = yelp_checkins.objects(business_id = b_id)
        for checkin in checkin_obj:
            checkin["date"] += ', ' + datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            res = checkin.save()

        return jsonify(res)

@api.route('/restaurants_sorted/<city_name>/')
class SortRestaurantsByReviewCount(Resource):
    def get(self, city_name):
        business_objs = yelp_businesses.objects(city = city_name)
        return jsonify(business_objs.order_by('-review_count'))
        
# sort_key = "useful" | "funny" | "cool"
@api.route('/reviews_sorted/<r_id>/<sort_key>')
class SortReviews(Resource):
    def get(self, r_id, sort_key):
        review_objs = yelp_reviews.objects(business_id = r_id).order_by('-' + sort_key)
        return jsonify(review_objs)

@api.route('/review_useful/<r_id>')
class IncrementReviewUseful(Resource):
    def put(self, r_id):
        review_obj = yelp_reviews.objects(review_id = r_id).first()
        review_obj["useful"] += 1
        res = review_obj.save(review_obj)
        return jsonify(res)

@api.route('/restaurants_by_category/<category>')
class RestaurantsByCategory(Resource):
    def get(self, category):
        business_objs = yelp_businesses.objects(categories__icontains = category)
        return jsonify(business_objs)