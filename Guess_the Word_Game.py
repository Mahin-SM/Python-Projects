import random

def choose_word():
    words = ["python", "developer", "university", "computer", "gaming", "artificial", "intelligence"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def guess_the_word():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to the Guess the Word Game!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter! Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"Out of attempts! The word was '{word}'.")

if __name__ == "__main__":
    guess_the_word()
