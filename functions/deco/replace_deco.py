# https://stepik.org/lesson/567063/step/5?unit=561337


t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def replace_deco(chars='!?'):
    def outer(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            for char in chars:
                res = res.replace(char, '-')
            while '--' in res:
                res = res.replace('--','-')
            return res
        return wrapper
    return outer

@replace_deco(chars='?!:;,. ')
def trnslt_text(text):
    text = text.lower()
    res = ''
    for i in text:
        if i in t:
            res += t.get(i)
        else:
            res += i
    return res
            

            
            
s = input()
print(trnslt_text(s))