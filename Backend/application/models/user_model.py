from datetime import datetime
from application import db, ma

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