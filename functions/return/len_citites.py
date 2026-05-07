# https://stepik.org/lesson/567053/step/9?unit=561327

def get_len_more_six(word):
    return len(word) >= 6

cities = input().split()
lst = [i for i in cities if get_len_more_six(i)]
print(*lst)