
while True:
    num = input("Введите натуральное число: ")

    print(f"Цифра 3 встречается ровно {num.count("3")} раз")
    print(f"Последняя цифра встречается ровно {num.count(num[-1])} раз")

    for i in range(len(num)):
        if int(num[i])%2==0:
            continue


