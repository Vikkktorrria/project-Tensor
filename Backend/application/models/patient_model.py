from datetime import datetime
from application import db, ma

# класс таблицы Patient
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anamnesis = db.Column(db.Text(500))
    created_on = db.Column(db.DateTime(), default=datetime.now)
    updated_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)
    # связи
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    note = db.relationship('Note', backref='patient')

    def __init__(self, anamnesis, user_id):
        self.anamnesis = anamnesis
        self.user_id = user_id


# класс для работы с полями в таблице Patient
class PatientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'anamnesis', 'created_on', 'updated_on')


# объекты для отправки и приёмов запросов
patient_schema = PatientSchema()
patient_schema = PatientSchema(many=True)