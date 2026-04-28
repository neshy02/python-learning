# https://stepik.org/lesson/446696/step/17?unit=437002

text = "TheyDon'tKnowThatWeKnowTheyKnowWeKnow"
res = {}

for ch in text:
    if ch in res:
        res[ch] += 1
    else:
        res.update({ch: 1})

print(res)