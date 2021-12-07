from datetime import datetime
from application import db, ma


# класс таблицы Note
class Note(db.Model):
    # __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    recipe = db.Column(db.Text(500))
    diagnosis = db.Column(db.Text(500))
    date_of_visit = db.Column(db.DateTime())
    created_on = db.Column(db.DateTime(), default=datetime.now)
    updated_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)
    # связи
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    doctor_id = db.Column(db.Integer(), db.ForeignKey('doctor.id'))
    patient_id = db.Column(db.Integer(), db.ForeignKey('patient.id'))

    def __init__(self, date_of_visit, user_id, doctor_id):
        self.date_of_visit = date_of_visit
        self.user_id = user_id
        self.doctor_id = doctor_id


# класс для работы с полями в таблице Notes
class NoteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_of_visit', 'diagnosis', 'recipe', 'doctor_id', 'user_id')


class UnsignedNoteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_of_visit', 'doctor_id', 'user_id')


# объекты для отправки и приёмов запросов
note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)
unsigned_notes_schema = UnsignedNoteSchema(many=True)