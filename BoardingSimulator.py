import models
import numpy as np
import random
import statistics


def main():
    plane = models.Model("737")
    nodes = createNodes(Random())

    # generate_next(plane, nodes)
    # plane.print()
    # generate_next(plane, nodes)
    # plane.print()
    # generate_next(plane, nodes)
    # plane.print()
    # generate_next(plane, nodes)
    # plane.print()
    # generate_next(plane, nodes)
    # plane.print()
    benchmark("Random", plane, 1)


def benchmark(bench_type, model, count = 50):
    tick_scores = []
    for i in range(count):
        if bench_type == "Random":
            nodes = createNodes(Random())
        else:
            print("Invalid benchmark type")
            return 0
        t = 0
        open('out.txt', 'w').close()
        text_file = open("out.txt", "a")
        while isDone(nodes) == 0:
            generate_next(model, nodes)
            text_file.write(model.str())
            text_file.write("[frame]\n")
            t += 1
        text_file.close()
        tick_scores.append(t)
    print("Benchmark " + bench_type + " avg: " + str(tick_scores[0]) + " ticks.")


# check if a set of nodes is finished boarding
def isDone(nodes):
    for node in nodes:
        if node.dest_aisle != node.aisle_pos:
            return 0
    return 1


def createNodes(list):
    nodes = []
    for i in range(0, len(list)):
        nodes.append(models.Node(i, list[i][1], list[i][0]))
    return np.array(nodes)


def Random():
    list = []
    for i in range(0, 6):
        for j in range(0, 30):
            seat_tuple = (i, j)
            list.append(seat_tuple)
    random.shuffle(list)
    return list


def generate_next(model, nodes, increment = 1):
    for i in range (0, increment):
        for node in nodes:
            if node.aisle_pos == "B" or node.aisle_pos == "E":
                move(node, model)
        for node in nodes:
            if node.aisle_pos == "C" or node.aisle_pos == "D":
                move(node, model)
        for index, node in enumerate(nodes):
            if node.aisle_pos == "Q":
                if node.pos == -1 and model.queue[0] == 0:
                    model.queue[0] = 1
                    node.pos += 1
                elif node.pos < -1:
                    if nodes[index - 1].pos != node.pos:
                        node.pos += 1
                else:
                    move(node, model)

# move used only for nodes already in queue
def move(node, model):
    if node.dest_row > node.pos and model.queue[node.pos + 1] == 0:
        # move forward
        model.queue[node.pos + 1] = 1
        model.queue[node.pos] = 0
        node.pos += 1
    elif node.dest_row == node.pos and node.aisle_pos != node.dest_aisle:
        # passenger is at corridor of correct row
        if node.aisle_pos == "Q":
            if node.tick == 0:
                # passenger finished storing, aisle on A/B/C
                if node.dest_aisle == "A" or node.dest_aisle == "B" or node.dest_aisle == "C":
                    model.seats[2][node.dest_row] += 1
                    model.queue[node.dest_row] = 0
                    node.aisle_pos = "C"
                # passenger finished storing, aisle on D/E/F
                else:
                    model.seats[3][node.dest_row] += 1
                    model.queue[node.dest_row] = 0
                    node.aisle_pos = "D"
            # passenger storing
            else:
                node.tick -= 1
        elif node.aisle_pos == "B":
            model.seats[0][node.pos] += 1
            model.seats[1][node.pos] -= 1
            node.aisle_pos = "A"
        elif node.aisle_pos == "C":
            model.seats[1][node.pos] += 1
            model.seats[2][node.pos] -= 1
            node.aisle_pos = "B"
        elif node.aisle_pos == "D":
            model.seats[4][node.pos] += 1
            model.seats[3][node.pos] -= 1
            node.aisle_pos = "E"
        elif node.aisle_pos == "E":
            model.seats[5][node.pos] += 1
            model.seats[4][node.pos] -= 1
            node.aisle_pos = "F"

main()
