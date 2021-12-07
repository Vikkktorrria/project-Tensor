from datetime import datetime
from application import db, ma

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