from modules import r1, r2, r3, r4, r5, GraphNodeLevel, translate_csv
import queue

def task(csv_file) -> list[list[list[str]]]:
    """ Возвращает массив отношений для пар вершин системы вида дерева. """

    nodes = translate_csv(csv_file)
    print(nodes)

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

    # getting relations
    r1_dict = r1(data_node.get(nodes[0][0]))
    r2_dict = r2(data_node.get(nodes[0][0]))
    r3_dict = r3(data_node.get(nodes[0][0]))
    r4_dict = r4(data_node.get(nodes[0][0]))
    r5_dict = r5(data_node.get(nodes[0][0]))

    def get_r_list(rk_dict: dict) -> list[list[str]]:
        output = []
        for key in rk_dict:
            for item in rk_dict.get(key):
                output.append([node_data.get(key), node_data.get(item)])
        
        return output

    output = []
    output.append(get_r_list(r1_dict))
    output.append(get_r_list(r2_dict))
    output.append(get_r_list(r3_dict))
    output.append(get_r_list(r4_dict))
    output.append(get_r_list(r5_dict))

    return output