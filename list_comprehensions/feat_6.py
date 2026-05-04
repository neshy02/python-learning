# https://stepik.org/lesson/567044/step/8?unit=561318

nums = input()
lst = [float(i) for i in nums.split()]
lst_res = [i for i in lst if int(i) % 2 == 0]
print(lst_res)
