from os import abort
from Extras.helpers import generate_22char_uuid
from application import app,api
from models import yelp_businesses, yelp_reviews
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
