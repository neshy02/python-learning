# https://stepik.org/lesson/567053/step/10?unit=561327

def get_len_cities(word):
    return word, len(word)
    
cities = input().split()
d = {k: v for city in cities for k, v in [get_len_cities(city)]}
a = sorted(d, key=d.get)
print(*a)