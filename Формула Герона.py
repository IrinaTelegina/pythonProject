a = float(input('Введите сторону А '))
b = float(input('Введите сторону Б '))
c = float(input('Введите сторону С '))

p = (a + b + c) / 2
S = (p * (p-a) * (p-b) * (p-c)) ** 0.5
print (f'Площадь треугольника: {round(S, 10)}')
