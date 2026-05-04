# https://stepik.org/lesson/567044/step/9?unit=561318

lst1 = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]
lst_res = [lst1[i] + lst2[i] for i in range(len(lst1))]
print(*lst_res)
