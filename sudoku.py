import networkx as nx


class Sudoku(object):
    pass


class Cell(object):
    pass


class Number(object):
    pass


def get_block(x, y):
    if x <= 3:
        a = 1
    elif x <= 6:
        a = 2
    elif x <= 9:
        a = 3

    if y <= 3:
        b = 0
    elif y <= 6:
        b = 3
    elif y <= 9:
        b = 6
    return a + b


g = nx.Graph()
count = 1
for x in range(1, 10):
    for y in range(1, 10):
        g.add_node('{0}'.format(count), {'x': x, 'y': y, 'block': get_block(x, y)})
        count += 1

for key, value in g.node.items():
    node = key
    for key2, value2 in g.node.items():
        if int(value['x'])+1 == int(value2['x']) and int(value['y']) == int(value2['y']):
            print("Enlace {0} - {1}".format(key, key2))

