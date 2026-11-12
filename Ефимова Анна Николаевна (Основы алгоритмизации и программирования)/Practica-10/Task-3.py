
max = int(input("Введите число: "))

while max != 0:
    num = int(input("Введите число: "))

    if num == 0:
        break
    
    if max < num:
        max = num
    
    
print(f"Самое большое число, которое вы ввели - это {max}")
    


