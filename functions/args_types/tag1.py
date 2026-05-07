# https://stepik.org/lesson/567055/step/7?unit=561329

def tag_text(text, tag='h1'):
    return f'<{tag}>{text}</{tag}>'

text = input()

print(tag_text(text))
print(tag_text(text, tag='div'))