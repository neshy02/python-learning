# https://stepik.org/lesson/567068/step/8?unit=561342

fp = open('projects/python/works.my', encoding='UTF8')
fp.seek(9)
fragment = fp.read(11)
fp.close()