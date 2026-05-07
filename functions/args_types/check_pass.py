# https://stepik.org/lesson/567055/step/5?unit=561329

def check_password(password, chars="$%!?@#"):
    return len(password) >= 8 and any(char in chars for char in password)