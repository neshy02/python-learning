# https://stepik.org/lesson/488831/step/6?unit=480067

n = int(input())
phones = {}

for _ in range(n):
    number, name = input().split()
    name = name.lower()
    if name in phones:
        phones[name].append(number)
    else:
        phones[name] = []
        phones[name].append(number)

m = int(input())

for _ in range(m):
    query = input().lower()
    if query in phones:
        print(*phones[query])
    else:
        print('абонент не найден')