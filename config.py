import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "teamray"

    MONGODB_SETTINGS = {
        'db' : 'test',
        'host':'mongodb://ec2-3-83-96-188.compute-1.amazonaws.com:27017'
    }
