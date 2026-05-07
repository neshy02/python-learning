# https://stepik.org/lesson/567056/step/5?unit=561330

def get_biggest_city(*args):
    lens = {k: len(k) for k in args}
    return max(lens, key=lens.get)