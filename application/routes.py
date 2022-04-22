from os import abort
from application import app,api
from models import yelp_businesses, yelp_reviews
from flask import jsonify, request, Response
from flask_mongoengine import MongoEngine
from flask_restx import Resource

@app.route('/')
def test_check_connect():
        return "<h1> Restaurant Finder <h1>"

# @app.route('/reviews', methods=['GET'])
# def get_reviews():
#     reviews = yelp_reviews.objects().to_json()
#     return Response(reviews, mimetype="application/json", status=200)

# @app.route("/postreview", methods=['POST'])
# def insert_review():
#     if not request.json:
#         abort(400)
#     body = request.get_json()
#     review = yelp_reviews(**body).save()
#     id = review.id
#     return {'id': str(id)}, 200

@api.route('/restaurants/<city_name>')
class GetBusinessesByCity(Resource):
    def get(self,city_name):
        return jsonify(yelp_businesses.objects(city = city_name))

@api.route('/reviews/<r_id>')
class GetReviewsByRestaurantId(Resource):
    def get(self,r_id):
        return jsonify(yelp_reviews.objects(business_id = r_id))