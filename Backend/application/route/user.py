import os

from flask import Response, request, make_response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from application import app, db
from application.models.user_model import User, user_schema
from application.models.passport_model import Passport
from application.models.snils_model import Snils
from application.models.patient_model import Patient
from application.models.note_model import Note, notes_schema
from application.models.doctor_model import Doctor
from application.route.auth import token_required

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