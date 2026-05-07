# https://stepik.org/lesson/567052/step/9?unit=561326

def perimeter(width, height):
    a, b = width, height
    x = 2 * (a + b)
    print(f'Периметр прямоугольника, равен {x}')
    
w, h = list(map(int, input().split()))

perimeter(w, h)