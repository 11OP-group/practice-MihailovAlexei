n = int(input("Факториал какого числа вы хоте получить: "))
fac = 1
for i in range(1, n+1):
    fac = fac * i 
print(fac)
