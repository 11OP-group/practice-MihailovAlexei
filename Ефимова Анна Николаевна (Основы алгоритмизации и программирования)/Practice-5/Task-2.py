



weight, height = map(float, input("Введите свой вес(кг) и рост(в метрах): ").split())

bmi = weight / height**2

print(f"Ваш индекс массы тела соотвествует {bmi:.1f}")
