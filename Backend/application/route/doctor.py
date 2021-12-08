from flask import jsonify, make_response

from application import app, db
from application.models.user_model import User, user_schema
from application.models.doctor_model import Doctor, doctors_schema, doctor_schema
from application.models.snils_model import Snils
from application.models.passport_model import Passport
from application.models.patient_model import Patient
from application.route.auth import token_required

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