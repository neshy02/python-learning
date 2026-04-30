# https://stepik.org/lesson/488831/step/5?unit=480067

n = int(input())
res = {}

for _ in range(n):
    words = input().split()
    country = words[0]
    cities = words[1:]
    for city in cities:
        res[city] = country

m = int(input())

for _ in range(m):
    word = input()
    print(res.get(word))
