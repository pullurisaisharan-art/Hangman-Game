import random

# Hangman word list
WORD_LIST = [
    "python", "hangman", "programming", "computer", "developer",
    "algorithm", "database", "network", "security", "engineering",
    "function", "variable", "recursion", "iteration", "debugging",
    "galaxy", "dinosaur", "adventure", "elephant", "chocolate"
]

# Hangman stages
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

def get_word():
    """Randomly select a word from the list"""
    return random.choice(WORD_LIST).upper()

def display_hangman(tries):
    """Display the hangman figure based on remaining tries"""
    return HANGMAN_STAGES[len(HANGMAN_STAGES) - tries - 1]

def get_guess(guessed_letters):
    """Get a valid letter guess from the player"""
    while True:
        guess = input("\nGuess a letter: ").upper()
        
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

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def play_hangman():
    """Main hangman game logic"""
    word = get_word()
    guessed_letters = set()
    correct_letters = set()
    tries = 6
    game_over = False
    
    print("\n" + "=" * 40)
    print("WELCOME TO HANGMAN!")
    print("=" * 40)
    print(f"\nThe word has {len(word)} letters.")
    
    while not game_over:
        print(display_hangman(tries))
        print("\nWord: ", display_word(word, correct_letters))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining tries: {tries}")
        
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if guess in word:
            correct_letters.add(guess)
            print(f"✓ Good guess! '{guess}' is in the word.")
            
            # Check if player won
            if correct_letters == set(word):
                print(display_hangman(tries))
                print("\nWord: ", word)
                print("\n🎉 YOU WON! Congratulations!")
                game_over = True
        else:
            tries -= 1
            print(f"✗ Sorry, '{guess}' is not in the word.")
            
            # Check if player lost
            if tries == 0:
                print(display_hangman(tries))
                print(f"\nGame Over! The word was: {word}")
                print("💀 YOU LOST!")
                game_over = True

def main():
    """Main program"""
    play_again = True
    
    while play_again:
        play_hangman()
        
        while True:
            response = input("\nDo you want to play again? (yes/no): ").lower()
            if response in ['yes', 'y']:
                play_again = True
                break
            elif response in ['no', 'n']:
                play_again = False
                break
            else:
                print("Please enter 'yes' or 'no'!")
    
    print("\nThanks for playing Hangman! Goodbye!")

if __name__ == "__main__":
    main()