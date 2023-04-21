"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        self._queue = []

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди
        :param elem: Элемент, который должен быть добавлен
        """
        self._queue.append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.
        :raise: IndexError - Ошибка, если очередь пуста
        :return: Извлеченный с начала очереди элемент.
        """
        if len(self) == 0:
            raise IndexError("Queue is empty")
        return self._queue.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.
        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)
        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди
        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Index should be an integer")
        if ind < 0 or ind >= len(self):
            raise IndexError("Index out of range")
        return self._queue[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        self._queue.clear()

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self._queue)