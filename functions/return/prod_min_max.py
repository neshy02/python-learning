# https://stepik.org/lesson/567053/step/11?unit=561327

digs = list(map(int, input().split()))
def get_product(a, b):
    return a * b

print(get_product(min(digs), max(digs)))