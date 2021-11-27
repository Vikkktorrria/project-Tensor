from flask import Flask, json, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from functools import wraps
import uuid, jwt

app = Flask(__name__)
CORS(app)  # убираем ошибку CORS

# подключение к MySQL
app.config['SECRET_KEY'] = 'MEDCARD'  # для кодирования информации
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/medcard_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from app import models, routes
