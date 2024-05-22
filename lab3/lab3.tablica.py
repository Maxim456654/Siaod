import pandas as pd

# Создаем словарь с данными
data = {
    'Алгоритм': ['Флойда-Уоршелла', 'Дейкстры', 'Беллмана-Форда', 'Джонсона', 'Левита', 'Йена'],
    'Временная сложность': ['O(V^3)', 'O((V + E) * log(V))', 'O(V * E)', 'O(V^2 * log(V) + V * E)', 'O(V + E)', 'O(K * (V^2 + E))']
}

# Создаем DataFrame из словаря
df = pd.DataFrame(data)

# Выводим таблицу
print(df)
print('V - количество узлов,', 'E - количество ребер в графе,', 'K - количество кратчайших путей')