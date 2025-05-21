import random

start_range = int(input("Enter Lower bound: "))
final_range = int(input("Enter Upper bound: "))

magic_number = random.randint(start_range, final_range)
counter = 0

print("\nYou've only 7 chances to guess the integer!\n")

while counter <= 7:

    number = int(input("Enter your guess: "))
    counter += 1
    if number > magic_number:
        print(f"Your guess {number} is too high. Try Again !")
    elif number < magic_number:
        print(f"Your guess {number} is too small. Try Again !")
    elif number == magic_number:
        print(f"\nCONGRATULATIONS !!! You are success to find magic number {magic_number}!")
        print(f"Total Number of Guesses = {counter}")
        break
else:
    print("\nSorry ! You can't guess the number after 7 tries. Good luck in the next game !")
