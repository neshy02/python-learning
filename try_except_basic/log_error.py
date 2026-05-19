# https://stepik.org/lesson/567069/step/7?unit=561343

try:
    with open('logs/01-01-2025/log_app.txt', encoding='utf8') as file:
        log_errors = []
        for line in file:
            if '[ERROR]' in line:
                log_errors.append(line.strip())
                
except FileNotFoundError:
    pass