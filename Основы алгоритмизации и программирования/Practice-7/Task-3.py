# # Задание 3

# Цены - Константы
COFFEE = 120
TEA = 80
JUICE = 100
WATER = 50
LEMONADE = 90

print("╔════════════════════════╗")
print("║       🌟 МЕНЮ 🌟       ║")
print("╚════════════════════════╝")

print("| 1 | Кофе ☕    | 120₽ |", "| 2 | Чай 🍵     | 80₽  |", "| 3 | Сок 🧃     | 100₽ |", "| 4 | Вода 💧    | 50₽  |", "| 5 | Лимонад 🥤 | 90₽  |", sep='\n')
drink = str(input("Введите номер или название напитка: ")).lower()
count = int(input("Введите кол-во порций: "))
code = input("Введите код скидки (Enter - если нет): ")

match drink:
    case "1" | "кофе":
        name, emoji, price = "Кофе", "☕", COFFEE
    case "2" | "чай":
        name, emoji, price = "Чай", "🍵", TEA
    case "3" | "сок":
        name, emoji, price = "Сок", "🧃", JUICE
    case "4" | "вода":
        name, emoji, price = "Вода", "💧", WATER
    case "5" | "лимонад":
        name, emoji, price = "Лимонад", "🥤", LEMONADE
    case _:
        print("❌ Ошибка: такого напитка нет в меню")
        
match count:
    case 0:
        print("❌ Ошибка: количество должно быть больше 0")
        exit()
    case 1:
        word = "порция"
    case 2 | 3 | 4:
        word = "порции"
    case _:
        word = "порций"

match code:
    case "STUDENT":
        percent = 20
    case "":
        percent = 0
    case _:
        print("⚠️ Такого кода нет, скидки не будет")
        percent = 0


total = price * count
discount = total * percent // 100
final = total - discount


print("╔══════════════════════════════╗")
print(f"║     {emoji} КВИТАНЦИЯ КАФЕ {emoji}     ║")
print("╚══════════════════════════════╝")
print(f"Товар: {name} {emoji}")
print(f"Цена за порцию: {price} ₽")
print(f"Количество: {count} {word}")
print(f"Сумма: {total} ₽")
print(f"Скидка ({percent}%): -{discount} ₽")
print("════════════════════════════════")
print(f"💰 К ОПЛАТЕ: {final} ₽")
print("════════════════════════════════")


