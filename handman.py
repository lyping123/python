import random

def choose_word():
    words = ["apple", "banana", "orange", "strawberry", "grape"]
    return random.choice(words)

def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 7

    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("Word:", display_word)
        print("Attempts left:", attempts)

        guess = input("Guess a letter: ").lower()
        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1

        if "_" not in display_word:
            print("Congratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("You ran out of attempts. The word was:", word)


play_hangman()
