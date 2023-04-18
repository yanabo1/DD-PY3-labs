from typing import Union

import networkx as nx


def stairway_graph(stairway):
    n = len(stairway)
    G = nx.DiGraph()
    for i in range(n):
        G.add_node(i, weight=stairway[i])
    for i in range(n - 2):
        G.add_edge(i, i + 2, weight=0)
        G.add_edge(i, i + 3, weight=0)
    G.add_edge(0, 1, weight=0)
    G.add_edge(0, 2, weight=0)
    return G


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    path = nx.dijkstra_path(graph, 0, graph.number_of_nodes() - 1)
    return sum(graph[u][v]["weight"] for u, v in zip(path[:-1], path[1:]))


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = stairway_graph(stairway)
    print(stairway_path(stairway_graph))  # 72