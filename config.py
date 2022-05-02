import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "teamray"

    MONGODB_SETTINGS = {
        'db' : 'testdb',
        'host':'ec2-44-202-81-95.compute-1.amazonaws.com:27017'
    }
