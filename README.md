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

- [ ] Describe the game's purpose.
      - Its a number guessing game with multiple diffuclty settings.
- [ ] Detail which bugs you found.
      - Visual bug of hints being backwars
      - Needed to refesh page when starting new game.
      - Code had values of numbers that would win or not when wrong when they match lexigraphically.
- [ ] Explain what fixes you applied.
      - fixed the logic of < or > of the hint
      - added code that set the reset value to not be a default.
      - check literal when checking answers in the code as well and reject.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

- See attached PNG files.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
