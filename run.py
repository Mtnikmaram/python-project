from random import randint

scores = {"computer": 0 , "user": 0}

class board :
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

    def guess(self, x , y):
        self.guesses.append((x , y))
        self.board[x][y]= "X"

        if (x ,y) in self.ship :
            self.board[x][y] = "x"
            return "Hit"
        else:
            return "Miss"
    
    def add_ship(self , x , y, type="computer"):
        if len(self.ship) >= self.ship_num :
            print ("Error : you cannot add any more ships!")
        else :
            self.ship.append((x , y))
            if self.type == "player":
                self.board[x][y] = "$"
def random_point(size):
    """ function to return a random integer between 0 and size"""
    return randint(0 , size -1)

def valid_coordinates (x ,y ,board):


def populate_board(borad):


def make_guess(board):


def play_game(computer_board , user_board):



def new_game():
    """ starts the new game """
    size = 5
    ship_num = 4
    scores["computer"] = 0
    scores["user"] = 0
    print("-" * 35)
    print("Welcome to my Battelship game")
    print(f"Board Size: {size}. Number of ships: {ship_num}")
    print("Top left corner is row: 0 , col : 0")
    print("-" * 35)
    user = input("please enter your name : \n")
    print("-" * 35)

    computer_board = board(size , ship_num, "computer" , type = "computer")
    player_board = board(size , ship_num , player_name , type = "player")

    for - in range(ship_num):
        populate_board(player_board)
        populate_board(computer_board)
    play_game(computer_board , player_board)

new_game()