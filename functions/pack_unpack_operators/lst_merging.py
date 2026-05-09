# https://stepik.org/lesson/567057/step/8?unit=561331

nums = list(map(float, input().split()))
cities = input().split()
lst = [*nums, *cities]
print(*lst)