from datetime import datetime
from application import db, ma

# класс таблицы Doctor
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qualification = db.Column(db.String(45), nullable=False)  # нужно ли ограничение по символам?
    experience = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now)
    updated_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)
    # связи
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    note = db.relationship('Note', backref='doctor')

    def __init__(self, qualification, experience):
        self.qualification = qualification
        self.experience = experience


# класс для работы с полями в таблице Doctor
class DoctorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'qualification', 'experience', 'created_on', 'updated_on')


# объекты для отправки и приёмов запросов
doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)