# https://stepik.org/lesson/567053/step/6?unit=561327

def get_even(x):
    return x % 2 == 0

while (x := int(input())) != 1:
    if get_even(x):
        print(x)