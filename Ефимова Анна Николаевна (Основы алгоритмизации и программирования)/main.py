
while True:
    x = input("Ведите пароль:")
    if len(x) > 10:
        print("Пароль сохранен!")
        break
    else:
        print("Пароль слишком легкий")
