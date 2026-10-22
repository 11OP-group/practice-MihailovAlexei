import random

chosen_number = random.randint(1, 10)

print("Я загадал число от 1 до 10. Одгадай его за 3 попытки")
for i in range(1, 4):
    conjecture = int(input(f"Попытка {i}: "))
    if conjecture == chosen_number:
        print("Угадали!")
        break
    if conjecture > chosen_number:
        print(f"Неверно. Бери меньше")
    else:
        print(f"Неверно. Бери больше")
else:
    print(f"Ты не угадал мое число. Я загадал {chosen_number}")