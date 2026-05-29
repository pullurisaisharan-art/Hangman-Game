import random
from typing import Set

# Hangman word list
WORD_LIST = [
    "python", "hangman", "programming", "computer", "developer",
    "algorithm", "database", "network", "security", "engineering",
    "function", "variable", "recursion", "iteration", "debugging",
    "galaxy", "dinosaur", "adventure", "elephant", "chocolate"
]

# Hangman stages for each incorrect guess
HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
       ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
       ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
       ---------
    """,
    """
       ------
       |    |
       |    O
       |   \\|
       |
       |
       ---------
    """,
    """
       ------
       |    |
       |    O
       |   \\|/
       |
       |
       ---------
    """,
    """
       ------
       |    |
       |    O
       |   \\|/
       |    |
       |
       ---------
    """,
    """
       ------
       |    |
       |    O
       |   \\|/
       |    |
       |   / \\
       ---------
    """
]

MAX_TRIES = len(HANGMAN_STAGES) - 1


def get_word() -> str:
    """Return a random word from the word list in uppercase."""
    return random.choice(WORD_LIST).upper()


def display_hangman(tries: int) -> str:
    """Return the hangman drawing for the current number of remaining tries."""
    stage_index = MAX_TRIES - tries
    stage_index = max(0, min(stage_index, MAX_TRIES))
    return HANGMAN_STAGES[stage_index]


def get_guess(guessed_letters: Set[str]) -> str:
    """Prompt the player for a single valid letter guess."""
    while True:
        guess = input("\nGuess a letter: ").strip().upper()

        if len(guess) != 1:
            print("Please enter exactly one letter!")
            continue

        if not guess.isalpha():
            print("Please enter a valid letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        return guess


def format_word(word: str, guessed_letters: Set[str]) -> str:
    """Return the word display with guessed letters revealed."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def prompt_yes_no(message: str) -> bool:
    """Prompt the player for a yes/no response."""
    while True:
        response = input(message).strip().lower()
        if response in {"yes", "y"}:
            return True
        if response in {"no", "n"}:
            return False
        print("Please enter 'yes' or 'no'.")


def show_game_status(word: str, guessed_letters: Set[str], tries: int) -> None:
    """Print the current game status to the player."""
    print(display_hangman(tries))
    print("\nWord: ", format_word(word, guessed_letters))
    print(
        f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}"
    )
    print(f"Remaining tries: {tries}")


def play_hangman() -> None:
    """Run a single game of Hangman."""
    word = get_word()
    guessed_letters: Set[str] = set()
    correct_letters: Set[str] = set()
    tries = MAX_TRIES
    word_letters = set(word)

    print("\n" + "=" * 40)
    print("WELCOME TO HANGMAN!")
    print("=" * 40)
    print(f"\nThe word has {len(word)} letters.")

    while True:
        show_game_status(word, guessed_letters, tries)

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            correct_letters.add(guess)
            print(f"✓ Good guess! '{guess}' is in the word.")

            if word_letters.issubset(correct_letters):
                print(display_hangman(tries))
                print("\nWord: ", word)
                print("\n🎉 YOU WON! Congratulations!")
                break
        else:
            tries -= 1
            print(f"✗ Sorry, '{guess}' is not in the word.")

            if tries == 0:
                print(display_hangman(tries))
                print(f"\nGame Over! The word was: {word}")
                print("💀 YOU LOST!")
                break


def main() -> None:
    """Entry point for the Hangman game."""
    print("Welcome to the improved Hangman game!")

    while True:
        play_hangman()
        if not prompt_yes_no("\nDo you want to play again? (yes/no): "):
            break

    print("\nThanks for playing Hangman! Goodbye!")


if __name__ == "__main__":
    main()
