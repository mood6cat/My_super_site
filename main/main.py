from flask import render_template, Blueprint, request
import logging
from main.main_search import Search

# from main.main_search import Search


main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)  # Логгирование при выполнении поиска - INFO

# В __name__ передаём имя блюпринта, потом нужна папка templates в папке с этим блюпринтом
# 2) регистрируется /
#  3)В первом случае просто возвращается render template
@main_blueprint.route('/', methods=['GET'])  # Метод GET - стандартный, для получения данных с
# сервера, потому не указывается в следующих функциях
def main_page_index():
    return render_template('index.html')

#   4) Во втором случае мы через args получаем какое слово, по которому будем производить поиск
# создали класс для поиска и загрузки постов
@main_blueprint.route('/search')
def main_search():
    sub_word = request.args.get('s')
    logging.info(f'Поиск: {sub_word}')
    search_content = Search('posts.json')
    post, error = search_content.search_post(sub_word)
    if error:
        logging.info(f'Ошибка: {error}')
        return 'Ошибка '
    return render_template('post_list.html', posts=post, sub_word=sub_word)
