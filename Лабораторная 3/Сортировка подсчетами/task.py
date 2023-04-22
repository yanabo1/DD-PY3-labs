from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    n = len(container)
    sorted_container = list(container)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if sorted_container[j] > sorted_container[j + 1]:
                sorted_container[j], sorted_container[j + 1] = sorted_container[j + 1], sorted_container[j]
                swapped = True
        if not swapped:
            break
    return sorted_container    # TODO реализовать алгоритм сортировки подсчетами
