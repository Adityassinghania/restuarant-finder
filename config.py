import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "teamray"

    MONGODB_SETTINGS = {
        'db' : 'test',
        'host':'ec2-18-212-72-140.compute-1.amazonaws.com:27017'
    }