from flask import Flask
from flask_cors import CORS
# from flask_sock import Sock
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
# sock = Sock(app)
app.json_provider_class.sort_keys = False
CORS(app)

app.config['JWT_SECRET_KEY'] = 'lap4'  
jwt = JWTManager(app)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
# app.config['SQLALCHEMY_ECHO'] = True 


db = SQLAlchemy(app)
