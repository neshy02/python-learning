# https://stepik.org/lesson/446696/step/18?unit=437002

text = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
text = list(text.split())
res = {}

for word in text:
    if word in res:
        res[word] += 1
    else:
        res.update({word: 1})

max_count = max(res.values())
candidates = []

for count in res:
    if res[count] == max_count:
        candidates.append(count)

print(min(candidates))