n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
if m < n:
    for i in range(n, m-1, -1):
        print(i)
else:
    for i in range(n, m+1):
        print(i)