'''
board
display board
play game
handel turn
les
ckeck win
    ->check rows
    ->check columns
    ->check diagomals
check tie
flip player

'''

board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_',]

game_still_going = True
winner = None
current_player = 'X'
p1 = 'Player 1'
p2 = 'Player 2'
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def play_game():
    
    print('Player 1 = X')
    print('Player 2 = O\n')

    display_board()
    global p1   
    global p2
    while game_still_going:
        handel_turn(current_player)

        check_if_game_over()

        flip_player()
    
    if winner == 'X' or winner == 'O':
        if winner == 'X':
            print(p1 + ' won.')
        elif winner == 'O':
            print(p2 + ' won.')
    
    elif winner == None :
        print('Tie.')

def handel_turn(player):
    global current_player
    global p1
    global p2
    
    if current_player == 'X': 
       position = input(p1 + " chosse a position from 1-9:")
    
    elif current_player == 'O': 
       position = input(p2 + " chosse a position from 1-9:")
    
    valid = False

    while not valid:
        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input('Invalid input.Chosse a position from 1-9:')
    
        position = int(position) - 1

        if board[position] == '_':
            valid = True
        else:
            print("You can't go there. Go again.")
    
    board[position] = player
    display_board()
   
def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_colums()
    # check diagomals
    diagomal_winner = check_diagomals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagomal_winner:
        winner = diagomal_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != '_'
    row_2 = board[3] == board[4] == board[5] != '_'
    row_3 = board[6] == board[7] == board[8] != '_'
    
    if row_1 or row_2 or row_3:
        game_still_going = False
    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    
    elif row_3:
        return board[6]
    return

def check_colums():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != '_'
    column_2 = board[1] == board[4] == board[7] != '_'
    column_3 = board[2] == board[5] == board[8] != '_'
    
    if column_1 or column_2 or column_3:
        game_still_going = False
    
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    
    elif column_3:
        return board[2]
    return

def check_diagomals():
    global game_still_going

    diagomals_1 = board[0] == board[4] == board[8] != '_'
    diagomals_2 = board[6] == board[4] == board[2] != '_'
    
    if diagomals_1 or diagomals_2:
        game_still_going = False
    
    if diagomals_1:
        return board[0]
    
    elif diagomals_2:
        return board[6]
    
    return

def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False

    return

def flip_player():
    global current_player
    
    if current_player == 'X':
        current_player = 'O'
    
    elif current_player == 'O':
        current_player = 'X'
    
    return current_player


play_game() 