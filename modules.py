import queue
from typing import Any
from math import log


class Node:
    def __init__(self, data: Any, parent: Any = None, children: list = None) -> None:
        self.data = data
        self.parent = None
        self.children = None

        if parent != None and type(parent) == Node:
            self.parent = parent
            if parent.children != None:
                parent.set_children(parent.children + [self])
            else:
                parent.set_children([self])
        
        if children != None:
            not_node = False
            for child in children:
                if type(child) != Node:
                    not_node = True
                    break
            
            if not_node:
                self.children = None
            else:
                self.children = children
                for child in children:
                    child.set_parent(self)

    def __str__(self) -> str:
        return str(self.data)

    def set_children(self, children: list) -> None:
        self.children = children

    def set_parent(self, parent: Any) -> None:
        self.parent = parent

class NodeLevel (Node):
    def __init__(self, data: Any, level: int, parent: Any = None, children: list = None) -> None:
        self.data = data
        self.parent = None
        self.children = None
        self.level = level

        if parent != None and type(parent) == NodeLevel:
            self.parent = parent
            if parent.children != None:
                parent.set_children(parent.children + [self])
            else:
                parent.set_children([self])
        
        if children != None:
            not_node = False
            for child in children:
                if type(child) != NodeLevel:
                    not_node = True
                    break
            
            if not_node:
                self.children = None
            else:
                self.children = children
                for child in children:
                    child.set_parent(self)

    def set_level(self, level: int) -> None:
        self.level = level

def r1(root: Node) -> dict:
    visited = [root]
    q = queue.SimpleQueue()

    r1_output = {}
    pointer = root

    while True:
        if pointer.children == None:
            if q.empty():
                break

            pointer = q.get()
            continue

        if r1_output.get(pointer) ==  None:
            r1_output[pointer] = []

        for child in pointer.children:
            r1_output[pointer].append(child)
            if child not in visited:
                q.put(child)

        if q.empty():
            break

        pointer = q.get()
        visited.append(pointer)

    return r1_output

def r2(root: Node) -> dict:
    visited = [root]
    q = queue.SimpleQueue()

    r2_output = {}
    pointer = root

    while True:
        if pointer.children == None:
            if q.empty():
                break

            pointer = q.get()
            continue

        for child in pointer.children:
            if r2_output.get(child) ==  None:
                r2_output[child] = []
            r2_output[child].append(pointer)
            if child not in visited:
                q.put(child)

        if q.empty():
            break

        pointer = q.get()
        visited.append(pointer)

    return r2_output

def r3(root: Node) -> dict:
    visited = [root]
    q = queue.SimpleQueue()

    r3_output = {}
    pointer = root

    while True:
        if pointer.children == None:
            if q.empty():
                break

            pointer = q.get()
            continue

        for child in pointer.children:
            if pointer.parent != None:
                parent_pointer = pointer.parent
                if r3_output.get(parent_pointer) ==  None:
                    r3_output[parent_pointer] = []
                while parent_pointer != None:
                    r3_output[parent_pointer].append(child)
                    parent_pointer = parent_pointer.parent

            if child not in visited:
                q.put(child)

        if q.empty():
            break

        pointer = q.get()
        visited.append(pointer)

    return r3_output

def r4(root: Node) -> dict:
    visited = [root]
    q = queue.SimpleQueue()

    r4_output = {}
    pointer = root

    while True:
        if pointer.children == None:
            if q.empty():
                break

            pointer = q.get()
            continue

        for child in pointer.children:
            if pointer.parent != None:
                parent_pointer = pointer.parent
                if r4_output.get(child) ==  None:
                    r4_output[child] = []
                while parent_pointer != None:
                    r4_output[child].append(parent_pointer)
                    parent_pointer = parent_pointer.parent

            if child not in visited:
                q.put(child)

        if q.empty():
            break

        pointer = q.get()
        visited.append(pointer)

    return r4_output

def r5(root: NodeLevel) -> dict:
    visited = [root]
    q = queue.SimpleQueue()

    r5_output = {}
    levels = {root.level: [root]}
    pointer = root

    while True:
        if pointer.children == None:
            if q.empty():
                break

            pointer = q.get()
            continue

        for child in pointer.children:
            if levels.get(child.level) == None:
                levels[child.level] = []
            levels[child.level].append(child)
            if child not in visited:
                q.put(child)

        if q.empty():
            break

        pointer = q.get()
        visited.append(pointer)

    for key in levels:
        if len(levels[key]) > 1:
            for node in levels[key]:
                if r5_output.get(node) == None:
                    r5_output[node] = []
                r5_output[node] += ([x for x in levels[key] if x != node])

    return r5_output

def H(l, n: int, base = 10) -> float:
    sum: float = 0.0
    denominator = n - 1

    for j in range(len(l)):
        for i in range(len(l[j])):
            if l[j][i] == 0: continue
            sum += (l[j][i] / denominator) * log(l[j][i] / denominator, base)

    return -sum

def row_rk(rk_dict: dict, nodes: list) -> list:
    row = []

    for j in range(len(nodes)):
        values_j = rk_dict.get(nodes[j])
        row.append(0) if values_j == None else row.append(len(values_j))
    
    return row

def l_matrix(nodes: list, k: int):
    l = []

    if k == 2:
        r1_dict = r1(nodes[0])
        r2_dict = r2(nodes[0])

        l.append(row_rk(r1_dict, nodes))
        l.append(row_rk(r2_dict, nodes))
    elif k == 5:
        r1_dict = r1(nodes[0])
        r2_dict = r2(nodes[0])
        r3_dict = r3(nodes[0])
        r4_dict = r4(nodes[0])
        r5_dict = r5(nodes[0])

        l.append(row_rk(r1_dict, nodes))
        l.append(row_rk(r2_dict, nodes))
        l.append(row_rk(r3_dict, nodes))
        l.append(row_rk(r4_dict, nodes))
        l.append(row_rk(r5_dict, nodes))
    else:
        raise ValueError(f"k arg must be equal to 2 or 5, got {k}.")

    return l