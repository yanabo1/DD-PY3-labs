def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
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
    return sorted_container
    # TODO реализовать рекурсивный алгоритм нахождения факториала
