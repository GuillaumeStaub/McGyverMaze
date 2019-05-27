class Position:
    '''Class that manages all the positions in the maze
    x being the line number and y the column number
     '''
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def move_down(self):
        return Position(self.x+1, self.y)

    def move_up(self):
        return Position(self.x-1, self.y)

    def move_left(self):
        return Position(self.x, self.y-1)

    def move_right(self):
        return Position(self.x, self.y+1)

    def __add__(self, direction):
        if direction == "U":
            return self.move_up()
        elif direction == "D":
            return self.move_down()
        elif direction == "L":
            return self.move_left()
        elif direction == 'R':
            return self.move_right()

    def __eq__(self, item_to_compare):
        if self.x == item_to_compare.x and self.y == item_to_compare.y:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))
