# https://stepik.org/lesson/567052/step/8?unit=561326

def find_values():
    lst = list(map(int, input().split()))
    v_min = min(lst)
    v_max = max(lst)
    v_sum = sum(lst)
    print(f'Min = {v_min}, max = {v_max}, sum = {v_sum}')
    
find_values()