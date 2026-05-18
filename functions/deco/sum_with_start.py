# https://stepik.org/lesson/567063/step/3?thread=solutions&unit=561337

nums = list(map(int, input().split()))


def start_number(start=0):
    def start_deco(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res + start
        return wrapper
    return start_deco

        
@start_number(start=5)
def sum_nums(n):
    return sum(n)

print(sum_nums(nums))