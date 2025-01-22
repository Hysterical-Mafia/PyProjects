#hangman game, functions only, simple layout
import random
import nltk
from nltk.corpus import words
nltk.download('words')

def play_hangman():
    play_the_game = input("Would you like to play hangman?\nPress '1' to continue\n")
    if play_the_game == "1":
        print("Ok, lets start")
        chosen_word = rand_word()
        guessed_letters = set()
        attempts = 6
        
        while attempts > 0 and not is_word_guess(chosen_word, guessed_letters):
            print("\n" + display_word(chosen_word, guessed_letters))
            print(f"Remaining Attempts: {attempts}")
            guess = get_user_letter(guessed_letters)
            
            if guess in chosen_word:
                print(f"Good Guess! ' {guess}' is in the word.")
                guessed_letters.add(guess)
            else:
                print(f"Wrong! '{guess}' is not in the word")
                attempts -= 1
                
            if is_word_guess(chosen_word, guessed_letters):
                print(f"\nCongratulations! You guessed the word: {chosen_word}")
        else:
                print(f"\nGame over! The word was: {chosen_word}")

    else:
        print("Ok, goodbye")
    
    
def rand_word():
    word_list = words.words()
    return random.choice(word_list).lower()

                    
def get_user_letter(guessed_letters):
    while True:  
        user_guess = input("Choose one letter: ").lower()
        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in guessed_letters:
                print(f"You have already guessed '{user_guess}'. Try Again.")
            else:
                return user_guess
        else:
            print("Invalid Input. Please enter a single alphabetic character")  

def display_word(chosen_word, user_guess):
    display = ""
    for letter in chosen_word:
        if letter in user_guess:
            display += letter
        else:
            display += "_"
    return display    

def is_word_guess(chosen_word, guessed_letters):
    return all(letter in guessed_letters for letter in chosen_word)
      
play_hangman()



