k = int(input("Первое число - "))
n = int(input("Второе число - "))
s = 0

for i in range(k, n+1):
    if i % 2 == 0:
        s += i
print(s)