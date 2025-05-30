import random
from collections import Counter

fruits = ["apple", "banana", "mango", "strawberry", "orange", "grape", "pineapple", "apricot", "lemon",
          "coconut", "watermelon", "cherry", "papaya", "berry", "peach", "lychee", "muskmelon"]
animals = ["lion","elephant","giraffe","zebra","kangaroo","panda","dolphin","eagle","tiger","penguin",
           "wolf","bear","koala","rhinoceros","chimpanzee"]

possible_words = fruits + animals

stop_game = False

while True:
    word = random.choice(possible_words)

    if word in fruits:
        print("\nGuess the word! HINT: word is a name of a fruit")
    elif word in animals:
        print("\nGuess the word! HINT: word is a name of a animal")

    for i in word:
        print("_", end=" ")
    print()

    current_letter = ""
    wrong_letter = ""
    chances = len(word) + 2
    flag = 0

    print(f"You have a {chances} chances ! Good luck !")

    while chances != 0 and flag == 0:
        guess = input("\nEnter a letter to guess: ")

        # Validation of the guess
        if not guess.isalpha():
            print("\nEnter only a LETTER !")
            continue
        elif len(guess) > 1:
            print("\nEnter only a SINGLE letter !")
            continue
        elif guess in current_letter or guess in wrong_letter:
            print("\nYou have already guessed that letter !")
            continue

        # If letter is guessed correctly
        if guess in word:
            # k stores the number of times the guessed letter occurs in the word
            k = word.count(guess)
            for _ in range(k):
                current_letter += guess

        # Print the word
            for char in word:
                if char in current_letter:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
        else:
            wrong_letter += guess
            for char in word:
                if char in current_letter:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
            chances -= 1
            print(f"\nYour available chances are : {chances}")

        if Counter(current_letter) == Counter(word):
            flag = 1
            break

    if flag != 0:
        print()
        print("\nCongratulations, You won !!!")
        print(f"The word is: {word}")
    else:
        print("\nYou lost! Try again.")
        print(f"The word was {word}")

    print()
    while True:
        new_game = input("Do you want to try it again ? (Y/N): ")
        if new_game == "Y" or new_game == "y":
            break
        elif new_game == "N" or new_game == "n":
            stop_game = True
            break
        else:
            print("Invalid choice . Expected: 'Y' or 'N'!")
            continue
    if stop_game:
        break
    else:
        continue
