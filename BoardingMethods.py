import random
import models
import numpy as np

# Everything only works with 737 model for now


def Random():
    # random ordering, no groups
    list = []
    for i in range(0, 6):
        for j in range(0, 30):
            seat_tuple = (i, j)
            list.append(seat_tuple)
    random.shuffle(list)
    return createNodes(list)


def WindowMA():
    # window, middle, aisle ordering, 3 groups
    window = []
    middle = []
    aisle = []
    for i in range(0, 30):
        A_seat = (0, i)
        B_seat = (1, i)
        C_seat = (2, i)
        D_seat = (3, i)
        E_seat = (4, i)
        F_seat = (5, i)

        window.append(A_seat)
        window.append(F_seat)
        middle.append(B_seat)
        middle.append(E_seat)
        aisle.append(C_seat)
        aisle.append(D_seat)

    random.shuffle(window)
    random.shuffle(middle)
    random.shuffle(aisle)
    list = window + middle + aisle
    return createNodes(list)


def WMAGroups():
    # 6 groups, WMA Back then WMA front
    window_rear = []
    middle_rear = []
    aisle_rear = []
    window_front = []
    middle_front = []
    aisle_front = []

    for i in range(15, 30):
        A_seat = (0, i)
        B_seat = (1, i)
        C_seat = (2, i)
        D_seat = (3, i)
        E_seat = (4, i)
        F_seat = (5, i)

        window_rear.append(A_seat)
        window_rear.append(F_seat)
        middle_rear.append(B_seat)
        middle_rear.append(E_seat)
        aisle_rear.append(C_seat)
        aisle_rear.append(D_seat)

    for i in range(0, 15):
        A_seat = (0, i)
        B_seat = (1, i)
        C_seat = (2, i)
        D_seat = (3, i)
        E_seat = (4, i)
        F_seat = (5, i)

        window_front.append(A_seat)
        window_front.append(F_seat)
        middle_front.append(B_seat)
        middle_front.append(E_seat)
        aisle_front.append(C_seat)
        aisle_front.append(D_seat)

    random.shuffle(window_rear)
    random.shuffle(middle_rear)
    random.shuffle(aisle_rear)
    random.shuffle(window_front)
    random.shuffle(middle_front)
    random.shuffle(aisle_front)

    list = window_rear + middle_rear + aisle_rear + \
        window_front + middle_front + aisle_front

    return createNodes(list)


def BackToFront():
    # 6 groups, back to front, no WMA
    group1 = []
    group2 = []
    group3 = []
    group4 = []
    group5 = []
    group6 = []

    for i in range(0, 6):
        for j in range(0, 5):
            group6.append((i, j))
        for j in range(5, 10):
            group5.append((i, j))
        for j in range(10, 15):
            group4.append((i, j))
        for j in range(15, 20):
            group3.append((i, j))
        for j in range(20, 25):
            group2.append((i, j))
        for j in range(25, 30):
            group1.append((i, j))

    random.shuffle(group1)
    random.shuffle(group2)
    random.shuffle(group3)
    random.shuffle(group4)
    random.shuffle(group5)
    random.shuffle(group6)

    list = group1 + group2 + group3 + group4 + group5 + group6
    return createNodes(list)


def FrontToBack():
    # 6 groups, front to back, no WMA
    group1 = []
    group2 = []
    group3 = []
    group4 = []
    group5 = []
    group6 = []

    for i in range(0, 6):
        for j in range(0, 5):
            group6.append((i, j))
        for j in range(5, 10):
            group5.append((i, j))
        for j in range(10, 15):
            group4.append((i, j))
        for j in range(15, 20):
            group3.append((i, j))
        for j in range(20, 25):
            group2.append((i, j))
        for j in range(25, 30):
            group1.append((i, j))

    random.shuffle(group1)
    random.shuffle(group2)
    random.shuffle(group3)
    random.shuffle(group4)
    random.shuffle(group5)
    random.shuffle(group6)

    list = group6 + group5 + group4 + group3 + group2 + group1
    return createNodes(list)


def SteffenOptimal():
    # order is absolute, Google Steffen's method
    list = []
    for i in range(29, -1, -2):
        list.append((0, i))
    for i in range(29, -1, -2):
        list.append((5, i))

    for i in range(28, -1, -2):
        list.append((0, i))
    for i in range(28, -1, -2):
        list.append((5, i))

    for i in range(29, -1, -2):
        list.append((1, i))
    for i in range(29, -1, -2):
        list.append((4, i))
    for i in range(28, -1, -2):
        list.append((1, i))
    for i in range(28, -1, -2):
        list.append((4, i))

    for i in range(29, -1, -2):
        list.append((2, i))
    for i in range(29, -1, -2):
        list.append((3, i))
    for i in range(28, -1, -2):
        list.append((2, i))
    for i in range(28, -1, -2):
        list.append((3, i))

    return createNodes(list)


def SimulationOptimal():
    list = []
    for i in range(0, 3):
        for j in range(29, -1, -1):
            list.append((i, j))
    for i in range(5, 2, -1):
        for j in range(29, -1, -1):
            list.append((i, j))
    return createNodes(list)


def createNodes(list):
    # create nodes from a list of parameters
    nodes = []
    for i in range(0, len(list)):
        nodes.append(models.Node(i, list[i][1], list[i][0]))
    return np.array(nodes)
