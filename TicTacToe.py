#!/usr/bin/env python
# coding: utf-8



def display_board(board):
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])




def player_input():
    
    mark = 'no'
    
    while mark not in ['x','o']:
        
        mark=input('Do you wanna be x or o?')
        if mark not in ['x','o']:
            print('Please choose x or o.')
            
    return mark




def place_marker(board, marker, position):

        board[position]=marker




def win_check(board, mark):
    
    for k in (1,4,7):
        if board[k]==board[k+1]==board[k+2]==mark:
            return True
    for l in (1,2,3):
        if board[l]==board[l+3]==board[l+6]==mark:
            return True
    return board[1]==board[5]==board[9]==mark or board[3]==board[5]==board[7]==mark




def space_check(board, position):
    
    return board[position]==''




def full_board_check(board):
    
    for num in range(1,10): 
        if board[num]=='':
            return False
    return True




def player_choice(board,mark):
    
    free = False
    
    choice = 0
    
    text = ''
    
    while text not in ['1','2','3','4','5','6','7','8','9'] or not free:
        
        text= input(f'Place {mark}. Where do you wanna go next? (1-9)')
        
        if text not in ['1','2','3','4','5','6','7','8','9']:
            print('Please intput a digit between 1 and 9.')
        else:
            choice = int(text)
        
        if choice in range (1,9) and not space_check(board,choice):
            
            print('Taken. Choose another position.')
            choice = 0
        else:
            free = space_check(board,choice)
    return choice



def replay():
    
    option = ''
    
    while option not in ['Y','N']:
        option = input('Do you wanna play again? (Y,N)')
    return option=='Y'




while True:
    
    print('Welcome to Tic Tac Toe!')

    first = ''

    second = ''

    board=['','','','','','','','','','']

    turn='player1'
    

    first = player_input()

    if first=='x':
        second='o'
    else:
        second='x'
        
    ready = ''
    
    while ready!='yes':
        ready = input('Are you ready?(yes or no)')
    
    gameinprogress=True


    while gameinprogress:
        #Player 1 Turn
        if turn=='player1':
            position = player_choice(board,first)
            place_marker(board, first, position)
            display_board(board)
            if win_check(board, first):
                print(f'{first} won!')
                break
            if full_board_check(board):
                print('Draw!')
                break
            turn='player2'
        if turn=='player2':
            position = player_choice(board,second)
            place_marker(board, second, position)
            display_board(board)
            if win_check(board, second):
                print(f'{second} won!')
                playing=False
                break
            if full_board_check(board):
                print('Draw!')
                break
            win_check(board, second)
            turn='player1'

        

    if not replay():
        break




