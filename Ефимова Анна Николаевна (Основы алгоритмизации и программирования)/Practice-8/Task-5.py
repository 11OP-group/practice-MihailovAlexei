
n = int(input("Введите количество проверяемых чисел: "))

max = 0
two_max = 0

for i in range(n):
    number = int(input("Введите натуральное число: "))
    if max < number:
        max = number
    if two_max < number and number < max:
        two_max = number

print(f"Максимальное число из последовательности: {max}")
print(f"Второе максимальное число из последовательности: {two_max}")