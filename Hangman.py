import os
import random
from hangman_art import logo, stages
from hangman_words import word_list
def clear_console():
        os.system("cls")
        
chosen_word = random.choice(word_list) #Choose a random word for the word_list
print (logo)

lives = 6  #Lives in the game
EndGame = False
guess_already_enter = [] #List to already entered letters
display = [] #List to add blank spaces
for i in chosen_word: 
        display += "_" 
#Add "_" in the list
while not EndGame :
    guess = str (input ("Guess a letter :")).lower()
    clear_console()
    #User input
    print ("\n")
    guess_already_enter += guess 
    if guess not in chosen_word:
        lives -= 1
        print (stages[lives])
        print ("The letter it's not in the word. You lose a life")
        print ("\n")
        print (f"Your have {lives} lives")
    #If the letter is not in the word, life -1     
    if guess in display:
      print ("You already enter the letter")   
    for position in range (len(chosen_word)):
        letter = chosen_word[position]
        if (letter == guess): 
            display[position] = letter
    #Check if one letter(guess) is in String (chosen_word) and replaces for the blank space                             
    print ('Already enter letter:' + "" + ",".join(guess_already_enter))
    print ("\n")                                 
    print (display)
    print ("\n")    
    #ENDGAME
    if "_" not in display:
        print ("You win")
        EndGame = True
        print ("".join(display))     
    elif lives == 0:
        print ("You lose")
        EndGame = True
