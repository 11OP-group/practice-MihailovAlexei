
def calculate_distance(x1, y1, x2, y2):
    """
    Вычесляет расстояние между точками

    Args:
        x1, y1 (float): Координаты первой точки
        x2, y2 (float): Координаты первой точки
    
    Renurs:
        float: Расстояние мужду точками
    """
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance


def calculate_triangle_area(a, b, c):
    """
    Вычисляет площадь по формуле Герона

    Args:
        a, b, c (float): Длины трех сторон треугольника

    Returns:
        float: Площадь треугольника
    """
    half_perimeter = (a + b + c) / 2
    area = (half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c)) ** 0.5
    return area

x1, y1 = map(float, input("Введите координаты точки A: ").split())
x2, y2 = map(float, input("Введите координаты точки B: ").split())
x3, y3 = map(float, input("Введите координаты точки C: ").split())


side_a = calculate_distance(x1, y1, x2, y2)
side_b = calculate_distance(x2, y2, x3, y3)
side_c = calculate_distance(x3, y3, x1, y1)

triangle_area = calculate_triangle_area(side_a, side_b, side_c)

print(f"Площадь треугольника равна {triangle_area:.2f}")

