from terminal.position import Position
import random
import config.constants as constants


class Labyrinth:

    def __init__(self, filename):
        self.filename = filename
        self.gates = []
        self.walls = []
        self.item = []
        self.start = None
        self.arrival = None
        self.hero = None
        self.width = None
        self.height = None
        # We must use the method of the Labyrinth class
        # to load the start position of our character
        self.load_from_file()
        # We must use the method of the Labyrinth class
        # to load the items position
        self.generate_item_position()

    def load_from_file(self):
        '''Manage the initialization of the maze
        from a text file self.filename.
        The method processes all the rows and columns of the file
        one by one and associates a character with
        a position of doors, walls, etc.
        '''
        with open(self.filename, 'r') as f:
            for num_line, line in enumerate(f):
                for num_column, carac in enumerate(line):
                    if carac == constants.GATES_CHAR:
                        self.gates.append(Position(num_line, num_column))
                    elif carac == constants.WALL_CHAR:
                        self.walls.append(Position(num_line, num_column))
                    elif carac == constants.START_CHAR:
                        self.start = Position(num_line, num_column)
                        self.gates.append(Position(num_line, num_column))
                    elif carac == constants.ARRIVAL_CHAR:
                        self.arrival = Position(num_line, num_column)
                        self.gates.append(Position(num_line, num_column))
                    self.width = num_column
                    self.height = num_line

    def generate_item_position(self):
        '''Manage the objects generating at a random position
        with random module.
        The method generates the position of the objects by randomly
        selecting 3 crossing positions avoiding the starting position.
        '''
        self.item = random.sample(
            set(self.gates)-{self.start, self.arrival}, 3)
        return self.item

    def display(self):
        '''Manages the labyrinth display.
        The representation of the elements is done from the settings.py file.
        To display the elements the method checks whether the position
        of the elements corresponds to a wall, a passage,
        an object or hero.
        '''
        for num_line in range(self.height+2):
            for num_column in range(self.width+2):
                if num_column == 15:
                    print()
                if Position(num_line, num_column) in self.item:
                    if Position(num_line, num_column) == self.hero.position:
                        print(self.hero.name, end="")
                    elif Position(num_line, num_column) in self.hero.inventory:
                        print(constants.GATES_REP, end="")
                    else:
                        print(constants.OBJ_REP, end="")
                elif Position(num_line, num_column) == self.arrival:
                    if Position(num_line, num_column) == self.hero.position:
                        print(self.hero.name, end="")
                    else:
                        print(constants.ARRIVAL_REP, end="")
                elif Position(num_line, num_column) == self.hero.position:
                    print(constants.CHAR_REP, end="")
                elif Position(num_line, num_column) in self.gates:
                    print(constants.GATES_REP, end="")
                elif Position(num_line, num_column) in self.walls:
                    print(constants.WALL_REP, end="")
