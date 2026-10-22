n = int(input("Введите число n: "))
m = int(input("Введите число m: "))

if m > 0 and n > 0:
    for i in range(m, n):
        if i%17 == 0 or i%10 == 9 or i%15 == 0:
            print(i)
