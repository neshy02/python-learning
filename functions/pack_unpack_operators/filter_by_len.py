# https://stepik.org/lesson/2284240/step/8?unit=2318722

def filter_by_length(*args, min_length=0, max_length):
    return [i for i in args if min_length <= len(i) <= max_length]
    

names_initial = input().split()

names_result = filter_by_length(*names_initial, min_length=5, max_length=9)