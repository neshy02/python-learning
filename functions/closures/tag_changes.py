# https://stepik.org/lesson/567061/step/6?thread=solutions&unit=561335

def tag_text(tag):
    def words(text):
        return f'<{tag}>{text}</{tag}>'
    return words

tag = input()
text = input()
f = tag_text(tag)
res = f(text)

print(res)