# https://stepik.org/lesson/567061/step/5?unit=561335

def header_str():
    def tag_str(string):
        return f'<h1>{string}</h1>'
    return tag_str

word = input()
tag = header_str()
res = tag(word)

print(res)