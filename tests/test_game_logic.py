from logic_utils import (
    check_guess,
    get_hint_message,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_guess_compared_as_numbers_not_text():
    # As text "9" > "50", but as numbers 9 is lower than 50
    assert check_guess(9, 50) == "Too Low"
    assert check_guess(100, 50) == "Too High"

def test_range_for_difficulty():
    # Each difficulty should have a wider range than the one before it
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_range_for_unknown_difficulty_uses_normal():
    assert get_range_for_difficulty("Impossible") == (1, 50)

def test_parse_valid_guess():
    assert parse_guess("42") == (True, 42, None)

def test_parse_guess_ignores_surrounding_spaces():
    assert parse_guess("  7 ") == (True, 7, None)

def test_parse_empty_guess():
    assert parse_guess("") == (False, None, "Enter a guess.")
    assert parse_guess("   ") == (False, None, "Enter a guess.")
    assert parse_guess(None) == (False, None, "Enter a guess.")

def test_parse_guess_rejects_decimals_and_text():
    assert parse_guess("3.7") == (False, None, "Enter a whole number.")
    assert parse_guess("abc") == (False, None, "Enter a whole number.")

def test_parse_guess_rejects_out_of_range():
    assert parse_guess("0", 1, 50) == (False, None, "Enter a number between 1 and 50.")
    assert parse_guess("51", 1, 50) == (False, None, "Enter a number between 1 and 50.")

def test_parse_guess_accepts_range_edges():
    assert parse_guess("1", 1, 50) == (True, 1, None)
    assert parse_guess("50", 1, 50) == (True, 50, None)

def test_hint_points_the_right_way():
    # A guess that is too high should tell the player to go lower, and vice versa
    assert "LOWER" in get_hint_message("Too High")
    assert "HIGHER" in get_hint_message("Too Low")
    assert "Correct" in get_hint_message("Win")

