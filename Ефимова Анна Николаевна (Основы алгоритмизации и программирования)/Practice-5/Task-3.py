

USD_TO_RUB = 95.50

def convert_usd_to_rub(amount_usd):
    """
    Конвентирует доллары в рубли

    Args:
        amount_usd (float): количество долларов
    
    Returns:
        float: количество долларов
    """

    usd_to_rub = amount_usd * 95.50
    return usd_to_rub

dollars = float(input("Сколько долларов вы хотите конвертировать в рубли:"))

rub = convert_usd_to_rub(dollars)

print(f"Вы получите {rub:.2f} рублей")

