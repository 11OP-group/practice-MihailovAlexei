
print("Введите 10 чисел для проверки на четность")

parity = True

for i in range(10):
    number = int(input(f"Введите число по порядку {i+1}: "))
    if number%2 != 0:
        parity = False


if parity:
    print("YES")
else:
    print("NO")