# https://stepik.org/lesson/2284240/step/5?unit=2318722

def count_chars(s, chars, *, return_type=tuple, ignore_case=True):
    if ignore_case:
        s = s.lower()
        chars = chars.lower()
        
    res = [s.count(i) for i in chars]
    
    return return_type(res)
    

text = input()
symbols = input()

result = count_chars(text, symbols, return_type=set, ignore_case=False)