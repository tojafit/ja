from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_URI']= 'mongodb://toja:fit@ds157740.mlab.com:57740/tojafit'
app.config['MONGO_DBNAME']= 'tojafit'

mongo = PyMongo(app)
