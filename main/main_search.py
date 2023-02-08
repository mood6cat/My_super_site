import json


class Search:
    def __init__(self, path):
        self.path = path

    def load_post(self):
        post = []
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                post = json.load(file)
        except Exception as e:
            return post, e
        return post, None

    def search_post(self, sub_word):
        """
        Через вхождение находим посты, содержащее данное слово
        """
        posts = []
        load_post, error = self.load_post()
        for p in load_post():
            if sub_word.lower() in p["content"].lower():
                posts.append(p)
        return posts, error

    def save_post_to_json(self, posts):  # Здесь передаём список - posts
        with open(self.path, 'w', encoding='utf-8') as file:  # Перезаписываем наше значение
            json.dump(posts, file)

    def add_post(self, post):  # Здесь получаем наш post
        posts, error = self.load_post()  # Здесь получаем наш post
        posts.append(post)  # В posts мы добавляем наш posts
        self.save_post_to_json(posts)  # передаём наши посты

    # def save_post_to_json(self, ):  # Здесь передаём список
