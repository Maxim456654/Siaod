import networkx as nx
import matplotlib.pyplot as plt


# Создание матрицы смежности
adjacency_matrix = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]

# Преобразование матрицы смежности в список ребер
edges = []
for i in range(len(adjacency_matrix)):
    for j in range(i+1, len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] == 1:
            edges.append((i, j))

# Создание графа на основе списка ребер
G = nx.Graph(edges)

# Визуализация графа
nx.draw(G, with_labels=True)
plt.show()

# Вычисление кратчайшего расстояния между задаваемыми вершинами
shortest_path_length = nx.shortest_path_length(G, source=0, target=3)

# Вывод кратчайшего расстояния
print("Кратчайшее расстояние от вершины 0 до вершины 4:", shortest_path_length)