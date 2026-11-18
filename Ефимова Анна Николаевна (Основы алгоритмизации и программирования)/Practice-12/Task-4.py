import random
marks = []

for i in range(1, random.randint(3, 30)):
    marks.append(random.randint(2, 5))

print(f"Количество пятерок: {marks.count(5)}")
print(f"Количество двоек: {marks.count(2)}")
print(f"Оценки: {marks}")