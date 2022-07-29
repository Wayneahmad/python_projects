import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock, paper, scissors]
print("\nWelcome to Rock, Paper, Scissors\n")
user_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#score = 0
#computer_score = 0
if user_choice >= 3 or user_choice < 0:
        print("This is an invalid number, you lose!!")
        #computer_score += 1
else:
        print(game_images[user_choice])


        computers_choice = random.randint(0, 2)
        print (f"Computers chose {computers_choice}")
        print(game_images[computers_choice])


        if user_choice >= 3 or user_choice < 0:
            print("This is an invalid number, you lose!!")
        elif user_choice == 0 and computers_choice == 2:
            print("You win!!")    
        elif computers_choice == 0 and user_choice == 2:
            print("You lose!!")
        elif user_choice == 1 and computers_choice == 2:
            print("You lose!!")
        elif computers_choice == 1 and user_choice == 2:
            print("You win!!")
        elif user_choice == 1 and computers_choice == 0:
            print("You win!!")    
        elif user_choice == 0 and computers_choice == 1:
            print("You lose!!")
        elif user_choice == computers_choice:
            print("It's a draw")            
