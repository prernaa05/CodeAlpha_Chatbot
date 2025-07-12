import random

# --- Word Bank ---
word_list = ["apple", "banana", "grape", "orange", "peach"]

# --- Choose a Random Word ---
secret_word = random.choice(word_list)
guessed_letters = []
tries_left = 6

# --- Display Setup ---
print("🎉 Welcome to Hangman Game! 🎉")
print("Guess the word, one letter at a time.")
print(f"You have {tries_left} incorrect guesses allowed.\n")

# --- Game Loop ---
while tries_left > 0:
    # Show current word status
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: ", display_word.strip())

    # Check for win
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Get input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("✅ Good guess!\n")
    else:
        tries_left -= 1
        print(f"❌ Wrong guess! Tries left: {tries_left}\n")

# --- Game Over ---
if tries_left == 0:
    print("💀 You lost! The word was:", secret_word)
print("\nThanks for playing Hangman! 🧩")
