from flask import render_template, Blueprint, request
import logging
from loader.utills import save_pic
from main.main_search import Search

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)

@loader_blueprint.route('/post')
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def change_post():
    pic = request.files.get("picture")  # указываем по имени, которое передаём в post_form.html
    content = request.form.get("content")

    if not pic or not content:
        return 'Не все поля заполнены'
    pic_path = save_pic(pic)
    if not pic_path:
        logging.info('Неверный формат файла')
        return 'Неверный формат файла загружен'

    search_content = Search('posts.json')  # Перехватываем наш Class Search
    new_post = {'pic':pic_path, 'content':content}# Возврщаем posts, передаём pic_path
    search_content.add_post(new_post) # Передаём в него наш путь к постам

    return render_template('post_uploaded.html', pic_path = pic_path, content = content)