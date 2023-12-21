
import math
import matplotlib.pyplot as plt
#Завдання 1
class Point_23:
    # Змінна класу для зберігання кількості створених екземплярів
    count = 0

    def __init__(self, x=0.0, y=0.0):
        """
        Конструктор класу Point_23.

        Параметри:
        - x: x-координата (за замовчуванням 0.0)
        - y: y-координата (за замовчуванням 0.0)
        """
        # Перевірка і встановлення x та y координат
        self._x = self._validate_coordinate(x)
        self._y = self._validate_coordinate(y)

        # Збільшення кількості створених екземплярів
        Point_23.count += 1

    def __del__(self):
        """Деструктор, виводить відповідне повідомлення."""
        print(f"Екземпляр Point_23 з координатами ({self._x}, {self._y}) видалено.")
        # Зменшення кількості створених екземплярів
        Point_23.count -= 1

    def _validate_coordinate(self, coord):
        """Перевірка та встановлення координати в межах [-100, 100]."""
        if -100 <= coord <= 100:
            return coord
        else:
            return 0.0

    @property
    def x(self):
        """Метод для отримання x-координати."""
        return self._x

    @property
    def y(self):
        """Метод для отримання y-координати."""
        return self._y

    @staticmethod
    def get_instance_count():
        """Метод класу, який повертає кількість створених екземплярів."""
        return Point_23.count

    def shift(self, dx, dy):
        """
        Метод для зміни координат точки на dx вздовж x та dy вздовж y.

        Параметри:
        - dx: Зсув вздовж x
        - dy: Зсув вздовж y
        """
        # Збільшення або зменшення координат відповідно до зсувів
        self._x += dx
        self._y += dy
        # Перевірка та встановлення нових координат в межах [-100, 100]
        self._x = self._validate_coordinate(self._x)
        self._y = self._validate_coordinate(self._y)

def calculate_distance(point1, point2):
    """
    Функція для обчислення відстані між двома точками.

    Параметри:
    - point1, point2: Екземпляри класу Point_23
    """
    return math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)

# Завдання 2
# Створити список із трьох точок
points_list = [Point_23(), Point_23(10,15), Point_23(-25,30)]

# Обчислити відстань між другою і третьою точками
distance_before = calculate_distance(points_list[1], points_list[2])
print(f"Відстань між другою і третьою точками перед змінами: {distance_before}")

# Зсунути координати першої точки
points_list[0].shift(30, -20)

# Завдання 3
# Відобразити точки до та після змін
x_values_before = [point.x for point in points_list]
y_values_before = [point.y for point in points_list]

# Змінити координати
points_list[0].shift(30, -20)

x_values_after = [point.x for point in points_list]
y_values_after = [point.y for point in points_list]

# Відобразити на графіку
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(x_values_before, y_values_before, color='blue')
plt.title('Точки перед змінами')

plt.subplot(1, 2, 2)
plt.scatter(x_values_after, y_values_after, color='red')
plt.title('Точки після змін')

plt.show()

# Відобразити відстань після змін
distance_after = calculate_distance(points_list[1], points_list[2])
print(f"Відстань між другою і третьою точками після змін: {distance_after}")

# Завдання 4
filename = "coordinates.txt"
with open(filename, "w") as file:
    for i, point in enumerate(points_list, start=1):
        file.write(f"{i}: {point.x}; {point.y}\n")

print(f"Координати збережено у файлі {filename}.")