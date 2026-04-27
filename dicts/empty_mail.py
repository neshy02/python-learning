# https://stepik.org/lesson/488830/step/11?unit=480066

users = [
    {'name': 'Andrew', 'email': 'and@gmail.com'},
    {'name': 'Tim', 'phone': '555-1618', 'email': 'tim-tim@yandex.ru'},
    {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
    {'name': 'Vika', 'phone': '547-2123', 'email': 'Viko4ka@gmail.com'},
    {'name': 'Kate', 'surname': 'Maltseva', 'city': 'Vologda'},
]
res = []

for user in users:
    name = user['name']
    if not user.get('email'):
        res.append(name)

print(*sorted(res))