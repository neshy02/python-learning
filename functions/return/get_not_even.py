# https://stepik.org/lesson/567053/step/7?unit=561327 

def get_not_even(number):
    return not number % 2 == 0


lst_d = list(map(int, input().split()))
lst = [i for i in lst_d if get_not_even(i)]
print(*lst)