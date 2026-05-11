# https://stepik.org/lesson/567058/step/4?unit=561332

n = int(input())

def get_rec_n(n):
    if n > 0:
        get_rec_n(n-1)
        print(n)
    

get_rec_n(n)