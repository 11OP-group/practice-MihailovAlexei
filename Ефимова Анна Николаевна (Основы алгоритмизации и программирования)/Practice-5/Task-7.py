FUEL_PRICE_PER_LITER = 49.5

def calculate_trip_cost(distance, fuel_consumption):
    """
    Рассчитываем расход топлива и стоимость поездки на такси

    Args:
        distance_km (float): расстояние поездки в километрах
        fuel_consumption_per_100km (float): расход топлива машины на 100 км в литрах

    Returns:
        float: расход топлива в литрах 
        float: стоимость поездки в рублях
    """

    total_fuel_consumption = distance * (fuel_consumption / 100)
    total_price = total_fuel_consumption * FUEL_PRICE_PER_LITER

    return total_fuel_consumption, total_price

distance = float(input("Введите расстояние (км): "))
fuel_consumption = float(input("Сколько литров на 100 км ест машина? "))

total_fuel_consumption, total_price = calculate_trip_cost(distance, fuel_consumption)

print(f"Нужно бензина: {total_fuel_consumption} л")
print(f"Стоимость поездки: {total_price} рублей")





