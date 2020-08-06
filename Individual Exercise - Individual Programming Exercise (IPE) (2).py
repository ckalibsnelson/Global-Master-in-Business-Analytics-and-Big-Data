#!/usr/bin/env python
# coding: utf-8

# # STATISTICAL PROGRAMMING – PYTHON Individual Programming Exercise (IPE)

# # Ckalib S. Nelson

# ## Functions

# ### Importing Linear Congruence

# In[1]:


#Linear congruence function per video: https://www.youtube.com/watch?v=RX51zO5G0n4

#For the random throw, proceed as follows. Generate a random number using the linear congruences method (see Appendix).
#If the random number is less than or equal to 2*32/2 (=2*31), the computer will play 0. Otherwise, it will play 1. 
#To facilitate the structure of your program, generate a new random number at the beginning of each move, and use it 
#only if necessary according to the rules above. If the random number is not used it will be discarded at the 
#beginning of the next move when a new number is generated.
#Only when you initialize your python game, it will require an initial seed x0, manually choose an integer value of 
#your choice between 1 and 2*31.

#def linear_congruence(xi):
    #""" Function to calculate linear congruences value and computer bet """
    #a = 22695477
    #b = 1
    #m = 2**32
    #xi_plus_1 = (a * xi + b) % m
    #if xi_plus_1 <= 2**31:
        #comp_move = 0
    #else:
        #comp_move = 1
    #return comp_move, xi_plus_1


# In[2]:


import os


# In[3]:


print(os.path)


# In[4]:


import mypackage.demo as lc


# In[5]:


print(lc)


# ### Throws

# In[6]:


#Function to keep track of the current and previous bids and accumulate counts per throw type
def throws(player_move1,player_move,throw_list):
    if player_move1 == 0 and player_move == 0:
        throw_list[0]+=1
    if player_move1 == 1 and player_move == 0:
        throw_list[1]+=1
    if player_move1 == 0 and player_move == 1:
        throw_list[2]+=1
    if player_move1 == 1 and player_move == 1:
        throw_list[3]+=1
    return(throw_list)


# ### Computer Move Difficult

# In[7]:


#Function that yields what the computer bid should be given the current and previous bids from the human
def computer_move_difficult(throw_list,xi): #t represents the throw # and throw_list = [throw00,throw01,throw10,throw11]
    throw00=throw_list[0]
    throw01=throw_list[1]
    throw10=throw_list[2]
    throw11=throw_list[3]
    if player_move == 0 and throw10 > throw00:#If the player's last throw was 0:
        comp_move_difficult = 1 #If throw10 > throw00: then the computer chooses 1
    elif player_move == 0 and throw10 < throw00:
        comp_move_difficult = 0 #If throw10 < throw00: then the computer chooses 0
    elif player_move == 0 and throw10 == throw00:
        comp_move_difficult = lc.linear_congruence(xi) #If throw10 = throw00: then the computer chooses randomly 0 or 1.
    elif player_move == 1 and throw11 > throw01:#If the player's last throw was 1:
        comp_move_difficult = 1 #If throw11 > throw01: then the computer chooses 1
    elif player_move == 1 and throw11 < throw01:
        comp_move_difficult = 0 #If throw11 < throw01: then the computer chooses 0
    elif player_move == 1 and throw11 == throw01:
        comp_move_difficult = lc.linear_congruence(xi) #If throw11 = throw01: then the computer chooses randomly 0 or 1.
    return(comp_move_difficult,xi)


# ## Game

# In[8]:


## Welcome
#1. Create opening message
print('Welcome to Human Behavior Prediction by Ckalib S. Nelson')
while True:

#Choose difficulty level. Either 1 or 2. If neither, this code ensures that either choice is made

#Extra participation point - if your code never breaks whatever the input entered by the user (if it is not an allowed
#number, if it is text, if it is empty, if it is float).
    while True:    
        try :
            select_difficulty = int(input("""Choose the type of game (1:Easy; 2:Dificult):"""))
            if select_difficulty == 2:
                break
            elif select_difficulty == 1:
                break
            else:
                print("Unfortunately, you're input is invalid. Please choose either 1 or 2")
        except:
            print("Please choose either 1 or 2")
        
#Decide number of moves. If input is invalid, this code ensures that the humann chooses correctly

#Extra participation point - if your code never breaks whatever the input entered by the user (if it is not an allowed
#number, if it is text, if it is empty, if it is float).
    while True:
        try:
            moves = int(input("Enter the number of moves: "))
            if moves > 0:
                break
            else: print("Unfortunately, you're input is invalid. Please choose a number above 0.")
        except:
            print("UUnfortunately, you're input is invalid. Please choose a number above 0.")
        
#In "easy" mode, the computer has no learning, i.e., all computer throws are random, using the method of 
#linear congruences. If the random number generated is less than or equal to 232/2 (=231), the computer will choose 0 
#and otherwise, 1.
    if select_difficulty == 1:#easy mode
        MS = 0
        PS = 0
        xi = 1234
        for turn in range(moves):
            print("--")
            while True:
                try:
                    player_move = int(input("Choose your number %s(O or 1):" % (turn+1)))
                    if  player_move == 0:
                        break
                    if  player_move == 1:
                        break
                    else: print("Unfortunately, you're input is invalid. Please choose 0 or 1. ")
                except:
                    print("Unfortunately, you're input is invalid. Please choose 0 or 1. ")
            computer_move, xi = lc.linear_congruence(xi)
            if player_move == computer_move:
                MS = MS + 1
                print("player = 0 machine = 0 - Machine wins!")
                print("You: %d Computer: %d" % (PS,MS))
            else:
                PS = PS + 1
                print("player = 1 machine = 0 - Player wins!")
                print("You: %d Computer: %d" % (PS,MS))
            print('Player ' + '*'*PS)
            print('Computer: ' + '*' * MS)
        
#In “difficult” mode, the computer will use the learning method described above.
    if select_difficulty == 2: #"difficult" mode
        xi = 1234
        MS = 0
        PS = 0
        player_move1=0
        throw_count_list=[0,0,0,0]
        for turn in range(moves):
            print("--")
            while True:
                try:
                    player_move = int(input("Choose your number %s(O or 1):" % (turn+1)))
                    if  player_move == 0:
                        break
                    if  player_move == 1:
                        break
                    else: print("Unfortunately, you're input is invalid. Please choose 0 or 1. ")
                except:
                    print("Unfortunately, you're input is invalid. Please choose 0 or 1. ")
            if(turn==0): #If there has not been a turn yet, apply throws function to throw count list and assign the player move to player_move1
                computer_move = lc.linear_congruence(xi) #For the first turn, the computer must go random using the linear_congruence function
                player_move1 = player_move
            else:
                throw_count_list = throws(player_move1,player_move,throw_count_list) #Apply throws function to throw count list
                computer_move = computer_move_difficult(throw_count_list,xi)[0] #Apply all moves from the computer from the thorws and computer_move_difficult functions
                player_move1 = player_move
            if player_move == computer_move:
                MS = MS + 1
                print("player = 0 machine = 0 - Machine wins!")
                print("You: %d Computer: %d" % (PS,MS))
            else:
                PS = PS + 1
                print("player = 1 machine = 0 - Player wins!")
                print("You: %d Computer: %d" % (PS,MS))
            print('Player ' + '*'*PS)
            print('Computer: ' + '*' * MS)

#At the end of the game (after the n-th0 round), you must print on the screen who was the winner or if there was a tie.
    if select_difficulty == 1:
        if PS > MS:
            print("Easy game is over, final score: player ", PS, " - ", MS, "computer - You won!")
        elif PS == MS:
            print("Easy game is over, final score: player ", PS, " - ", MS, "computer - No one won!")
        elif PS < MS:
            print("Easy game is over, final score: player ", PS, " - ", MS, "computer - Computer won!")
    else:
        if PS > MS:
            print("Hard game is over, final score: player ", PS, " - ", MS, "computer - You won!")
        elif PS == MS:
            print("Hard game is over, final score: player ", PS, " - ", MS, "computer - No one won!")
        elif PS < MS:
            print("Hard game is over, final score: player ", PS, " - ", MS, "computer - Computer won!")
    print("--")
   
    try :
        play_again = int(input("""Would you like to play again: 1 for Yes, 2 for No: """))
        if play_again == 2:
            print("Thank you for playing my game!")
            break
        else:
            print("Thank you for deciding to play again!")
    except:
        print("Please choose between Y or N")


# In[ ]:




