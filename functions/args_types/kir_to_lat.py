# https://stepik.org/lesson/567055/step/6?unit=561329

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
    'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# здесь продолжайте программу

def kir_to_lat(text, sep='-'):
    text = text.lower()
    res = ''
    for ch in text:
        if ch == ' ':
            res += sep
        elif ch in t:
            res += t[ch]
        else:
            res += ch
    return res
            
            
text = input()

print(kir_to_lat(text))
print(kir_to_lat(text, sep = '+'))