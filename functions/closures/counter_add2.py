# https://stepik.org/lesson/567061/step/4?unit=561335

def counter_add(n):
    def nums(k):
        return k + n
    return nums

cnt = counter_add(2)
k = int(input())
print(cnt(k))