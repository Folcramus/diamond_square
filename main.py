import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray


def diamond_square(n, R, initial_heights) -> ndarray:
    size = 2 ** n + 1
    height_map = np.zeros((size, size))

    # Установка начальных высот для углов квадрата
    height_map[0, 0] = initial_heights[0]
    height_map[0, size - 1] = initial_heights[1]
    height_map[size-1, 0] = initial_heights[2]
    height_map[size-1, size-1] = initial_heights[3]

    step = size
    while step > 1:
        half_step = step // 2

        # Square
        for i in range(half_step, size - 1, step):
            for j in range(half_step, size - 1, step):
                # Среднее арифметическое вершин сдвинутое на случайную величину
                height_map[i, j] = (height_map[i - half_step, j - half_step] +
                                    height_map[i - half_step, j + half_step] +
                                    height_map[i + half_step, j - half_step] +
                                    height_map[i + half_step, j + half_step]) / 4 + (np.random.random() * 2 - 1) * half_step * R

        # Diamond
        for i in range(0, size - 1, half_step):
            for j in range((i + half_step) % step, size - 1, step):
                # Среднее арифметическое вершин сдвинутое на случайную величину
                height_map[i, j] = (height_map[(i - half_step) % size, j] +
                                    height_map[(i + half_step) % size, j] +
                                    height_map[i, (j - half_step) % size] +
                                    height_map[i, (j + half_step) % size]) / 4 + (np.random.random() * 2 - 1) * half_step * R

        step = half_step

    return height_map


# Параметры алгоритма
n = int(input("Введите размерность n: "))  # Размерность карты высот, 2^n + 1
R = float(input("Введите значение параметра R: "))  # Шероховатость

# Ввод высот углов
print("Введите высоты углов:")
top_left = int(input("Верхний левый угол: "))
top_right = int(input("Верхний правый угол: "))
bottom_left = int(input("Нижний левый угол: "))
bottom_right = int(input("Нижний правый угол: "))
initial_heights = [top_left, top_right, bottom_left, bottom_right]

# Генерация карты высот
height_map = diamond_square(n, R,  initial_heights)


# Отображение карты высот
plt.imshow(height_map, cmap='terrain')
plt.colorbar()
plt.show()