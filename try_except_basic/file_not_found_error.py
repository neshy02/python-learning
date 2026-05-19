# https://stepik.org/lesson/567069/step/4?unit=561343

try:
    with open('diagnostics.csv', encoding='UTF8') as diag:
        header = diag.readline()
        row = diag.readline()
        success_open_file = True
except FileNotFoundError:
    success_open_file = False