import networkx as nx


class Sudoku(object):
    pass


class Cell(object):
    pass


class Number(object):
    pass


def get_block(x, y):
    return (((x-1)//3)+1)+(((y-1)//3)*3)


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
            g.add_edge(key,key2, direction='y')
        elif int(value['y'])+1 == int(value2['y']) and int(value['x']) == int(value2['x']):
            g.add_edge(key,key2, direction='x')
            # print("Enlace {0} - {1}".format(key, key2))
# print(g.node)
for key, value in g.edge.items():
    print(key,value)
# print(g.nodes())
# print(g.edges())
