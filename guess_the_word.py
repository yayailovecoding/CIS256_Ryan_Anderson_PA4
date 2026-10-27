# Ryan Anderson
# CIS256 Fall 2026
# Programming Assignment 4

import random

# predefined list the game picks its secret word from
WORDS = ["python", "variable", "function", "loop", "string", "list",
         "dictionary", "boolean", "integer", "program"]


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
