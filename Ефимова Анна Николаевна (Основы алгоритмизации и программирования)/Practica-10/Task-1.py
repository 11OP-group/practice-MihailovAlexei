
PIN_COD = "4590"


while True:
    pin_cod = input("Введите пни код для входа: ")
    if pin_cod == PIN_COD:
        break
    print("Ошибка. Попробуйте еще раз")

print("Доступ разрешен")