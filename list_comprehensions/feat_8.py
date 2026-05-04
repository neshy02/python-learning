# https://stepik.org/lesson/567044/step/10?unit=561318

text = input().split()
res = [[text[i], int(text[i + 1])] for i in range(0, len(text), 2)]
print(res)