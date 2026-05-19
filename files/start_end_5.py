# https://stepik.org/lesson/567068/step/7?unit=561342

f_text = open('course.new.dat', encoding='UTF8')
start_5 = f_text.read(5)
text = f_text.read()
end_5 = text[-5:]
f_text.close()