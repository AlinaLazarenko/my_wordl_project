
"""
random word for every time the program runs +
user input +
use colorama to get colors +
don't accept words that not in dictionary
"""
import random
import time

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def load_words():
    with open('words2.txt') as f:
        return f.read().split()

def get_feedback(secret, guess):
    feedback = []
    for index, letter in enumerate(guess):
        if letter == secret[index]:
            feedback.append(f"{Fore.GREEN + letter + Style.RESET_ALL}")
        elif letter in secret:
            feedback.append(f"{Fore.YELLOW + letter + Style.RESET_ALL}")
        else:
            feedback.append(f"{Fore.RED + letter + Style.RESET_ALL}")
    return feedback

def is_valid_word(word, valid_words):
    return word in valid_words

def play_wordle():
    words = load_words() 
    secret_word = random.choice(words)
    attempts = 6
    # print(secret_word)# to recheck the correct word
    print("Welcome to Wordle!")
    print("Guess the 5-letter word. You have 6 attempts.")
    print(
        f"If the letter is {Fore.GREEN}Green{Style.RESET_ALL}, it is in the word and in the right position."
    )
    print(
        f"If the letter is {Fore.YELLOW}Yellow{Style.RESET_ALL}, it is in the word but in wrong position. "
    )
    print(
        f"If the letter is {Fore.RED}Red{Style.RESET_ALL}, it is not in the word."
    )

    start_time = time.time()

    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").lower()

        while True:  # Loop until valid input is provided
            if len(guess) != 5 or any(char.isdigit() for char in guess):
                print("Enter a 5-letter word without any digits:")
                guess = input(f"Attempt {attempt + 1}/{attempts}: ").lower()
            if not is_valid_word(guess, words):
                print("Word is not in our list. Please enter another 5-letter word:")
                guess = input(f"Attempt {attempt + 1}/{attempts}: ").lower()
            else:
                break  # Exit the loop if the input is valid

        if guess == secret_word:
            end_time = time.time()
            duration = end_time - start_time
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            print(
                f"Congratulations! You've guessed the word '{Fore.GREEN + secret_word + Style.RESET_ALL}' correctly!"
            )
            print(
                f"You took {minutes} minutes and {seconds} seconds to guess the word."
            )
            break
        feedback = get_feedback(secret_word, guess)
        print(" ".join(feedback))
        print()
        # for message in feedback:
        #     print(message)
        if attempt == attempts - 1:
            end_time = time.time()
            duration = end_time - start_time
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            print(
                f"Sorry, you've run out of attempts. The word was '{secret_word}'."
            )
            print(
                f"You took {minutes} minutes and {seconds} seconds to complete the game."
            )

play_wordle()
