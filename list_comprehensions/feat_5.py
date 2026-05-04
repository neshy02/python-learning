# https://stepik.org/lesson/567044/step/7?unit=561318

n = int(input())
lst = [[i for _ in range(n)] for i in range(n)]
for row in lst:
    print(*row)