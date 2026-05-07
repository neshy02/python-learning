# https://stepik.org/lesson/567053/step/8?unit=561327

tp = input().strip()

#здесь продолжайте программу
if tp == 'RECT':
    def get_sq(w, h):
        return w * h
else:
    def get_sq(a):
        return a * a