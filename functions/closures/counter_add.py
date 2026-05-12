# https://stepik.org/lesson/567061/step/3?unit=561335

def counter_add():
    def add(x):
        x += 5
        return x
    return add

k = int(input())
cnt = counter_add()

print(cnt(k))