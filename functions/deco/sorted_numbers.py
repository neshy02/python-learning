# https://stepik.org/lesson/567062/step/5?unit=561336

numbers = input()

def deco(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res = sorted(res)
        return res
    return wrapper

@deco
def get_list(n):
    lst = [int(i) for i in n.split()]
    return lst

print(get_list(numbers))