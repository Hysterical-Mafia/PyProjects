#Number Guessing Game
import random

#Player is asked to play a game
play_game = input("Would you like to guess the number I have in mind? Yes or No")
play_game = play_game.strip().lower()

def start_game():
    if play_game == "yes":
        print("Great! The number I have in mind is a number from 1 to 100 !!")
        #generates a random number
        number_to_guess = random.randint(1,100)
    #asks user for guess, if guess is not equal to random number than print try again
        user_guess = int(input("Make a Guess!"))
        while user_guess != number_to_guess:
            if user_guess < number_to_guess:
                print("Incorrect! Guess Higher")
                user_guess = int(input("Make another Guess!"))
            if user_guess < number_to_guess:
                print("Incorrect! Guess Higher")
                user_guess = int(input("Make another Guess!"))
            if user_guess > number_to_guess: 
                print("Incorrect! Guess Lower")
                user_guess = int(input("Make another Guess!"))
            if user_guess == number_to_guess:
                play_again = input("Congratulations! You have guessed my number, would you like to play again?")
                play_again = play_again.lower().strip()
                if play_again == "yes":
                    start_game()
                else:
                    print("Ok, maybe next time")
    else:
        print("Ok, maybe next time")
        
start_game()

