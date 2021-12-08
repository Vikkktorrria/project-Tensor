from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # убираем ошибку CORS

app.config['UPLOAD_FOLDER'] = 'C:/Users/mauta/Desktop/project-Tensor-main/Backend/upload'
app.config['SECRET_KEY'] = 'MEDCARD'  # для кодирования информации
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/medcard_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from application import models, route