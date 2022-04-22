import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "teamray"

    MONGODB_SETTINGS = {
        'db' : 'test',
        'host':'ec2-44-203-201-144.compute-1.amazonaws.com:27017'
    }
