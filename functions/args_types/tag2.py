# https://stepik.org/lesson/567055/step/8?unit=561329

def tag_text(text, tag='h1', up=True):
    if up:
        tag = tag.upper()
    else:
        tag = tag.lower()        
    return f'<{tag}>{text}</{tag}>'

text = input()

print(tag_text(text, tag='div'))
print(tag_text(text, tag='div', up=False))