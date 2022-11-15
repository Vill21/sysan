from modules import *
import numpy as np
from lxml import etree
from urllib.request import urlopen

def main() -> None:
    nodes = read_csv("sample2.csv")

    print(nodes)

    nodes_dict = node_dicts_from_csv(nodes)
    data_node = nodes_dict[0]
    node_data = nodes_dict[1]

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

    keys = [x for x in node_data]
    l = l_matrix(keys, 5)

    l_np = np.array(l)
    l_np = l_np.transpose()

    for i in l_np:
        print(i)

    result = H(l, 4, 2)
    print("Энтропия составляет {:.4g}".format(result))

# NOT DONE
def xpath():
    htmlparser = etree.HTMLParser()
    with open("tree.html", "r") as htmlfile:
        html = htmlfile.read()

    local = "tree.html"
    response = urlopen(local)
    tree = etree.parse(response, htmlparser)

xpath()
