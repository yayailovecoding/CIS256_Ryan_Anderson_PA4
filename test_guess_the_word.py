# Ryan Anderson
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import (WORDS, choose_word, display_word, check_guess,
                            is_word_guessed)


def test_choose_word_comes_from_list():
    # run it many times because the choice is random
    for _ in range(50):
        assert choose_word(WORDS) in WORDS


def test_display_word_hides_unguessed_letters():
    assert display_word("python", []) == "_ _ _ _ _ _"


def test_display_word_reveals_correct_guess():
    assert display_word("python", ["p", "o"]) == "p _ _ _ o _"


def test_display_word_reveals_every_repeated_letter():
    # a letter that appears twice must show in both spots
    assert display_word("loop", ["o"]) == "_ o o _"


def test_check_guess_correct_and_incorrect():
    assert check_guess("python", "y") is True
    assert check_guess("python", "z") is False


def test_is_word_guessed():
    assert is_word_guessed("loop", ["l", "o", "p"]) is True
    assert is_word_guessed("loop", ["l", "o"]) is False
