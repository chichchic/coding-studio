from pprint import pprint
table = []
for i in range(9):
    table.append([])
    for j in range(9):
        table[i].append((i + 1) * (j + 1))
pprint(table)

table2 = [[i * j for i in range(1, 10)] for j in range(1, 10)]
pprint(table2)

pprint([[0, 0, 0] * 3])
