from terminal.labyrinthe import Labyrinth
from terminal.character import Character


class Game:
    '''Class managing the execution of the game'''

    def __init__(self):
        self.labyrinth = Labyrinth("data/mazes/labyrinth1.txt")
        self.perso = Character(self.labyrinth)
        self.user = None
        self.running = False

    def test_move(self):
        '''Method that asks for user input,
        test if this input is valid and
        returns the entered value.
        '''
        self.user = input(
            'In which direction do you want to go ?'
            ' U for Up, D for Down, L for Left, R for Right and Q for quit...').upper()
        while self.user != "R" and\
                self.user != "L" and self.user != "U" and\
                self.user != "D" and self.user != "Q":
            self.user = input(
                'In which direction do you want to go ?'
                ' U for Up, D for Down, L for Left, R for Right and Q for quit...').upper()
            if self.user == "R" and self.user == "L" and\
                    self.user == "U" and self.user == "D" and\
                    self.user != "Q":
                break
            else:
                print("You didn't enter a valid direction")
        return self.user

    def start(self):
        '''Main method of the game. It returns the entire game to the user,
        the display, entry requests, movements and inventory.
        '''
        self.running = True
        while self.running:
            self.labyrinth.display()
            if self.perso.position in self.labyrinth.item:
                if self.perso.position in self.perso.inventory:
                    pass
                else:
                    self.perso.pick_up_object()
            self.test_move()
            if self.user == 'Q':
                self.running = False
            else:
                self.perso.move(self.user)
            if self.perso.position == self.labyrinth.arrival:
                self.perso.fight()
                self.running = False


def main():
    jeu = Game()
    jeu.start()


if __name__ == "__main__":
    main()
