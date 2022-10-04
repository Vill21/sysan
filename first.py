from traceback import print_tb
from modules import *
from task3.task3 import task

def test_r1_r2():
    first = Node(1)
    second = Node(2, first, None)
    third = Node(3, second, [first])

    r1_dict = r1(first)
    print(first, r1_dict.get(first)[0])
    print(second, r1_dict.get(second)[0])
    print(third, r1_dict.get(third)[0])

    print()

    r2_dict = r2(first)
    print(first, r2_dict.get(first)[0])
    print(second, r2_dict.get(second)[0])
    print(third, r2_dict.get(third)[0])

    print()

    print(len(r1_dict), len(r2_dict))

def test_l_matrix() -> None:
    first = Node(1)
    second = Node(2, first, None)
    third = Node(3, second, [second])

    l = l_matrix([first, second, third], 2)

    for j in range(len(l)):
        print(l[j])

def task3_1() -> None:
    first = Node(1)
    second = Node(2, first, None)
    third = Node(3, second, [second])

    r1_dict = r1(first)
    print(first, r1_dict.get(first)[0])
    print(second, r1_dict.get(second)[0])
    print(third, r1_dict.get(third)[0])

    print()

    r2_dict = r2(first)
    print(first, r2_dict.get(first))
    print(second, r2_dict.get(second)[0])
    print(third, r2_dict.get(third)[0])

def test3_1_second():
    first = Node(1)
    second = Node(2, first, [first])
    
    print(second.children[0])

    third = Node(3, second, [second])

    print(second.children[0], second.children[1])

def test3_1_r3():
    first = Node(1)
    second = Node(2, first, None)
    third = Node(3, second, None)
    fourth = Node(4, second, None)

    r3_dict = r3(first)

    print(first, r3_dict.get(first)[0], r3_dict.get(first)[1])
    print(second, r3_dict.get(second))
    print(third, r3_dict.get(third))
    print(fourth, r3_dict.get(fourth))

def test3_1_r4():
    first = Node(1)
    second = Node(2, first, None)
    third = Node(3, second, None)
    fourth = Node(4, second, None)

    r4_dict = r4(first)

    print(first, r4_dict.get(first))
    print(second, r4_dict.get(second))
    print(third, r4_dict.get(third)[0])
    print(fourth, r4_dict.get(fourth)[0])

def test3_1_r5():
    first = NodeLevel(1, 1)
    second = NodeLevel(2, 2, first, None)
    third = NodeLevel(3, 3, second, None)
    fourth = NodeLevel(4, 3, second, None)
    fifth = NodeLevel(5, 3, second, None)

    r5_dict = r5(first)

    print(first, r5_dict.get(first))
    print(second, r5_dict.get(second))
    print(third, r5_dict.get(third)[0], r5_dict.get(third)[1])
    print(fourth, r5_dict.get(fourth)[0], r5_dict.get(fourth)[1])
    print(fifth, r5_dict.get(fifth)[0], r5_dict.get(fifth)[1])

def test3_1_debug():
    first = NodeLevel(1, 1)
    second = NodeLevel(2, 2, first, [first])
    third = NodeLevel(3, 3, second, [second])
    fourth = NodeLevel(4, 2, first, [first])
    fifth = NodeLevel(5, 3, fourth, [fourth])

    l = l_matrix([first, second, third, fourth, fifth], 5)
    result = H(l)

def test3_1_debug2():
    first = GraphNodeLevel(1, 1)
    second = GraphNodeLevel(2, 2, [first], None)
    third = GraphNodeLevel(3, 3, [second], None)
    fourth = GraphNodeLevel(4, 3, [second], None)

    l = l_matrix([first, second, third, fourth], 5)
    result = H(l)

    print("Ответ на первый пункт задачи 3.2 равен {:.4g}".format(result))

def test3_1_debug_graph():
    first = GraphNodeLevel(1, 1)
    second = GraphNodeLevel(2, 2, [first], [first])
    fourth = GraphNodeLevel(4, 2, [first], [first])
    third = GraphNodeLevel(3, 3, [second, fourth], [second, fourth])

    #print_lambda = lambda node: print(node, '\n', len(node.parents), '\n', node.parents[0], node.parents[1], '\n', len(node.children), '\n', node.children[0], node.children[1])

    #print_lambda(first)
    #print_lambda(second)
    #print_lambda(third)
    #print_lambda(fourth)


    l = l_matrix([first, second, third, fourth], 5)
    print(l)
    result = H(l)

    print("Ответ на второй пункт задачи 3.3 равен {:.4g}".format(result))

def test_read_csv() -> None:
    l = read_csv("./sample.csv")

def test_task33() -> None:
    with open('sample.csv') as file:
        csvString = file.read()
        result = task(csvString)

        for i in result:
            print(i)

def main() -> None:
    test_task33()

main()