summ = float(input('Введите сумму '))
mes = int(input('Введите количество месяцев '))
i = 0
while i < mes:
    summ += summ * (0.0418 / 12)
    i += 1

print (int(summ))

