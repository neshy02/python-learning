# https://stepik.org/lesson/567068/step/4?unit=561342

f_log = open('log.dat', encoding='UTF8')
header = f_log.readline()
for line in f_log:
    last_data = line
f_log.close()