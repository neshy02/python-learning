# https://stepik.org/lesson/567062/step/3?unit=561336

def get_sq(width, height):
    return width * height

def func_show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return print(f'Площадь прямоугольника: {res}')
    return wrapper