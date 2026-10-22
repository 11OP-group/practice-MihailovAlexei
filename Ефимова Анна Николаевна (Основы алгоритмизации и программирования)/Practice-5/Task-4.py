
PI = 3.14

def calculate_rectangle_area(width, height):
    """
    Вычесляет площадь прямоугольника

    Args:
        width (float): Ширина треугольника
        height (float): Высота треугольника

    Returns:
        float: Площадь прямоугольника
    """
    area = width * height
    return area

def calculate_circle_area(radius):
    """
    Вычесляет площадь прямоугольника
    
    Args:
        radius (float): Радиус
    
    Returns:
        float: Площадь круга
    """
    area = PI * radius**2
    return area



rectangle_width, rectangle_height = map(float, input("Ведите высоту и длину прямоугольника: ").split())

area_rectangle = calculate_rectangle_area(rectangle_width, rectangle_height)

print(f"Площадь прямоугольника равна {area_rectangle} ")



circle_radius = map(float, input("Ведите радиус круга: ").split())

area_circle = calculate_circle_area(circle_radius)

print(f"Площадь круга равна {area_circle}")



