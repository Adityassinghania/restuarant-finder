import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "teamray"

    MONGODB_SETTINGS = {
        'db' : 'test',
        'host':'ec2-34-239-111-117.compute-1.amazonaws.com:27020'
    }