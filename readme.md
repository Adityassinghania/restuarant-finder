set up for MacOS- 
1. install virtual environment : pip3 install virtualenv
2. create virtual environment : python3 -m venv venv
3. activate virtual environment : source venv/bin/activate
4. install dependancies : pip3 install requirements.txt
the above file is created using : pip freeze > requirements.txt

We use MongoEngine library to work with a MongDb backend Databse which is a sharded cluster deployed in AWS
We use the flask-restx library for quick development of APIs
