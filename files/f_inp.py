# https://stepik.org/lesson/567068/step/6?unit=561342

f_inp = open('sites/links.txt', encoding='windows-1251')
f_inp.seek(0, 2)
size_file = f_inp.tell()
f_inp.close()