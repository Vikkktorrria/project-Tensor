from datetime import datetime, timedelta
from app import db, ma


# класс таблицы User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    patronymic = db.Column(db.String(45))
    b_date = db.Column(db.Date, nullable=False)
    mail = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(45), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now)  # когда сознадо
    updated_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)  # когда изменено
    avatar_img = db.Column(db.String(200))
    is_doctor = db.Column(db.Boolean, default=False)
    # отношения с другими таблицами
    article = db.relationship('Article', backref='user')
    passport = db.relationship('Passport', backref='user', uselist=False)
    snils = db.relationship('Snils', backref='user', uselist=False)
    note = db.relationship('Note', backref='user', uselist=False)

    def __init__(self, public_id, name, surname, patronymic, b_date, mail, password, phone_number, avatar_img):
        self.public_id = public_id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.b_date = b_date
        self.mail = mail
        self.password = password
        self.phone_number = phone_number
        self.avatar_img = avatar_img


# класс для работы с полями в таблице User
class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'avatar_img', 'name', 'surname', 'patronymic', 'b_date', 'mail', 'phone_number',
            'is_doctor', 'created_on', 'updated_on')


# объекты для отправки и приёмов запросов
user_schema = UserSchema()
users_schema = UserSchema(many=True)


# класс таблицы Article
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text(500), nullable=False)
    article_img = db.Column(db.String(200))
    created_on = db.Column(db.DateTime(), default=datetime.now)  # когда сознадо
    # связи
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, text, article_img, title):
        self.text = text
        self.article_img = article_img
        self.title = title


# класс для работы с полями в таблице Article
class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'text', 'article_img', 'created_on', 'title')


# объекты для отправки и приёмов запросов
article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)


# класс таблицы Passport
class Passport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)  # нужно ли ограничение по символам?
    series = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now)
    # связи
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, number, series, user_id):
        self.number = number
        self.series = series
        self.user_id = user_id


# класс для работы с полями в таблице Passport
class PassportSchema(ma.Schema):
    class Meta:
        fields = ('id', 'number', 'series', 'created_on')


# объекты для отправки и приёмов запросов
passport_schema = PassportSchema()
Passport_schema = PassportSchema(many=True)


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


# класс таблицы Snils
class Snils(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20))
    created_on = db.Column(db.DateTime(), default=datetime.now)
    # связи
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, number, user_id):
        self.number = number
        self.user_id = user_id


# класс для работы с полями в таблице Snils
class SnilsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'number', 'created_on')


# объекты для отправки и приёмов запросов
snils_schema = SnilsSchema()
snils_schema = SnilsSchema(many=True)


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
        fields = ('id', 'date_of_visit', 'diagnosis', 'recipe', 'doctor_id')


class UnsignedNoteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_of_visit', 'doctor_id')


# объекты для отправки и приёмов запросов
note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)
unsigned_notes_schema = UnsignedNoteSchema(many=True)

