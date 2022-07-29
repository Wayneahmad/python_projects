from random import randint
from art import logo
import os
 
def restart():
    result = input("\nDo you want to play again? 'Yes' or 'No': ").lower()
    if result == 'yes':
        os.system("clear")
        play()
    else:
        exit()    
 
def play():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        num_of_attempts = 10
    elif difficulty == 'hard':
        num_of_attempts = 5
    while num_of_attempts != 0:
        print(f"\nYou have {num_of_attempts} attempts remaining\n")  
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high")
            num_of_attempts -= 1
        elif guess < number:
            print("Too low")
            num_of_attempts -= 1
        else:
            print (f"You got it! The answer was {guess}.")
            restart() 
        if num_of_attempts > 1:
            print("Guess again")

    print (f"You've run out of guesses, you lose!\nThe number was {number}")
    restart()
 
play()
 