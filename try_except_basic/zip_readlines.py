# https://stepik.org/lesson/567069/step/6?unit=561343

try:    
    with open('bank.csv', encoding='utf8') as file:
        first = file.readline().strip().split(',')
        second = file.readline().strip().split(',')
        row_data = dict(zip(first, second))
except FileNotFoundError:
    pass