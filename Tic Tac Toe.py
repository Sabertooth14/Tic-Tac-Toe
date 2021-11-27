#!/usr/bin/env python
# coding: utf-8

# TIc TAc TOe game 

# In[1]:


#displayiing the board
from IPython.display import clear_output

def display_board(game_board):
    clear_output()
    print(board[7]+ "|" +str(board[8])+ "|" +board[9])
    print('------')
    print(board[4]+ "|" +str(board[5])+ "|" +board[6])
    print('------')
    print(board[1]+ "|" +str(board[2])+ "|" +board[3])
    


# In[2]:


board=[" "]*10
display_board(board)
type(board)


# In[3]:


def user_choice():
    choice= input("chose X or O: ").upper()
    if choice!='X' and choice!='O':
        print("Wrong Choice")
        user_choice()
    else:
        return choice
        
                


# In[4]:


user_choice()


# In[5]:



#taking input from the user

def user_input():
    position= 99
    while(position<0 or position>9):
            position= int(input("Enter a number between 0-9: ")) 
            if position>0 or position<9:
                 return position
            else:
                print("Wrong input.. Please try again")
                position= int(input("Enter a number between 0-9: ")) 
            


# In[6]:


user_input()


# In[7]:


def win_check(board,choice):
    
    return ((board[7] == choice and board[8] == choice and board[9] == choice) or # across the top
    (board[4] == choice and board[5] == choice and board[6] == mark) or # across the middle
    (board[1] == choice and board[2] == choice and board[3] == choice) or # across the bottom
    (board[7] == choice and board[4] == choice and board[1] == choice) or # down the middle
    (board[8] == choice and board[5] == choice and board[2] == choice) or # down the middle
    (board[9] == choice and board[6] == choice and board[3] == choice) or # down the right side
    (board[7] == choice and board[5] == choice and board[3] == choice) or # diagonal
    (board[9] == choice and board[5] == choice and board[1] == choice)) # diagonal


# In[8]:


def space_check(board,position):
    return board[position]==''


# In[9]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return True
    return False


# In[10]:


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[11]:


def replay():
    play= input("Do u wnat to play another game......Enter Yes or No: ")
    return play== 'Yes'


# In[12]:


print("Welcome to Tic Tac Toe")


while True:
    board=[" "]*10
    turn = choose_first()
    print(turn + "will go first")
    play_game= input("Ready to play? y or n")
    if play_game== 'y':
        True
    else:
        False
    
    
    while play_game:
        if turn == 'Player 1':
            display_board(board)
            your_choice = user_choice()
            your_input = user_input()
            board[your_input] = your_choice
        
            if win_check(board,your_choice):
                diplay_board(board)
                print('Congratulations! You have won the game!')
                play_game = False
        
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME!")
                    play_game = False
                else:
                    turn = "Player 2" 
        
        else:
            display_board(board)
            your_choice = user_choice()
            your_input = user_input()
            board[your_input] = your_choice
        
            if win_check(board,your_choice):
                display_board(board)
                print('Congratulations! You have won the game!')
                play_game = False
        
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME!")
                    play_game = False
                else:
                    turn = "Player 1" 
    
    
    if not replay():
        break


# In[13]:


print(type(board[3]))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




