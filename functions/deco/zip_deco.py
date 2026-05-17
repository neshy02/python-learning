# https://stepik.org/lesson/567062/step/6?unit=561336

words = input()
trnslt = input()


def zip_deco(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return dict(zip(*res))
    return wrapper
    
    
@zip_deco
def words_f(w, t):
    w = w.split()
    t = t.split()
    return w, t

d = words_f(words, trnslt)

print(*sorted(d.items()))