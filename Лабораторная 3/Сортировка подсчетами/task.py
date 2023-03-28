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
    if not container:
        return []
    max_val = max(container)
    counts = [0] * (max_val+1)
    for x in container:
        counts[x] += 1
    res = []
    for i in range(max_val+1):
        res.extend([i] * counts[i])
    return res


