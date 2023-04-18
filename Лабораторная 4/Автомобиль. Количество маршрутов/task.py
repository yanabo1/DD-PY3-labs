from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """

    # Инициализируем таблицу нулями
    table = [[0] * m for _ in range(n)]

    # Заполняем первую строку и первый столбец единицами, так как из начальной клетки можно попасть только вниз или вправо
    for i in range(n):
        table[i][0] = 1
    for j in range(m):
        table[0][j] = 1

    # Заполняем оставшиеся клетки
    for i in range(1, n):
        for j in range(1, m):
            table[i][j] = table[i - 1][j] + table[i][j - 1] + table[i - 1][j - 1]

    return table
