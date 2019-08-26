from IPython.display import clear_output
board = [' ']*9

import random

def display_board(board):
    
    clear_output()
            
    
    print('{0:^8}|{1:^8}|{2:^8}'.format(board[6],board[7],board[8]))
    print('{0:-^8}|{1:-^8}|{2:-^8}'.format('','',''))
    print('{0:^8}|{1:^8}|{2:^8}'.format(board[3],board[4],board[5]))
    print('{0:-^8}|{1:-^8}|{2:-^8}'.format('','',''))
    print('{0:^8}|{1:^8}|{2:^8}'.format(board[0],board[1],board[2]))

    
def player_input():
    while True:
        player1 = input("What would like to play 'O' or 'X'\n").upper()
        if player1 == 'O':
            player2 = 'X'
            break
        elif player1 == 'X':
            player2 = 'O'
            break
        else:
            continue
    return player1,player2


def place_marker(board, marker, position):
    board[position-1] = marker

    
def win_check(board, mark):
    result = False
    for i in range(3):
        if((board[3*i] == board[3*i+1] == board[3*i+2] == mark) or (board[i] == board[3+i] == board[6+i] == mark)):
            result = True
        elif((board[0] == board[4] == board[8] == mark) or (board[2] == board[4] == board[6] == mark)):
            result = True
    return result


def choose_first():
    return 'Player'+ str(random.randint(1,2))

def space_check(board, position):
    return (board[position-1] == ' ')


def full_board_check(board):
    for i in board:
        if(i == ' '):
            return False
    return True


def player_choice(board):
    choice = 0
    while((not space_check(board, choice)) or (choice not in [1,2,3,4,5,6,7,8,9])):
        choice = int(input('Enter a valid number of choice in [0,9]\n'))
    return choice


def replay():
    result = False
    if(input('Do you want to play again? (yes/no)\n').lower() == 'yes'):
        result = True
    return result


print('Welcome to Tic Tac Toe!')


while True:
    
    new_board = [' ']*9
    
    player1, player2 = player_input()
    
    turn = choose_first()
    
    print(turn + ' will go first')
    
    r = input('are you ready?(yes/no)').lower()
    
    if(r == 'yes'):
        ready = True
    else:
        ready = False
    
    
    while ready:
        
        if turn == 'Player1':
            
            #player 1's turn
            display_board(new_board)
        
            position = player_choice(new_board)
        
            place_marker(new_board, player1, position)
        
            if win_check(new_board, player1):
                display_board(new_board)
                print('Congratulations!! player1')
                ready = False
            
            elif (full_board_check(new_board)):
                
                display_board(new_board)
                print('Match Drawn!')
                ready = False
            turn = 'Player2'
        else:
             #player 2's turn
            display_board(new_board)
        
            position = player_choice(new_board)
        
            place_marker(new_board, player2, position)
        
            if(win_check(new_board, player2) == True):
                display_board(new_board)
                print('Congratulations!! player2')
                ready = False
            
            elif (full_board_check(new_board)):
                
                display_board(new_board)
                print('Match Drawn!')
                ready = False
            turn = 'Player1'
    
    if not replay():
        break