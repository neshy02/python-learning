# https://stepik.org/lesson/567069/step/5?unit=561343

success_open_file = True
success_file_operations = True

try:
    with open('images/targets.dat', encoding='UTF8') as tar:
        last_row = tar.readlines()[-1]
except FileNotFoundError:
    success_open_file = False
except:
    success_file_operations = False