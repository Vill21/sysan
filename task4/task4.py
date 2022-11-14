import sys, os

ROOT = os.path.abspath(os.pardir)

sys.path.insert(1, ROOT)

from modules import H, l_matrix, GraphNodeLevel, translate_csv
import queue

def task(csv_file):

    nodes = translate_csv(csv_file)

    # creating instances of GraphNodeLevel without levels being set
    data_node: dict = {}
    node_data: dict = {}
    for i in nodes:
        if data_node.get(i[0]) == None:
            node = GraphNodeLevel(i[0], 0)
            data_node[i[0]] = node
            node_data[node] = i[0]
        if data_node.get(i[1]) == None:
            node = GraphNodeLevel(i[1], 0)
            data_node[i[1]] = node
            node_data[node] = i[1]
        
        first: GraphNodeLevel = data_node.get(i[0])
        second: GraphNodeLevel = data_node.get(i[1])

        first.add_children([second])
        second.add_parents([first])

    # setting levels for each node in a tree
    root: GraphNodeLevel = data_node.get(nodes[0][0])
    q = queue.SimpleQueue()
    q.put(root)
    while not q.empty():
        pointer: GraphNodeLevel = q.get()
        pointer.set_level(1) if pointer == root else pointer.set_level(pointer.parents[0].level + 1)
        if pointer.children == None:
            continue
        for child in pointer.children:
            q.put(child)

    l = l_matrix([key for key in node_data], 5)
    entropy = H(l, 5, 2)

    return entropy

if __name__ == '__main__':
    csv_str = '''1,2
    1,3
    3,4
    3,5'''

    entropy = task(csv_str)
    print(entropy)