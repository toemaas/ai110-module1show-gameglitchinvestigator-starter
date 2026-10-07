# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

**Game purpose:** A Streamlit number-guessing game. The app picks a secret number based on the difficulty, and the player guesses it within a limited number of attempts using "higher/lower" hints. Each guess updates a running score.

**Bugs found:**
- The hints were backwards: guessing too low said "Go LOWER!" and guessing too high said "Go HIGHER!".
- The Normal and Hard ranges were swapped (Normal was 1-100, Hard was 1-50).
- The attempt limits didn't match the difficulty (Easy 6, Normal 8, Hard 5).
- On every other attempt the secret was turned into a string, so guesses were compared as text (for example, "9" > "50").
- Decimal guesses like `3.7` were quietly cut down to `3`, and out-of-range guesses were accepted.
- Scoring was inconsistent: a "Too High" guess gained 5 points on even attempts.
- Pressing Enter does not submit a guess; only the Submit Guess button does.

**Fixes applied:**
- Moved `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` from `app.py` into `logic_utils.py`.
- Set the ranges to Easy 1-20, Normal 1-50, Hard 1-100, and the attempt limits to Easy 5, Normal 6, Hard 8.
- `check_guess` now compares numbers only and returns just the outcome, and a new `get_hint_message` returns the correct hint.
- Removed the code in `app.py` that turned the secret into a string.
- `parse_guess` now accepts only whole numbers inside the difficulty's range.
- `update_score` gives 100 points for a first-try win (10 fewer per later attempt, minimum 10) and takes 5 points for every wrong guess.
- Added `test_range_for_difficulty` to the test suite.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects Hard difficulty; the sidebar shows a range of 1 to 100 and 8 attempts allowed.
2. User opens "Developer Debug Info" and sees the secret is 55.
3. User enters a guess of 40, and the game shows "📈 Go HIGHER!" (Too Low). Score drops to -5.
4. User enters a guess of 70, and the game shows "📉 Go LOWER!" (Too High). Score drops to -10.
5. User enters a guess of 55, and the game shows "🎉 Correct!" with balloons and "You won! The secret was 55. Final score: 60".
6. The game ends; any further action shows "You already won. Start a new game to play again."

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python -m pytest tests/ -v
collected 13 items

tests/test_game_logic.py::test_winning_guess PASSED                      [  7%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 15%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 23%]
tests/test_game_logic.py::test_guess_compared_as_numbers_not_text PASSED [ 30%]
tests/test_game_logic.py::test_range_for_difficulty PASSED               [ 38%]
tests/test_game_logic.py::test_range_for_unknown_difficulty_uses_normal PASSED [ 46%]
tests/test_game_logic.py::test_parse_valid_guess PASSED                  [ 53%]
tests/test_game_logic.py::test_parse_guess_ignores_surrounding_spaces PASSED [ 61%]
tests/test_game_logic.py::test_parse_empty_guess PASSED                  [ 69%]
tests/test_game_logic.py::test_parse_guess_rejects_decimals_and_text PASSED [ 76%]
tests/test_game_logic.py::test_parse_guess_rejects_out_of_range PASSED   [ 84%]
tests/test_game_logic.py::test_parse_guess_accepts_range_edges PASSED    [ 92%]
tests/test_game_logic.py::test_hint_points_the_right_way PASSED          [100%]

============================= 13 passed in 0.03s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
