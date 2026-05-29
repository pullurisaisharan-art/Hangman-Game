# Hangman Game

A simple Python Hangman game implemented in `test.py`.

## Project Overview

This repository contains a console-based Hangman game where the player guesses letters to reveal a hidden word. The game includes:

- random word selection from a built-in list
- visual hangman stages for each incorrect guess
- input validation for letters and repeated guesses
- replay support after each game ends

## How to run

### Option 1: Run in VS Code
1. Open this folder in VS Code.
2. Install the Python extension if needed.
3. Select the Python interpreter in the status bar.
4. Open `test.py`.
5. Open the Run and Debug view (`Ctrl+Shift+D`).
6. Run `Python: Run test.py`.

### Option 2: Run in terminal
From the project folder, run:

```powershell
cd "c:\python internship"
& .\.venv\Scripts\python.exe .\test.py
```

Or if you have Python installed globally:

```powershell
cd "c:\python internship"
python .\test.py
```

## How to play

- Guess a letter by typing a single letter and pressing Enter.
- The game shows which letters you have already guessed.
- You have 6 incorrect tries before the hangman is complete.
- When the game finishes, type `yes` or `no` to play again.

## Notes

- If you see `python not found`, make sure the correct interpreter is selected or use the virtual environment path.
- The game logic is contained entirely in `test.py`.
