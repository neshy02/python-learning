# https://stepik.org/lesson/567062/step/4?unit=561336

menu = input()

def show_menu(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        for index, item in enumerate(res, start=1):
            print(f'{index}. {item}')
        return res
    return wrapper

        
@show_menu
def get_menu(s):
    return s.split()