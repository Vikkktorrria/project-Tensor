import os

from flask import Response, jsonify, request, make_response

from application import app, db
from application.models.article_model import Article, articles_schema
from application.route.auth import token_required

# список новостей
@app.route('/api/news', methods=['GET'])
def get_articles():
    all = Article.query.all()
    results = articles_schema.dump(all)
    return jsonify(results)


# получить информацию о статье
@app.route('/api/article/<article_id>', methods=['GET'])
def get_article(article_id):
    article = Article.query.filter_by(id=article_id).first()
    results = {'title': article.title, 'text': article.text, 'id': article.id}
    return jsonify(results)


# загрузить img для статьи
@app.route('/api/user/change/article/img/<article_id>', methods=['PUT'])
@token_required
def upload_article_image(current_user, article_id):
    current_article = Article.query.filter_by(id=article_id).first()
    img = request.files['file']
    if not img:
        return make_response("Фото не загружено!", 400)

    filename = img.filename
#     mimetype_reverse = filename[::-1].partition('.')[0]  # определяем тип
#     mimetype = '.' + mimetype_reverse[::-1]
#
#     filename = 'article-' + str(article_id) + '-user-' + str(current_user.id) + mimetype
# удаление нужны права администратора и проверка существует ли файл
#     os.remove(app.config['UPLOAD_FOLDER'] + '/' + str(current_article.article_img))
    img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    current_article.article_img = filename
    db.session.commit()
    return make_response("Файл загружен", 200)


# добавление статьи
@app.route('/api/user/article', methods=['POST'])
@token_required
def add_article(current_user):
    title = request.json['title']
    text = request.json['text']
    article_img = None
    user_id = current_user.id

    if not current_user.is_doctor:
        return make_response('Статья успешно не добавлена', 403)

    article = Article(text, article_img, title, user_id)
    db.session.add(article)
    db.session.commit()

    return make_response('Статья успешно добавлена ' + str(article.id), 200) #редактировать мб


# редиактирование статьи
@app.route('/api/user/change/article/<article_id>', methods=['PUT'])
@token_required
def change_article(current_user, article_id):
    new_title = request.json['title']
    new_text = request.json['text']
    current_article = Article.query.filter_by(id=article_id).first()
    user_id = current_article.user_id

    if not current_user.is_doctor:
        return make_response('Вы не можете редактировать статью. Вы не являетесь доктором.', 403)

    if current_user.id != user_id:
        return make_response('Вы не можете редактировать статью. Это не ваша статья.', 403)

    current_article.title = new_title
    current_article.text = new_text
    db.session.commit()

    return make_response('Статья успешно отредактирована', 200)


# удаление статьи
@app.route('/api/user/delete/article/<article_id>', methods=['DELETE'])
@token_required
def delete_article(current_user, article_id):
    current_article = Article.query.filter_by(id=article_id).first()
    user_id = current_article.user_id

    if not current_user.is_doctor:
        return make_response('Вы не можете удалить статью', 403)

    if current_user.id != user_id:
        return make_response('Вы не можете удалить статью', 403)

    db.session.delete(current_article)
    db.session.commit()

    return make_response('Статья успешно удалена', 200)