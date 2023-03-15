from random import randint

Hidden_Pattern = [[' ']*5 for x in range(5)]
Guess_Pattern = [[' ']*5 for x in range(5)]

let_to_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}


def print_board(board):
    print(' A B C D E ')
    print(' **********')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


def get_ship_location():
    """Enter the row number between 1 to 5"""
    row = input('Please enter a ship row 1-5 \n').upper()
    while row not in '12345':
        print("Please enter a valid row ")
        row = input('Please enter a ship row 1-5 \n')
    """Enter the Ship column from A TO E"""
    column = input('Please enter a ship column A-E \n ').upper()
    while column not in 'abcde':
        print("Please enter a valid column ")
        column = input('Please enter a ship column A-E \n ')
    return int(row)-1, let_to_num[column]


def create_ships(board):
    """Function that creates the ships"""
    for ship in range(3):
        ship_r, ship_cl = randint(0, 4), randint(0, 4)
        while board[ship_r][ship_cl] == 'X':
            ship_r, ship_cl = randint(0, 4), randint(0, 4)
        board[ship_r][ship_cl] = 'X'


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


create_ships(Hidden_Pattern)
print('Welcome to Battleship')
turns = 10
while turns > 0:
    print_board(Guess_Pattern)
    row, column = get_ship_location()
    if Guess_Pattern[row][column] == '-':
        print(' You already guessed that ')
    elif Hidden_Pattern[row][column] == 'X':
        print(' Congratulations you have hit the battleship ')
        Guess_Pattern[row][column] = 'X'
        turns -= 1
    else:
        print('Sorry,You missed')
        Guess_Pattern[row][column] = '-'
        turns -= 1
    if count_hit_ships(Guess_Pattern) == 3:
        print("Congratulations you have sunk all the battleships ")
        break
    print(' You have ' + str(turns) + ' turns remaining ')
    if turns == 0:
        print('Game Over ')
        break
