import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "teamray"

    MONGODB_SETTINGS = {
        'db' : 'testdb',
<<<<<<< HEAD
        'host':'ec2-34-238-121-163.compute-1.amazonaws.com:27017'
=======
        'host':'ec2-44-202-81-95.compute-1.amazonaws.com:27017'
>>>>>>> origin/main
    }
