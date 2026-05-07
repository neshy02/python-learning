# https://stepik.org/lesson/567056/step/8?unit=561330

def str_min(a, b):
    return a if a < b else b 


def str_min3(a, b, c):
    return str_min(str_min(a, b), c)


def str_min4(a, b, c, d):
    return str_min(str_min3(a, b, c), d)