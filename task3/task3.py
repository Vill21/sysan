import sys, os

ROOT = os.path.abspath(os.pardir)

sys.path.insert(1, ROOT)

from modules import r1, r2, r3, r4, r5, node_dicts_from_csv, GraphNodeLevel, translate_csv
import queue

def task(csv_file) -> list[list[str]]:
    """ Возвращает массив отношений для пар вершин системы вида дерева. """

    nodes = translate_csv(csv_file)

    # creating instances of GraphNodeLevel without levels being set
    node_dicts = node_dicts_from_csv(nodes)
    data_node = node_dicts[0]
    node_data = node_dicts[1]

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

    # getting relations
    r1_dict = r1(data_node.get(nodes[0][0]))
    r2_dict = r2(data_node.get(nodes[0][0]))
    r3_dict = r3(data_node.get(nodes[0][0]))
    r4_dict = r4(data_node.get(nodes[0][0]))
    r5_dict = r5(data_node.get(nodes[0][0]))

    def get_r_list(rk_dict: dict) -> list[list[str]]:
        output = []
        for key in rk_dict:
            output.append(node_data.get(key))
        
        return output

    output = []
    output.append(get_r_list(r1_dict))
    output.append(get_r_list(r2_dict))
    output.append(get_r_list(r3_dict))
    output.append(get_r_list(r4_dict))
    output.append(get_r_list(r5_dict))

    return output