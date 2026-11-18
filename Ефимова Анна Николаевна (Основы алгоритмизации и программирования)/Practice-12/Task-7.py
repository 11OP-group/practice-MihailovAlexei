
numbers = [10, 20, 30, 40, 50]

num = int(input("Введите число: "))

for i in range(len(numbers)):
    if num == numbers[i]:
        print(i)
        break
else:
    print("Нет такого числа")
