from flask import Flask, json, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import uuid, jwt

app = Flask(__name__)
CORS(app) #убираем ошибку CORS

# подключение к MySQL
app.config['SECRET_KEY'] = 'MEDCARD' # для кодирования информации
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/medcard_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


# класс таблицы User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    patronymic = db.Column(db.String(45))
    b_date = db.Column(db.Date, nullable=False)
    mail = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(45), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now)  # когда сознадо
    updated_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)  # когда изменено
    # отношения с другими таблицами
    article = db.relationship('Article', backref='user')
    doctor = db.relationship('Doctor', backref='user', uselist=False)
    patient = db.relationship('Patient', backref='user', uselist=False)
    passport = db.relationship('Passport', backref='user', uselist=False)
    snils = db.relationship('Snils', backref='user', uselist=False)
    note = db.relationship('Note', backref='user', uselist=False)

    def __init__(self, public_id, name, surname, patronymic, b_date, mail, password, phone_number):
        self.public_id = public_id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.b_date = b_date
        self.mail = mail
        self.password = password
        self.phone_number = phone_number


# класс для работы с полями в таблице User
class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'public_id', 'name', 'surname', 'patronymic', 'b_date', 'mail', 'password', 'phone_number', 'created_on',
            'updated_on')


# объекты для отправки и приёмов запросов
user_schema = UserSchema()
users_schema = UserSchema(many=True)


# класс таблицы Article
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text(500), nullable=False)
    image = db.Column(db.String(45), nullable=False)  # я пока не знаю, что делать с картинкой
    created_on = db.Column(db.DateTime(), default=datetime.now)  # когда сознадо
    # связи
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, text, image):
        self.text = text
        self.image = image


# класс для работы с полями в таблице Article
class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'text', 'image', 'created_on')


# объекты для отправки и приёмов запросов
article_schema = ArticleSchema()
article_schema = ArticleSchema(many=True)


# класс таблицы Passport
class Passport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)  # нужно ли ограничение по символам?
    series = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now)
    # связи
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, number, series):
        self.number = number
        self.series = series


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
doctor_schema = DoctorSchema(many=True)


# класс таблицы Patient
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anamnesis = db.Column(db.Text(500))
    created_on = db.Column(db.DateTime(), default=datetime.now)
    updated_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)
    # связи
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    note = db.relationship('Note', backref='patient')

    def __init__(self, anamnesis):
        self.anamnesis = anamnesis


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
    number = db.Column(db.Integer)
    created_on = db.Column(db.DateTime(), default=datetime.now)
    # связи
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, number):
        self.number = number


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
    date_of_visit = db.Column(db.DateTime())
    created_on = db.Column(db.DateTime(), default=datetime.now)
    updated_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)
    # связи
    recipe = db.relationship('Recipe', backref='note')
    diagnosis = db.relationship('Diagnosis', backref='note')
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    doctor_id = db.Column(db.Integer(), db.ForeignKey('doctor.id'))
    patient_id = db.Column(db.Integer(), db.ForeignKey('patient.id'))

    def __init__(self, date_of_visit):
        self.date_of_visit = date_of_visit


# класс для работы с полями в таблице Notes
class NoteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_of_visit', 'created_on', 'updated_on')


# объекты для отправки и приёмов запросов
note_schema = NoteSchema()
note_schema = NoteSchema(many=True)


# класс таблицы Diagnosis
class Diagnosis(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    inf_about_diagnosis = db.Column(db.Text(500))
    created_on = db.Column(db.DateTime(), default=datetime.now)
    updated_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)
    # связи
    note_id = db.Column(db.Integer(), db.ForeignKey('note.id'))

    def __init__(self, inf_about_diagnosis):
        self.inf_about_diagnosis = inf_about_diagnosis


# класс для работы с полями в таблице Diagnosis
class DiagnosisSchema(ma.Schema):
    class Meta:
        fields = ('id', 'inf_about_diagnosis', 'created_on', 'updated_on')


# объекты для отправки и приёмов запросов
diagnosis_schema = DiagnosisSchema()
diagnosis_schema = DiagnosisSchema(many=True)


# класс таблицы Recipe
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inf_about_recipe = db.Column(db.Text(500))
    created_on = db.Column(db.DateTime(), default=datetime.now)
    updated_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)
    # связи
    note_id = db.Column(db.Integer(), db.ForeignKey('note.id'))

    def __init__(self, inf_about_recipe):
        self.inf_about_recipe = inf_about_recipe


# класс для работы с полями в таблице Recipe
class RecipeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'inf_about_recipe', 'created_on', 'updated_on')


# объекты для отправки и приёмов запросов
recipe_schema = RecipeSchema()
recipe_schema = RecipeSchema(many=True)


# api
@app.route('/api/user/<public_id>', methods = ['GET'])
def get_one_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message':'No user found'})

    result = user_schema.dump(user)
    return jsonify(result)


@app.route('/api/auth/registration', methods = ['POST'])
def create_user():
    public_id = str(uuid.uuid4())
    name = request.json['name']
    surname = request.json['lastName']
    patronymic = request.json['patronymic']
    b_date = request.json['birthday']
    mail = request.json['mail']
    password = generate_password_hash(request.json['password'], method ='sha256')
    phone_number = request.json['phone']

    user = User(public_id, name, surname, patronymic, b_date, mail, password, phone_number)
    db.session.add(user)
    db.session.commit()
    return make_response('User successful registered', 200)


@app.route('/api/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'message':'Login required!'})

    user = User.query.filter_by(phone_number=auth.username).first()

    if not user:
        return jsonify({'message':'No user found!'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp' : datetime.now()+timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})
    
    return make_response('Could not verify', 401, {'message':'Login required!'})


if __name__ == "__main__":
    app.run(debug=True)
