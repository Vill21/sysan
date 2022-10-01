from modules import *

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

def main() -> None:
    test3_1_r5()

main()