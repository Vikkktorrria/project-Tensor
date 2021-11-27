from flask import Flask, json, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from functools import wraps
import uuid, jwt

from app import app, db
from app.models import User, Passport, user_schema, passport_schema


# декоратор для проверки токена авторизации
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            token = token.split(" ")[1]

        
        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

# пример получения информации об авторизированном пользователе
@app.route('/api/user/info', methods = ['GET']) 
@token_required
def get_one_user(current_user):
    result = user_schema.dump(current_user)
    return jsonify(result)


@app.route('/api/user/change/mail', methods = ['PUT'])
@token_required
def change_mail(current_user):
    return ''


@app.route('/api/user/change/password', methods = ['PUT'])
@token_required
def change_password(current_user):
    return ''


@app.route('/api/user/passport', methods = ['POST'])
@token_required
def add_passport(current_user):
    series = request.json['passportSeries']
    number = request.json['passportNumber']
    user_id = current_user.id

    #added_passport = Passport.query.filter_by(user_id = user_id).first()
    #if added_passport:
    #    return make_response('Passport is already added', 409, {'message':'К вашей учётной записи уже добавлен паспорт!'})

    passport = Passport(number, series, user_id)
    db.session.add(passport)
    db.session.commit()

    return make_response('Passport succesfully added', 200)

# регистрация пользователя
@app.route('/api/auth/registration', methods = ['POST'])
def register():
    public_id = str(uuid.uuid4())
    name = request.json['name']
    surname = request.json['lastName']
    patronymic = request.json['patronymic']
    b_date = request.json['birthday']
    mail = request.json['email']
    password = generate_password_hash(request.json['password'], method ='sha256')
    phone_number = request.json['phone']
    avatar_img = None

    # обработка ошибки существующей почты, номера телефона
    added_user = User.query.filter_by(mail=mail).first()
    if added_user:
        return make_response('Registration failed', 409, {'message':'Пользователь с такой почтой уже существует!'})

    added_user = User.query.filter_by(phone_number=phone_number).first()
    if added_user:
        return make_response('Registration failed', 409, {'message':'Данный номер телефона уже привязан к другой учетной записи!'})

    user = User(public_id, name, surname, patronymic, b_date, mail, password, phone_number, avatar_img)
    db.session.add(user)
    db.session.commit()
    return make_response('User successful registered', 200)

# авторизация пользователя
@app.route('/api/auth/auth')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'message':'Login required!'})

    user = User.query.filter_by(mail=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'message':'Login required!'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp' : datetime.now()+timedelta(minutes=120)}, app.config['SECRET_KEY'])

        result = user_schema.dump(user)

        return jsonify({'token': token.decode('UTF-8'), 'user': result})
    
    return make_response('Could not verify', 401, {'message':'Login required!'})