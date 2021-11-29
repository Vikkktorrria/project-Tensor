from flask import Flask, json, send_file, jsonify, request, make_response, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from functools import wraps
from urllib.request import urlopen
import uuid, jwt
import os

from app import app, db
from app.models import *

# проверить директорию
UPLOAD_FOLDER = 'C:/Users/mauta/Desktop/project-Tensor-main/Backend/app/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# декоратор для проверки токена авторизации
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            token = token.split(" ")[1]

        if not token:
            return jsonify({'message': 'Ошибка авторизации'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Ошибка авторизации'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


# получить img
@app.route('/user/image/<file_name>', methods=['GET'])
def get_img(file_name):
    with open(app.config['UPLOAD_FOLDER'] + '/' + file_name, 'rb') as file:
        binaryData = file.read()
    return Response(binaryData, mimetype='image/jpeg')

# загрузить img
@app.route('/api/user/upload/avatar', methods=['PUT'])
@token_required
def upload_image(current_user):
    img = request.files['file']
    if not img:
        return make_response("Фото не загружено!", 400)

    filename = img.filename
    mimetype_reverse = filename[::-1].partition('.')[0] # определяем тип
    mimetype = '.' + mimetype_reverse[::-1]

    filename = 'avatar-' + str(current_user.id) + mimetype

    img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    current_user.avatar_img = filename
    db.session.commit()
    return make_response("Файл загружен", 200)

# получение информации об авторизированном пользователе
@app.route('/api/user/info', methods=['GET'])
@token_required
def get_one_user(current_user):
    result = user_schema.dump(current_user)
    passport = Passport.query.filter_by(user_id = current_user.id).first()
    snils = Snils.query.filter_by(user_id = current_user.id).first()
    patient = Patient.query.filter_by(user_id = current_user.id).first()

    if not passport:
        passport = Passport(None, None, None)
    
    if not snils:
        snils = Snils(None, None)

    if not patient:
        patient = Patient(None, None)

    return jsonify({'user': result, 'passport': {'series': passport.series, 'number':passport.number}, 'snils': snils.number, 'anamnesis': patient.anamnesis})


# смена email
@app.route('/api/user/change/email', methods=['PUT'])
@token_required
def change_mail(current_user):
    new_email = request.json['email']

    current_user.mail = new_email
    db.session.commit()

    return make_response('Адрес электронной почты успешно изменен', 200)


# смена пароля
@app.route('/api/user/change/password', methods=['PUT'])
@token_required
def change_password(current_user):
    old_password = request.json['passwordOld']
    new_password = generate_password_hash(request.json['password'], method='sha256')

    if not check_password_hash(current_user.password, old_password):
        return make_response('Старый пароль введён неверно', 400)

    current_user.password = new_password
    db.session.commit()

    return make_response('Пароль успено изменён', 200)


@app.route('/api/news', methods=['GET'])
def get_articles():
    all = Article.query.all()
    results = articles_schema.dump(all)
    return jsonify(results)


@app.route('/api/user/diagnoses', methods=['GET'])
@token_required
def get_diagnoses(current_user):
    patient = Patient.query.filter_by(user_id = current_user.id).first()
    all = Note.query.filter_by(patient_id = patient.id).all()
    results = notes_schema.dump(all)
    for val in results:
        current_doctor = Doctor.query.filter_by(id = val['doctor_id']).first()
        doctor = User.query.filter_by(id = current_doctor.user_id).first()
        val['doctor'] = {'name': doctor.name, 'surname':doctor.surname, 'patronymic':doctor.patronymic}
    return jsonify(results)

# добавление анамнеза
@app.route('/api/user/anamnesis', methods=['POST'])
@token_required
def add_anamnesis(current_user):
    anamnesis = request.json['anamnesis']
    user_id = current_user.id

    added_patient = Patient.query.filter_by(user_id=user_id).first()
    if added_patient:
        return edit_anamnesis()

    patient = Patient(anamnesis, user_id)
    db.session.add(patient)
    db.session.commit()

    return make_response('Анамнез успешно добавлен', 200)

@token_required
def edit_anamnesis(current_user):
    anamnesis = request.json['anamnesis']
    user_id = current_user.id

    patient = Patient.query.filter_by(user_id=user_id).first()
    patient.anamnesis = anamnesis
    db.session.commit()

    return make_response('Анамнез успешно обновлен', 200)

# добавление СНИЛС
@app.route('/api/user/snils', methods=['POST'])
@token_required
def add_snils(current_user):
    number = request.json['snils']
    user_id = current_user.id

    added_snils = Snils.query.filter_by(user_id=user_id).first()
    if added_snils:
        return make_response('К данной учётной записи уже привязан СНИЛС', 409)

    snils = Snils(number, user_id)
    db.session.add(snils)
    db.session.commit()

    return make_response('СНИЛС успешно привязан', 200)


# добавление паспорта
@app.route('/api/user/passport', methods=['POST'])
@token_required
def add_passport(current_user):
    series = request.json['passportSeries']
    number = request.json['passportNumber']
    user_id = current_user.id

    added_passport = Passport.query.filter_by(user_id=user_id).first()
    if added_passport:
        return make_response('К вашей учётной записи уже добавлен паспорт!', 409)

    passport = Passport(number, series, user_id)
    db.session.add(passport)
    db.session.commit()

    return make_response('Passport succesfully added', 200)


# регистрация пользователя
@app.route('/api/auth/registration', methods=['POST'])
def register():
    public_id = str(uuid.uuid4())
    name = request.json['name']
    surname = request.json['lastName']
    patronymic = request.json['patronymic']
    b_date = request.json['birthday']
    mail = request.json['email']
    password = generate_password_hash(request.json['password'], method='sha256')
    phone_number = request.json['phone']
    avatar_img = None

    # обработка ошибки существующей почты, номера телефона
    added_user = User.query.filter_by(mail=mail).first()
    if added_user:
        return make_response('Registration failed', 409, {'message': 'Пользователь с такой почтой уже существует!'})

    added_user = User.query.filter_by(phone_number=phone_number).first()
    if added_user:
        return make_response('Registration failed', 409, {'message': 'Данный номер телефона уже привязан к другой учетной записи!'})

    user = User(public_id, name, surname, patronymic, b_date, mail, password, phone_number, avatar_img)
    db.session.add(user)
    db.session.commit()
    return make_response('User successful registered', 200)


# авторизация пользователя
@app.route('/api/auth/auth')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'message': 'Login required!'})

    user = User.query.filter_by(mail=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'message': 'Login required!'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.now() + timedelta(minutes=120)},
                           app.config['SECRET_KEY'])

        result = user_schema.dump(user)

        return jsonify({'token': token.decode('UTF-8'), 'user': result})

    return make_response('Could not verify', 401, {'message': 'Login required!'})
