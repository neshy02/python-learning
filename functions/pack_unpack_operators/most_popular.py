# https://stepik.org/lesson/2284240/step/4?unit=2318722

writers = input().split()

def most_popular(people, *, case_sens=False):
    if case_sens:
        lst = people
    else:
        lst = [i.lower() for i in people]
        
    d = {k: lst.count(k) for k in lst}
    res = max(d, key=d.get)
    return (res, d[res])

result = most_popular(writers, case_sens=True)

# это было тяжко))