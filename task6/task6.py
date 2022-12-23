import numpy as np
import json


def to_json(s: str):
    js = json.loads(s)
    s_out = []
    for j in js:
        if isinstance(j, list):
            s_out.append(j)
        if isinstance(j, str):
            a = []
            a.append(j)
            s_out.append(a)
    return s_out


def exp_ind(arr: list, experts: list[list]):
    ind = -1
    for i in range(len(experts)):
        if arr == experts[i]:
            ind = i
    return ind


def create_matrix(experts: list[list], index: int):
    exp = np.zeros((len(experts[index]), len(experts[index])))
    for i in range(len(experts[index])):
        for j in range(len(experts[index])):
            if experts[index][i] < experts[index][j]:
                exp[i][j] = 1
            if experts[index][i] == experts[index][j]:
                exp[i][j] = 0.5
            if experts[index][i] > experts[index][j]:
                exp[i][j] = 0
    return exp


def task(js: str):
    experts = to_json(js)
    experts_matrices = []
    for exp in experts:
        experts_matrices.append(create_matrix(experts, exp_ind(exp, experts)))

    m = np.zeros(experts_matrices[0].shape)
    for i in range(experts_matrices[0].shape[0]):
        for j in range(experts_matrices[0].shape[0]):
            for k in range(len(experts_matrices)):
                m[i][j] += 1/experts_matrices[k].shape[0] * experts_matrices[k][i][j]

    k0 = []
    for i in range(experts_matrices[0].shape[0]):
        k0.append(1/experts_matrices[0].shape[0])

    y = np.dot(m, k0)
    l = np.dot(np.array([1, 1, 1]), y)
    k1 = np.dot(1/l, y)

    while max(abs(k1-k0)) >= 0.001:
        k0 = k1
        y = np.dot(m, k0)
        l = np.dot(np.array([1, 1, 1]), y)
        k1 = np.dot(1/l, y)

    return [round(x,3) for x in k1]


if __name__ == '__main__':
    json_str = '[[1,3,2],[2,2,2],[1.5,3,1.5]]'
    result = task(json_str)
    expected = [0.468, 0.169, 0.363]
    print(result)
    print('Result is as Expected:', result == expected)
