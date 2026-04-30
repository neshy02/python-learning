# https://stepik.org/lesson/488831/step/1?thread=solutions&unit=480067

n = int(input())
terms = {}

for _ in range(n):
    letter = input()
    word, defin = letter.split(': ')
    word = word.lower()
    terms[word] = defin

m = int(input())

for _ in range(m):
    keys = input().lower()
    print(terms.get(keys, 'Не найдено'))
