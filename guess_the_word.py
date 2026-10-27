# Ryan Anderson
# CIS256 Fall 2026
# Programming Assignment 4

import random

# predefined list the game picks its secret word from
WORDS = ["python", "variable", "function", "loop", "string", "list",
         "dictionary", "boolean", "integer", "program"]

# wrong guesses allowed before the player loses
MAX_ATTEMPTS = 6


def choose_word(word_list):
    # picks one random word so the answer is different each game
    return random.choice(word_list)


def display_word(word, guessed_letters):
    # shows correct guesses in place and an underscore for every hidden letter
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def check_guess(word, guess):
    # a guess is correct if the letter appears anywhere in the word
    return guess in word


def is_word_guessed(word, guessed_letters):
    # the word is solved only when every letter has been guessed
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True


def play_game():
    word = choose_word(WORDS)
    guessed_letters = []
    attempts_left = MAX_ATTEMPTS

    print("Welcome to Guess the Word!")

    # keep going until the word is solved or the attempts run out
    while attempts_left > 0 and not is_word_guessed(word, guessed_letters):
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts_left)
        guess = input("Guess a letter: ").strip().lower()

        # reject anything that is not exactly one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            # repeats are ignored so they do not cost an attempt
            print("You already guessed that letter.")
        else:
            guessed_letters.append(guess)
            if check_guess(word, guess):
                print("Good guess!")
            else:
                attempts_left -= 1
                print("Incorrect guess.")

    if is_word_guessed(word, guessed_letters):
        print("\nCongratulations! You guessed the word: " + word)
    else:
        print("\nOut of attempts! The word was: " + word)


if __name__ == "__main__":
    play_game()
