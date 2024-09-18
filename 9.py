s = int(input("Стипендия - "))
r = int(input("Расходы - "))
m = int(input("Месяц - "))

for i in range(1,m+1):
    ssum = r * i

    if i % 2 == 0:
        r = r+r*0.03
    else:
        r = r+r*0.05
for j in range(1,m+1):
    if j % 2 == 0:
        r = r+r*0.03
    else:
        r = r+r*0.05
    ssum2 = r*j

print(f'Начальная сумма,чтобы прожить {m} месяцев - {ssum}')
print(f'Начальная сумма,чтобы прожить {m} месяцев, если учитывать рост цен - {ssum2}')