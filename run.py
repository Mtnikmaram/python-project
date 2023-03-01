from random import randint

scores = {"computer": 0 , "user": 0}

class board
    """ this is for the main board size and the ships"""
    def __init__(self, size , ship_num , name, type):
        self.size = size
        self.ship_num = ship_num
        self.name = name
        self.board = [["." for x in range(size)] for y in range(size)]
        self.type = type
        self.guesses = []
        self.ship = []

    def print(self) :
        for row in self.board :
            print(" ". join(row))

    def guesses(self, x , y):
        self.guesses.append((x , y))
        self.board[x][y]= "X"

        if (x ,y) in self.ship :
            self.board[x][y] = "x"
            return "Hit"
        else:
            return "Miss"
    
    
