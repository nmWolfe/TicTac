""" 
My attempt at creating a (over)simple(fied) game of Tic Tac Toe 
"""
import os
from time import sleep 

""" Setting the initial game board """
game = {'a':
    [' ',' ',' '],
    'b':
    [' ',' ',' '],
    'c':
    [' ',' ',' '],
    }

def new_board():
    """ To clear the board """
    game = {'a':
        [' ',' ',' '],
        'b':
        [' ',' ',' '],
        'c':
        [' ',' ',' '],
        }

def example_board():

    """ This is to give a clear idea of the layout of the board """

    print("This is what our game board will look like:\n")

    columns = ['1','2','3']
    
    print(" ---Columns--- ")
    print(columns)
    print("    -------    ")
    print(f"{game['a']} - Row 1\n{game['b']} - Row 2\n{game['c']} - Row 3")

"""
Give an example of a winning board
"""

def example_win():

    print("\nAnd THIS is what a win looks like. Three in a row: \n")
    
    """Laying out the display boards """

    example_win_X = {'a':
        ['X','X','X'],
        'b':
        [' ',' ',' '],
        'c':
        [' ',' ',' '],
    } 
    
    example_win_O = {'a':
        ['O',' ',' '],
        'b':
        [' ','O',' '],
        'c':
        [' ',' ','O'],
    } 

    """ Displaying the boards """

    print(f"{example_win_X['a']}\n{example_win_X['b']}\n{example_win_X['c']}\n")
    print(f"{example_win_O['a']}\n{example_win_O['b']}\n{example_win_O['c']}\n")

""" 
Winning Position Check
"""

def win_check(board,player):

    """ Checking for a WINNER by seeing if player marker is in corresponding spots """

    # Horizontal Win #
    return (
    (game['a'][0] == player and game['a'][1] == player and game['a'][2] == player) or
    (game['b'][0] == player and game['b'][1] == player and game['b'][2] == player) or
    (game['c'][0] == player and game['c'][1] == player and game['c'][2] == player) or
    # Vertical Win #
    (game['a'][0] == player and game['b'][0] == player and game['c'][0] == player) or
    (game['a'][1] == player and game['b'][1] == player and game['c'][1] == player) or
    (game['a'][2] == player and game['b'][2] == player and game['c'][2] == player) or
    # Crossways Win #
    (game['a'][0] == player and game['b'][1] == player and game['c'][2] == player) or
    (game['a'][2] == player and game['b'][1] == player and game['c'][0] == player)
    )

"""
Checking empty spaces
"""

############## NEED TO FIX THIS 

def choice_check(board,row,col):

    """ This will return a bool check if space is empty """

    if row == 1:
        row = 'a'
    if row == 2:
        row = 'b'
    if row == 3:
        row = 'c'
    
    return board[row][col] == ' '

"""
Amending the scoreboard
"""

def score_board(r,c,p):
    
    # Need to input some check here for whether an X or O already in postion #

    if r == 1:
        #while game['a'][c] == ' ':
            game['a'].pop(c-1)
            game['a'].insert(c-1,p)
            
    elif r == 2:
        #while game['b'][c] == ' ':
            game['b'].pop(c-1)
            game['b'].insert(c-1,p)

    elif r == 3:
        #while game['c'][c] == ' ':
            game['c'].pop(c-1)
            game['c'].insert(c-1,p)
            

    print(f"{game['a']}\n{game['b']}\n{game['c']}")

"""
Player Turns
""" 

def player_choice_x(player):
    r = 0
    c = 0
    choice_range = ['1','2','3']
    while choice_check:
        r = input(f"Ok {player} (X), please pick a row: 1, 2 or 3 ")
        while r not in choice_range:
            r = input("Hmm, not in the range.. try again: ")
            
        c = input("Great, now pick a column: 1, 2 or 3 ")
        while c not in choice_range:
            c = input("Hmm.. again, not in the range. Try again: ")
        
        p = 'X'
        
        score_board(int(r),int(c),p)
        break

def player_choice_o(player):
    r = 0
    c = 0
    choice_range = ['1','2','3']
    while choice_check:
        r = input(f"Ok {player} (O), please pick a row: 1, 2 or 3 ")
        while r not in choice_range:
            r = input("Hmm, not in the range.. try again: ")
            
        c = input("Great, now pick a column: 1, 2 or 3 ")
        while c not in choice_range:
            c = input("Hmm.. again, not in the range. Try again: ")
        
        p = 'O'
    
        score_board(int(r),int(c),p)
        break

"""
Making a replay function
"""

def replay():
    """ Will return TRUE if 'Y' """
    return input("Do you want to play again? Y/N: ").lower().startswith('y')

"""
Anticipation Function
"""

def aniticipation():

    """ Silly func to add suspence.. or not """

    build_up = ['.','..','...']
    for dot in build_up:
        print(dot)
        sleep(1)

"""
Actual game assembly and logic
"""

def Tic_Tac_Toe():

    print("Welcome to a simple game of Tic Tac Toe.\n")

    run = ''

    while run != 'n':

        """ This deals with wrong inputs (and right inputs) """

        run = input("Would you like to play? 'Y' / 'N' \n") 

        if run.lower() == 'y':
            game_on = True
            example_board()
            example_win()
            break
            
        else:
            if run.lower() == 'n':
                game_on = False
            else:
                run = input("Hmm.. Please try that again. 'Y' / 'N' \n")
                game_on = True
                break
            
    # Running the game

    while game_on:

        print("Okay, time to find out who is playing today: \n")

        player_one = input("Player one, please enter your name: ")
        print(f"\nOoh, {player_one} is a lovely name.\n")

        player_two = input("Player two, please enter your name: ")
        print(f"\nHey! I love the name {player_two}")
        
        print(f"\nOkay {player_one} and {player_two},\n")

        aniticipation()
        
        print("\nLets play\n")
        sleep(1)
        os.system('clear')

        playing = True

        while playing:

            player_choice_x(player_one)

            if win_check(score_board,'X'):
                print(f"{player_one} is our winner!\n")
                if replay():
                    os.system('clear')
                    break
                else:
                    game_on = False
                    break

            
            player_choice_o(player_two)
            
            if win_check(score_board,'O'):
                print(f"{player_two} is our winner!\n")
                if replay():
                    os.system('clear')
                    break
                else:
                    game_on = False
                    break

    while not game_on:
        os.system('clear')
        print("Thank you for playing.. or not playing.\n")
        aniticipation()
        print("\nGoodbye\n")
        break

Tic_Tac_Toe()

readme = """
A simple game of Tic Tac Toe, that I started but haven't quite finished due to a few bugs.
This was my first attempt, and I will return to this at a later date to fix the few remaining issues.
"""
with open('README.txt', 'w') as file:
    file.write(readme)
