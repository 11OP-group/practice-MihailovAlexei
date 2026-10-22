
n = int(input("Введите натуральное число: "))

sign = 1

sum = 0

for i in range(1, n+1):
    sum = sum + i * sign
    sign = sign * (-1)

print(f"{sum} – значение суммы")