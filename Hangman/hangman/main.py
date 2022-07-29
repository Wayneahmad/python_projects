def main():
    import random
    import os

    from hangman_art import stages, logo
    from hangman_words import word_list
    #from replit import clear
    
    print(logo) 
    game_is_finished = False
    lives = len(stages) - 1
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    wrong_letters = []
    score = 0
    display = []
    #print (chosen_word)
    for _ in range(word_length):
        display += "_"
    while not game_is_finished:
        guess = input("Guess a letter: ").lower()
        os.system("clear")
        print(logo)
        if guess in display:
            print(f"You've already guessed {guess}")
        for position in range(word_length):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter
        print(f"{' '.join(display)}")

        if guess not in chosen_word:
            print(f"You guessed '{guess}', that's not in the word. You lose a life.")

            lives -= 1
            if lives == 0:
                game_is_finished = True
                print(f"You lose,\nThe word you tried to guess was '{chosen_word}'\n")
                
        if not "_" in display:
            game_is_finished = True
            print("You win.")
                       
        wrong_letters .append(guess)
        print (f"\nGuessed letters = {wrong_letters}")
        print(stages[lives])
    result = input("Play again? Type 'Y' or 'N' ").lower()
    if result == "y":
        os.system("clear")
        main()

    else:
        exit()  
main()          