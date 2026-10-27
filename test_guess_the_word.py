# Ryan Anderson
# CIS256 Fall 2026
# Programming Assignment 4

import guess_the_word
from guess_the_word import (WORDS, choose_word, display_word, check_guess,
                            is_word_guessed, play_game)


def fake_inputs(monkeypatch, typed_guesses):
    # replaces input() so the test types each guess for the player
    guesses = iter(typed_guesses)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(guesses))


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


def test_game_win_shows_congratulations(monkeypatch, capsys):
    # force the secret word to "loop" so the guesses are predictable
    monkeypatch.setattr(guess_the_word, "choose_word", lambda words: "loop")
    fake_inputs(monkeypatch, ["l", "o", "p"])
    play_game()
    assert "Congratulations" in capsys.readouterr().out


def test_game_loss_after_too_many_wrong_guesses(monkeypatch, capsys):
    monkeypatch.setattr(guess_the_word, "choose_word", lambda words: "loop")
    # six wrong letters uses up all 6 attempts
    fake_inputs(monkeypatch, ["x", "y", "z", "q", "w", "e"])
    play_game()
    output = capsys.readouterr().out
    assert "Out of attempts" in output
    assert "loop" in output


def test_repeated_guess_does_not_cost_an_attempt(monkeypatch, capsys):
    monkeypatch.setattr(guess_the_word, "choose_word", lambda words: "loop")
    # the repeated "x" should be ignored, not counted as a second miss
    fake_inputs(monkeypatch, ["x", "x", "l", "o", "p"])
    play_game()
    output = capsys.readouterr().out
    assert "already guessed" in output
    assert "Attempts left: 5" in output
    assert "Congratulations" in output
