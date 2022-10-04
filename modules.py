from io import StringIO
import queue
from typing import Any
from math import log
import csv
import os

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

class GraphNodeLevel:
    def __init__(self, data: Any, level: int, parents: list = None, children: list = None) -> None:
        self.data = data
        self.parents = None
        self.children = None
        self.level = level

        if parents != None:
            self.parents = parents
            for parent in parents:
                parent.add_children([self])
        
        if children != None:
            self.children = children
            for child in children:
                child.add_parents([self])

    def __str__(self) -> str:
        return str(self.data)

    def set_children(self, children: list) -> None:
        self.children = children

    def add_children(self, children: list) -> None:
        if self.children != None:
            self.set_children(self.children + children)
        else:
            self.set_children(children)

    def set_parents(self, parents: list) -> None:
        self.parents = parents

    def add_parents(self, parents: list) -> None:
        if self.parents != None:
            self.set_parents(self.parents + parents)
        else:
            self.set_parents(parents)

    def set_level(self, level: int) -> None:
        self.level = level

def r1(root: GraphNodeLevel) -> dict:
    visited_children = [root]
    cq = queue.SimpleQueue()
    cq.put(root)

    r1_output = {}
    while not cq.empty():
        pointer = cq.get()
        if pointer.children != None:
            if r1_output.get(pointer) ==  None:
                r1_output[pointer] = []
            for child in pointer.children:
                r1_output[pointer].append(child)
                if child not in visited_children:
                    cq.put(child)
                    visited_children.append(child)

    return r1_output

def r2(root: GraphNodeLevel) -> dict:
    visited_children = [root]
    cq = queue.SimpleQueue()
    cq.put(root)

    r2_output = {}
    while not cq.empty():
        pointer = cq.get()
        if pointer.children != None:
            for child in pointer.children:
                if r2_output.get(child) == None:
                    r2_output[child] = []
                r2_output[child].append(pointer)
                if child not in visited_children:
                    cq.put(child)
                    visited_children.append(child)

    return r2_output

def r3(root: GraphNodeLevel) -> dict:
    visited_children = [root]
    cq = queue.SimpleQueue()
    cq.put(root)

    r3_output = {}
    while not cq.empty():
        pointer = cq.get()
        if pointer.children != None:
            for child in pointer.children:
                if child not in visited_children:
                    cq.put(child)
                    visited_children.append(child)

        visited_parents = [pointer]
        pq = queue.SimpleQueue()
        pq.put(pointer)
        cur_level = pointer.level
        while not pq.empty():
            pointer_parent = pq.get()
            if pointer_parent.parents == None:
                continue
            for parent in pointer_parent.parents:
                if parent not in visited_parents and parent.level < cur_level:
                    pq.put(parent)
                    visited_parents.append(parent)
                    if cur_level - parent.level > 1:
                        if r3_output.get(parent) == None:
                            r3_output[parent] = []
                        r3_output[parent].append(pointer)

    return r3_output

def r4(root: GraphNodeLevel) -> dict:
    visited_children = [root]
    cq = queue.SimpleQueue()
    cq.put(root)

    r4_output = {}
    while not cq.empty():
        pointer = cq.get()
        if pointer.children != None:
            for child in pointer.children:
                if child not in visited_children:
                    cq.put(child)
                    visited_children.append(child)

        visited_parents = [pointer]
        pq = queue.SimpleQueue()
        pq.put(pointer)
        cur_level = pointer.level
        while not pq.empty():
            pointer_parent = pq.get()
            if pointer_parent.parents == None:
                continue
            for parent in pointer_parent.parents:
                if parent not in visited_parents and parent.level < cur_level:
                    pq.put(parent)
                    visited_parents.append(parent)
                    if cur_level - parent.level > 1:
                        if r4_output.get(pointer) == None:
                            r4_output[pointer] = []
                        r4_output[pointer].append(parent)

    return r4_output

def r5(root: GraphNodeLevel) -> dict:
    visited_children = []
    cq = queue.SimpleQueue()
    cq.put(root)

    r5_output = {}
    levels = {}

    while not cq.empty():
        pointer = cq.get()
        visited_children.append(pointer)
        if pointer.children != None:
            for child in pointer.children:
                if child not in visited_children:
                    cq.put(child)
                    if levels.get(child.level) == None:
                        levels[child.level] = []
                    levels[child.level].append(child)

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

def read_csv(file_path) -> list[str]:
    output = []

    # reading csv file
    with open(file_path, "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",", quotechar="|")
        
        for row in csv_reader:
            row_stripped = []
            for i in row:
                row_stripped.append(i.strip())
            output.append(row_stripped)

    return output

def translate_csv(csv_string) -> list[str]:
    output = []

    csv_file = StringIO(csv_string)
    csv_reader = csv.reader(csv_file, delimiter=",", quotechar="|")
    for row in csv_reader:
        row_stripped = []
        for i in row:
            row_stripped.append(i.strip())
        output.append(row_stripped)

    return output
