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
UPLOAD_FOLDER = './app/upload'
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
    mimetype_reverse = filename[::-1].partition('.')[0]  # определяем тип
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
    passport = Passport.query.filter_by(user_id=current_user.id).first()
    snils = Snils.query.filter_by(user_id=current_user.id).first()
    patient = Patient.query.filter_by(user_id=current_user.id).first()

    if not passport:
        passport = Passport(None, None, None)

    if not snils:
        snils = Snils(None, None)

    if not patient:
        patient = Patient(None, None)

    return jsonify(
        {'user': result, 'passport': {'series': passport.series, 'number': passport.number}, 'snils': snils.number,
         'anamnesis': patient.anamnesis})


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


# диагнозы пользователя
@app.route('/api/user/diagnoses', methods=['GET'])
@token_required
def get_diagnoses(current_user):
    patient = Patient.query.filter_by(user_id=current_user.id).first()
    all = Note.query.filter_by(user_id=patient.user_id).all()
    results = notes_schema.dump(all)
    for val in results:
        current_doctor = Doctor.query.filter_by(id=val['doctor_id']).first()
        doctor = User.query.filter_by(id=current_doctor.user_id).first()
        val['doctor'] = {'name': doctor.name, 'surname': doctor.surname, 'patronymic': doctor.patronymic}
    return jsonify(results)


# все диагнозы
@app.route('/api/diagnoses', methods=['GET'])
@token_required
def get_unsigned_diagnoses(current_user):
    all = Note.query.all()
    results = unsigned_notes_schema.dump(all)
    for val in results:
        current_doctor = Doctor.query.filter_by(id=val['doctor_id']).first()
        doctor = User.query.filter_by(id=current_doctor.user_id).first()
        val['doctor'] = {'name': doctor.name, 'surname': doctor.surname, 'patronymic': doctor.patronymic}
    return jsonify(results)


# получить список докторов
@app.route('/api/doctors/all', methods=['GET'])
@token_required
def get_doctors(current_user):
    all = Doctor.query.all()
    results = doctors_schema.dump(all)
    for val in results:
        current_doctor = Doctor.query.filter_by(id=val['id']).first()
        doctor = User.query.filter_by(id=current_doctor.user_id).first()
        val['fullName'] = {'name': doctor.name, 'surname': doctor.surname, 'patronymic': doctor.patronymic}
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
        return make_response('Registration failed', 409,
                             {'message': 'Данный номер телефона уже привязан к другой учетной записи!'})

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
        passport = Passport.query.filter_by(user_id=user.id).first()
        snils = Snils.query.filter_by(user_id=user.id).first()
        patient = Patient.query.filter_by(user_id=user.id).first()

        if not passport:
            passport = Passport(None, None, None)

        if not snils:
            snils = Snils(None, None)

        if not patient:
            patient = Patient(None, None)

        return jsonify({'token': token.decode('UTF-8'),
                        'user': {'user': result, 'passport': {'series': passport.series, 'number': passport.number},
                                 'snils': snils.number, 'anamnesis': patient.anamnesis}})

    return make_response('Could not verify', 401, {'message': 'Login required!'})


# добавление статьи
@app.route('/api/user/article', methods=['POST'])
@token_required
def add_article(current_user):
    title = request.json['title']
    text = request.json['text']
    article_img = request.json['article_img']
    user_id = current_user.id

    if not current_user.is_doctor:
        return make_response('Статья успешно не добавлена', 403)

    article = Article(text, article_img, title, user_id)
    db.session.add(article)
    db.session.commit()

    return make_response('Статья успешно добавлена', 200)


# редиактирование статьи
@app.route('/api/user/change/article/<article_id>', methods=['PUT'])
@token_required
def change_article(current_user, article_id):
    new_title = request.json['title']
    new_text = request.json['text']
    new_article_img = request.json['article_img']
    current_article = Article.query.filter_by(id=article_id).first()
    user_id = current_article.user_id

    if not current_user.is_doctor:
        return make_response('Вы не можете редактировать статью', 403)

    if current_user.id != user_id:
        return make_response('Вы не можете редактировать статью', 403)

    current_article.title = new_title
    current_article.text = new_text
    current_article.article_img = new_article_img
    db.session.commit()

    return make_response('Статья успешно отредактирована', 200)


# удаление статьи
@app.route('/api/user/delete/article/<article_id>', methods=['DELETE'])
@token_required
def delete_article(current_user, article_id):
    current_article = Article.query.filter_by(id=article_id).first()
    user_id = current_article.user_id

    if not current_user.is_doctor:
        return make_response('Вы не можете удалить статью', 403)

    if current_user.id != user_id:
        return make_response('Вы не можете удалить статью', 403)

    db.session.delete(current_article)
    db.session.commit()

    return make_response('Статья успешно удалена', 200)

# добавление записи
@app.route('/api/user/patient/note', methods=['POST'])
@token_required
def add_note(current_user):
    date_of_visit = request.json['date_of_visit']
    user_id = current_user.id
    doctor_id = request.json['doctor_id']

    if current_user.is_doctor:
        return make_response('Запись не добавлена', 403)

    note = Note(date_of_visit, user_id, doctor_id)
    db.session.add(note)
    db.session.commit()

    return make_response('Запись успешно добавлена', 200)


# удаление записи
@app.route('/api/user/patient/delete/note/<note_id>', methods=['DELETE'])
@token_required
def delete_note(current_user, note_id):
    current_note = Note.query.filter_by(id=note_id).first()
    user_id = current_note.user_id

    if current_user.id != user_id:
        return make_response('Вы не можете удалить запись', 403)

    db.session.delete(current_note)
    db.session.commit()

    return make_response('Запись успешно удалена', 200)


# удаление записи для доктора
@app.route('/api/user/doctor/delete/note/<note_id>', methods=['DELETE'])
@token_required
def delete_note_by_doctor(current_user, note_id):
    if not current_user.is_doctor:
        return make_response('Вы не можете удалить запись', 403)

    current_note = Note.query.filter_by(id=note_id).first()
    doctor_id = current_note.doctor_id
    current_doctor = Doctor.query.filter_by(id=doctor_id).first()


    if current_doctor.id != doctor_id:
        return make_response('Вы не можете удалить запись', 403)

    db.session.delete(current_note)
    db.session.commit()

    return make_response('Запись успешно удалена', 200)

# получение информации о докторе
@app.route('/api/user/doctor/info', methods=['GET'])
@token_required
def get_one_doctor(current_user):
    if not current_user.is_doctor:
        return make_response('Этот пользователь не доктор', 403)

    current_doctor = Doctor.query.filter_by(user_id=current_user.id).first()
    user = User.query.filter_by(id=current_doctor.user_id).first()

    result = doctor_schema.dump(current_doctor)
    result['fullName'] = {'name': user.name, 'surname': user.surname, 'patronymic': user.patronymic}
    
    return jsonify(result)


# получение записей (для доктора)
@app.route('/api/user/doctor/note', methods=['GET'])
@token_required
def get_note_doctor(current_user):
    if not current_user.is_doctor:
        return make_response('Этот пользователь не доктор', 403)

    current_doctor = Doctor.query.filter_by(user_id=current_user.id).first()
    doctors_notes = Note.query.filter_by(doctor_id=current_doctor.id).all()

    results = notes_schema.dump(doctors_notes)
    for val in results:
        patient = User.query.filter_by(id=val['user_id']).first()
        val['patient'] = {'name': patient.name, 'surname': patient.surname, 'patronymic': patient.patronymic}
    return jsonify(results)


@app.route('/api/user/doctor/note/<note_id>', methods=['GET'])
@token_required
def get_one_note_doctor(current_user, note_id):
    if not current_user.is_doctor:
        return make_response('Этот пользователь не доктор', 403)

    current_doctor = Doctor.query.filter_by(user_id=current_user.id).first()
    doctors_note = Note.query.filter_by(id=note_id).first()

    if current_doctor.id != doctors_note.doctor_id:
        return make_response('Ошибка доступа. Это не ваша запись.', 403)

    result = note_schema.dump(doctors_note)
    patient = User.query.filter_by(id=result['user_id']).first()
    result['patient'] = {'name': patient.name, 'surname': patient.surname, 'patronymic': patient.patronymic}
    return jsonify(result)


# редактирование записи (для доктора)
@app.route('/api/user/doctor/change/note/<note_id>', methods=['PUT'])
@token_required
def change_note_doctor(current_user, note_id):
    if not current_user.is_doctor:
        return make_response('Этот пользователь не доктор', 403)

    current_doctor = Doctor.query.filter_by(user_id=current_user.id).first()
    current_note = Note.query.filter_by(id=note_id).first()

    if current_note.doctor_id != current_doctor.id:
        return make_response('Вы не можете редактировать статью', 403)

    new_recipe = request.json['recipe']
    new_diagnosis = request.json['diagnosis']
    # new_date_of_visit = request.json['date_of_visit']

    current_note.recipe = new_recipe
    current_note.diagnosis = new_diagnosis
    # current_note.date_of_visit = new_date_of_visit
    db.session.commit()

    return make_response('Запись успешно отредактирована', 200)

#получить доктору информацию о пациенте
@app.route('/api/doctor/getuserinfo/<user_id>', methods=['GET'])
@token_required
def watch_user_by_doctor(current_user, user_id):
    if not current_user.is_doctor:
        return make_response('Недостаточно прав', 403)

    user = User.query.filter_by(id=user_id).first()

    if not user:
        return make_response('Пользователь не найден!', 404)

    result = user_schema.dump(user)
    passport = Passport.query.filter_by(user_id=user.id).first()
    snils = Snils.query.filter_by(user_id=user.id).first()
    patient = Patient.query.filter_by(user_id=user.id).first()

    if not passport:
        passport = Passport(None, None, None)

    if not snils:
        snils = Snils(None, None)

    if not patient:
        return make_response('Указанный пользователь не является пациентом!', 404)

    return jsonify(
        {'user': result, 'passport': {'series': passport.series, 'number': passport.number}, 'snils': snils.number,
         'anamnesis': patient.anamnesis})