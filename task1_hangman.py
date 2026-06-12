# ============================================
# CodeAlpha Internship — Task 1: Hangman Game
# ============================================

import random

# Predefined list of 5 words
WORDS = ["python", "laptop", "coding", "rocket", "jungle"]

HANGMAN_STAGES = [
    # 0 wrong guesses
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    # 1 wrong guess
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    # 2 wrong guesses
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    # 3 wrong guesses
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    # 4 wrong guesses
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    # 5 wrong guesses
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    # 6 wrong guesses — Game Over
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("=" * 40)
    print("       Welcome to Hangman! 🎮")
    print("=" * 40)
    print("Guess the word — you have 6 wrong guesses allowed.\n")

    while wrong_guesses < max_wrong:
        # Display hangman stage
        print(HANGMAN_STAGES[wrong_guesses])

        # Display current word progress
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print(f"Word: {display_word}")
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
        print(f"Letters guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 You won! The word was '{word}'. Congratulations!")
            return

        # Get player input
        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! '{guess}' is not in the word.")

    # Game over
    print(HANGMAN_STAGES[6])
    print(f"\n💀 Game Over! The word was '{word}'. Better luck next time!")


def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (yes/no): ").lower().strip()
        if again not in ["yes", "y"]:
            print("\nThanks for playing Hangman! Goodbye! 👋")
            break


if __name__ == "__main__":
    main()
