from typing import Union
import networkx as nx

def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.
    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    path_lengths = nx.dijkstra_path_length(graph, 0, len(graph) - 1)  # находим кратчайшие пути от 0-ой ступени до последней
    return path_lengths

def create_stairway_graph(stairway: tuple) -> nx.DiGraph:
    """
    Создать направленный граф по стоимости ступеней
    :param stairway: Кортеж со стоимостями ступеней
    :return: Взвешенный направленный граф NetworkX
    """
    G = nx.DiGraph()
    G.add_node(0, weight=0)  # добавляем начальную ноду со стоимостью 0
    for i, weight in enumerate(stairway):
        G.add_node(i+1, weight=weight)  # добавляем узлы-ступени
        if i+1 < len(stairway):
            G.add_edge(i, i+1, weight=0)  # дуги "вниз" со стоимостью 0
            G.add_edge(i, i+2, weight=stairway[i+1])  # дуги "вперед" со стоимостью, указанной на следующей ступени
    return G

if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = create_stairway_graph(stairway)
    print(stairway_path(stairway_graph))  # 72
