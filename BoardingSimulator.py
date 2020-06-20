def generate_next(model, nodes, increment=1):
    for i in range(0, increment):
        # move passengers in seats first
        for node in nodes:
            if node.aisle_pos == "B" or node.aisle_pos == "E":
                move(node, model)
        for node in nodes:
            if node.aisle_pos == "C" or node.aisle_pos == "D":
                move(node, model)
        # then in queue
        for index, node in enumerate(nodes):
            if node.aisle_pos == "Q":
                # pushing onto the queue
                if node.pos == -1 and model.queue[0] == 0:
                    model.queue[0] = 1
                    node.pos += 1
                    node.node_tick += 1
                # moving forward on pre queue
                elif node.pos < -1:
                    if nodes[index - 1].pos != node.pos:
                        node.pos += 1
                    node.node_tick += 1
                # already in queue
                else:
                    move(node, model)


def move(node, model):
    # check if node is already in correct seat
    if node.dest_aisle != node.aisle_pos:
        # increment node tick
        node.node_tick += 1
        if node.dest_row > node.pos and model.queue[node.pos + 1] == 0:
            # move forward
            model.queue[node.pos + 1] = 1
            model.queue[node.pos] = 0
            node.pos += 1
        elif node.dest_row == node.pos:
            # passenger is at corridor of correct row
            if node.aisle_pos == "Q":
                if node.wait_tick == 0:
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
                    node.wait_tick -= 1
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
