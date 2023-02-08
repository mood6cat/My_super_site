def save_pic(pic):
    filename = pic.filename  # Теперь мы получили изображение
    file_type = filename.split('.')[-1]

    if file_type not in ('jpg', 'jpeg', 'svg', 'bmp'):  # какие форматы я считаю корректными
        return None

    pic.save(f'./uploads/{filename}')  # Теперь мы сохранили изображение
    return f'uploads/{filename}'  # Теперь мы возвращаем путь
