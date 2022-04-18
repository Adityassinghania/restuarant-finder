from os import abort
from application import app
from models import yelp_reviews
from flask import request, Response
from flask_mongoengine import MongoEngine

@app.route('/')
def test_check_connect():
        """
        Tests connectivity to the db server. Requires the db server to be
        running.
        """
        client = MongoEngine.connection.get_connection()
        print(str(client))

@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = yelp_reviews.objects().to_json()
    return Response(reviews, mimetype="application/json", status=200)

@app.route("/postreview", methods=['POST'])
def insert_review():
    if not request.json:
        abort(400)
    body = request.get_json()
    review = yelp_reviews(**body).save()
    id = review.id
    return {'id': str(id)}, 200