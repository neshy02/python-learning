#https://stepik.org/lesson/446696/step/16?unit=437002

dict1 = {'apple': 7, 'orange': 2, 'peach': 5}
dict2 = {'kiwi': 1, 'apple': 6, 'orange': 2}
result = dict1.copy()

for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result.update({key: value})

print(result)
