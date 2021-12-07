from datetime import datetime
from application import db, ma

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