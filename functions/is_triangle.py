# https://stepik.org/lesson/567053/step/4?unit=561327

def is_triangle(a, b, c):
    return a < b + c and b < c + a and c < b + a