from flask import request, jsonify, make_response

from application import app, db
from application.models.user_model import User
from application.models.note_model import Note, notes_schema, note_schema, unsigned_notes_schema
from application.models.doctor_model import Doctor
from application.models.patient_model import Patient
from application.route.auth import token_required

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
        user_patient = User.query.filter_by(id=val['user_id']).first()
        patient = Patient.query.filter_by(user_id=val['user_id']).first()
        val['patient'] = {'name': user_patient.name, 'surname': user_patient.surname, 'patronymic': user_patient.patronymic, 'anamnesis': patient.anamnesis}
    return jsonify(results)


# получить 1 запись (для доктора)
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


#получить записи доктора для пациента
@app.route('/api/user/notes/doctor/<doctor_id>', methods=['GET'])
@token_required
def get_doctors_noted(doctor_id):
    notes = Note.query.filter_by(doctor_id = doctor_id).all()
    result = notes_schema.dump(notes)
    return jsonify(result)