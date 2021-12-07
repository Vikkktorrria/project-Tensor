from datetime import datetime, timedelta

from flask import jsonify, make_response, request
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import uuid, jwt

from application import app, db
from application.models.user_model import User, user_schema
from application.models.passport_model import Passport
from application.models.snils_model import Snils
from application.models.patient_model import Patient


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