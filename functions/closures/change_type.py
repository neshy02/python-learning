# https://stepik.org/lesson/567061/step/7?unit=561335

def change_type(tp):
    def text(nums):
        if tp == 'list':
            return list(nums)
        else:
            return tuple(nums)
    return text

tp = input()
nums = input().split()
f = change_type(tp)
res = f(nums)

print(res)