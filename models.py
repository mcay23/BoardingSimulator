import numpy as np

walk_tick = 1
store_tick = 2


class Node:
    def __init__(self, order, dest_row, dest_aisle):
        self.dest_row = dest_row
        if dest_aisle == 0:
            self.dest_aisle = "A"
        elif dest_aisle == 1:
            self.dest_aisle = "B"
        elif dest_aisle == 2:
            self.dest_aisle = "C"
        elif dest_aisle == 3:
            self.dest_aisle = "D"
        elif dest_aisle == 4:
            self.dest_aisle = "E"
        elif dest_aisle == 5:
            self.dest_aisle = "F"

        self.tick = 2
        # order of entry, decrements as people board front
        self.pos = -1 * order - 1
        self.aisle_pos = "Q"


class Model:
    """Class to hold different plane models"""
    def __init__(self, model_name):
        if model_name == "737":
            self.model = "737"
            self.i = 3
            self.j = 3
            self.rows = 30
            self.groups = 2
        else:
            raise Exception("Only '737' model is available at this time")

        self.seats = np.full((self.i + self.j, self.rows), 0)
        self.queue = np.full(self.rows, 0)
        self.state = self.seats


    def print(self):
        print(self.str())

    def str(self):
        ret = ""
        if self.model == "737":
            ret += "   1                 10                  20                  30\n"
            for i in range(len(self.seats)):
                ret += chr(65 + i) + "  "
                for j in range(len(self.seats[i])):
                    if self.seats[i][j] == 0:
                        ret += "O "
                    elif self.seats[i][j] == 1:
                        ret += '\x1b[6;30;42m' + 'X' + '\x1b[0m '
                    elif self.seats[i][j] == 2:
                        ret += '\x1b[1;34;47m' + 'X' + '\x1b[0m '
                ret += "\n"
                if i == 2:
                    ret += "   "
                    for i in range(0, self.rows):
                        if (self.queue[i] == 0):
                            ret += "= "
                        else:
                            ret += '\x1b[6;30;42m' + 'X' + '\x1b[0m '
                    ret += "\n"
            return ret
        else:
            return "Only 737 is supported at this time"
