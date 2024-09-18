s = 0
k = 0

for i in range(int(1000000)):
    f = int(i % 10)
    e = int((i % 100) // 10)
    d = int((i % 1000) // 100)

    c = int((i // 1000) % 10)
    b = int((i // 10000) % 10)
    a = int((i // 100000) % 10)

    #2.1
    if f+e+d == a+b+c:
        s += 1
    else:
        pass

    #2.2
    if a + b + c == 13 and a+b+c == f+e+d:
        k += 1
print(f'Всего счастливых билетов - {s}')
print(f'Всего счастливых билетов, у которых сумма цифр равна 13 - {k}')



