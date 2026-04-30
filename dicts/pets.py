# https://stepik.org/lesson/446696/step/19?unit=437002

pets = [
    ('Барсик', 'Маша', 'Петрова', 17),
    ('Джек', 'Галина', 'Лагунова', 45),
    ('Муся', 'Александр', 'Каракулов', 28),
    ('Буся', 'Маша', 'Петрова', 17),
    ('Кира', 'Вова', 'Пухарев', 54),
]
res = {}

for item in pets:
    owner = item[1:4]
    pet = item[0]
    res.setdefault(owner, []).append(pet)
print(res)
        