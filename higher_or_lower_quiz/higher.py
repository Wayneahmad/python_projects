import random
import os
from re import A
from art import logo, vs
from game_data import data

def format(account):
    account_name = account["name"]
    account_disc = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_disc}, from {account_country}")



def check_answer(guess, a_followers_account, b_followers_account):
    """use if statment to check if users answer is correct"""
    if a_followers_account > b_followers_account:
        return guess == "a"
    else:
        return guess == "b"


game_is_finished = False

#print logo

b = random.choice(data)     
   
score = 0

while game_is_finished == False:
    print (logo)
    print(f"You're current score is {score}")
    a = (b)
    b = random.choice(data)
    while a == b:
        b = random.choice(data)


    print(f"Compare A: {format(a)}")  
    print (vs)
    print(f"Against B: {format(b)}")  

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = a["follower_count"]
    b_followers = b["follower_count"]

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
        os.system("clear")
    else:
        game_is_finished = True
        print(f"You're wrong! Final score {score}")