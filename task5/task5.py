import json
import numpy as np

                
def decompose(array: list):
    decomposed = []

    for item in array:
        if isinstance(item, list):
            for i in item:
                decomposed.append(i)
        else:
            decomposed.append(item)
    
    return decomposed

def dict_from_json(json_str, elements = None):
    decomposed = []
    if elements != None:
        decomposed = elements
    else:
        decomposed = decompose(json_str)
        decomposed.sort(key=lambda x: int(x))

    index_dict = {}
    for ind, item in enumerate(json_str):
        for d in decomposed:
            if (isinstance(item, list) and d in item) or d == item:
                index_dict[d] = ind
    
    return index_dict

def relation_matrix(json_str, elements = None):
    if elements == None:
        elements = decompose(json_str)
        elements.sort(key=lambda x: int(x))
    
    matrix_size = len(elements)
    matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
    matrix = np.array(matrix)

    indices = dict_from_json(json_str, elements)

    for y, element_y in enumerate(elements):
        for x, element_x in enumerate(elements):
            if indices[element_y] <= indices[element_x]:
                matrix[y, x] = 1
            else:
                matrix[y, x] = 0

    return matrix

def dispute_core(matrix_fs, elements):
    core = []

    for y in range(len(matrix_fs)):
        for x in range(y, len(matrix_fs)):
            if matrix_fs[y, x] == 0:
                core.append([elements[y], elements[x]])

    return core

def task(first: str, second: str):
    json_first = json.loads(first)
    json_second = json.loads(second)

    decomposed = decompose(json_second)
    decomposed.sort(key=lambda x: int(x))

    matrix_first = relation_matrix(json_first, decomposed)
    matrix_second = relation_matrix(json_second, decomposed)

    matrix_fs = np.multiply(matrix_first, matrix_second)
    return dispute_core(matrix_fs, decomposed)


if __name__ == '__main__':
    first = '["1", ["2","3"],"4", ["5", "6", "7"], "8", "9", "10"]'
    second = '[["1","2"], ["3","4","5"], "6", "7", "9", ["8","10"]]'
    result = task(first, second)
    print(result)