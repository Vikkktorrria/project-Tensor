from datetime import datetime
from application import db, ma

# класс таблицы Article
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text(500), nullable=False)
    article_img = db.Column(db.String(200))
    created_on = db.Column(db.DateTime(), default=datetime.now)  # когда сознадо
    # связи
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, text, article_img, title, user_id):
        self.text = text
        self.article_img = article_img
        self.title = title
        self.user_id = user_id


# класс для работы с полями в таблице Article
class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'text', 'article_img', 'created_on', 'title')


# объекты для отправки и приёмов запросов
article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)