# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
(for example: "the hints were backwards").

The game was very buggy. I am able to enter a guess and the submit guess button works. The hint shows up after submitting a guess and the
developer debug info has all the correct information. Some bugs I found:
The difficulty slider says the "normal" difficulty is a range 1-100 while the "hard" difficulty is a range from 1-50. The amount of attempts 
allowed for the easy and normal difficulties also seem to be switched. The hints were backwards; they would show to go lower when guessing a number 
lower than the secret. I expect the hint to show go higher. 
Pressing enter to apply the guess doesn't work either, only the Submit Guess button does. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.


| Input                                             | Expected Behavior                  | Actual Behavior                                                                                     | Console Output / Error |
| ------------------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------- |
| Secret is 70, guess 50                            | Hint says "Go HIGHER!"             | Hint says "Go LOWER!"                                                                               | None                   |
| Select Normal, then Hard in the sidebar           | Hard has a wider range than Normal | Normal shows 1-100, Hard shows 1-50                                                                 | None                   |
| Secret is 50, guess 9 on an even-numbered attempt | Outcome is "Too Low"               | Outcome is "Too High" because the secret was turned into a string and compared as text ("9" > "50") | None                   |
| Type a guess and press Enter                      | Guess is submitted                 | Nothing happens until Submit Guess is clicked                                                       | None                   |


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used the AI agent in Cursor. A correct suggestion was swapping the Normal and Hard ranges in get_range_for_difficulty so Normal is 1-50 and Hard is 1-100. I verified it by checking the sidebar range on each difficulty and by adding test_range_for_difficulty, which passes. A suggestion I would not accept as written was how the AI fixed check_guess: it changed the function to return only the outcome, added a new get_hint_message function, and edited [app.py](http://app.py) to match. That was more change than needed; a smaller fix would keep the original (outcome, message) return value, fix the backwards hints, and have the tests check result[0]. Either way, I would verify it by running pytest and playing a round to confirm a high guess says "Go LOWER!" and a low guess says "Go HIGHER!".

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I counted a bug as fixed when I could reproduce it before the change and could no longer reproduce it with the same input afterward. I ran pytest, and all 4 tests passed, including the three check_guess tests and the new difficulty range test. The tests showed that the hints now point the right way and each difficulty returns the correct range. AI helped by pointing out that the starter tests expected check_guess to return just win, too high, or too low, which is why they failed at first. It also wrote test_range_for_difficulty which I read through to make sure it checked the ranges I wanted.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time the "state" of the app changes, i.e. clicking a button, choosing a slider option, or changing a widget, Streamlit runs the whole script again from top to bottom. So normal variables would reset on every state change, so a secret number stored in a plain variable would change every time. Session state is similar to the app having a short term memory. So the secret, attempts, score, and history stays the same between clicks even though Streamlit runs the whole script again. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

A habit I want to keep is writing a small pytest test for each bug so I can prove it is fixed and catch it if it comes back. Next time, I would ask the AI for smaller, focused changes and review each one before moving on, instead of asking it to fix everything at once. This project showed me that AI-generated code can look finished and still have bugs, so I need to test it rather than trust it. It oftens goes above and beyond to fix the problem, creating more overhead than needed for the situation. It also makes understanding/testing more difficult. 