import statistics
import BoardingMethods
import BoardingSimulator
import models

types = ["Random", "WindowMA", "WMAGroups", "BackToFront",
         "FrontToBack", "SteffenOptimal", "SimulationOptimal"]


def benchmark(bench_type, iter=10):
    tick_scores = []
    node_ticks = []
    model = models.Model("737")

    if bench_type not in types:
        print("Invalid benchmark type")
        return 0

    for i in range(iter):
        if bench_type == "Random":
            nodes = BoardingMethods.Random()
        elif bench_type == "WindowMA":
            nodes = BoardingMethods.WindowMA()
        elif bench_type == "WMAGroups":
            nodes = BoardingMethods.WindowMA()
        elif bench_type == "BackToFront":
            nodes = BoardingMethods.BackToFront()
        elif bench_type == "FrontToBack":
            nodes = BoardingMethods.FrontToBack()
        elif bench_type == "SteffenOptimal":
            nodes = BoardingMethods.SteffenOptimal()
        elif bench_type == "SimulationOptimal":
            nodes = BoardingMethods.SimulationOptimal()

        count = 0
        while isDone(nodes) == 0:
            BoardingSimulator.generate_next(model, nodes)
            count += 1
        for node in nodes:
            node_ticks.append(node.node_tick)
        tick_scores.append(count)

    print("[" + bench_type + " Benchmark] x" + str(iter))
    print("avg-completion: " +
          str(statistics.mean(tick_scores)) + " ticks.")
    print("min-completion: " +
          str(min(tick_scores)) + " ticks.")
    print("max-completion: " +
          str(max(tick_scores)) + " ticks.")
    print("avg-per-node: " +
          str(statistics.mean(node_ticks)) + " ticks.")
    print("min-node: " +
          str(min(node_ticks)) + " ticks.")
    print("max-node: " +
          str(max(node_ticks)) + " ticks.")
    print()


def write(bench_type, file_name="out.txt"):
    model = models.Model("737")
    if bench_type == "Random":
        nodes = BoardingMethods.Random()
    elif bench_type == "WindowMA":
        nodes = BoardingMethods.WindowMA()
    elif bench_type == "WMAGroups":
        nodes = BoardingMethods.WMAGroups()
    elif bench_type == "BackToFront":
        nodes = BoardingMethods.BackToFront()
    elif bench_type == "FrontToBack":
        nodes = BoardingMethods.FrontToBack()
    elif bench_type == "SteffenOptimal":
        nodes = BoardingMethods.SteffenOptimal()
    elif bench_type == "SimulationOptimal":
        nodes = BoardingMethods.SimulationOptimal()
    else:
        print("Invalid benchmark type")
        return 0

    open('out.txt', 'w').close()
    text_file = open(file_name, "a")
    ticks_elapsed = 0
    while isDone(nodes) == 0:
        BoardingSimulator.generate_next(model, nodes)
        ticks_elapsed += 1
        text_file.write(model.str())
        text_file.write(("Tick: " + str(ticks_elapsed)).rjust(63) + "\n")
        text_file.write("[frame]\n")
    text_file.close()
    print("File written: " + file_name)


def isDone(nodes):
    """check if a set of nodes is finished boarding"""
    for node in nodes:
        if node.dest_aisle != node.aisle_pos:
            return 0
    return 1
