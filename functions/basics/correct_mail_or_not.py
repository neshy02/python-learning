# https://stepik.org/lesson/567052/step/10?unit=561326

def check_mail(mail):
    allowed = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_@.')
    if set(mail).issubset(allowed) and '@' in mail and '.' in mail:  # через нейронку узнал что такое issubset
        print('ДА')
    else:
        print('НЕТ')
     
    
mail = input()

check_mail(mail)