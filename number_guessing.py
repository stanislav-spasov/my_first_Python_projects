import random

print("\nWelcome to the game Guess the Number.\n \nFollow the instructions and have fun!")

stop_game = False

while True:
    if stop_game:
        break
    while True:
        start_range = input("\nEnter Lower bound: ")
        if not start_range.isdigit():
            print("Invalid bound. Try again with INTEGER ...")
            continue
        else:
            break
    while True:
        final_range = input("Enter Upper bound: ")
        if not final_range.isdigit():
            print("Invalid bound. Try again with INTEGER ...")
            continue
        elif int(final_range) < int(start_range):
            print("Invalid bounds. Upper bound must be bigger than lower bound. Try again ...")
        else:
            start_range = int(start_range)
            final_range = int(final_range)
            break

    magic_number = random.randint(start_range, final_range)
    counter = 0

    print("\nYou've only 7 chances to guess the integer! Good Luck !!!\n")

    while counter < 7:
        while True:
            number = input(f"Enter your guess ({start_range} - {final_range}): ")
            if not number.isdigit():
                print("Invalid input. Try again with INTEGER ...")
                continue
            else:
                number = int(number)
                if start_range > number or final_range < number:
                    print(f"Invalid number. Your bounds are ({start_range} - {final_range}) ! Try again ...")
                    continue
                break
        counter += 1
        if number > magic_number:
            print(f"Your guess {number} is too high. Remaining attempts: {7 - counter}. Try Again ...")
        elif number < magic_number:
            print(f"Your guess {number} is too small. Remaining attempts: {7 - counter}. Try Again ...")
        elif number == magic_number:
            print(f"\nCONGRATULATIONS !!! You are success to find magic number {magic_number}!")
            print(f"Total Number of Guesses = {counter}")
            new_try = input("\nDo you want to try your luck again? (Y/N): ")
            if new_try == "Y" or new_try == "y":
                break
            elif new_try == "N" or new_try == "n":
                stop_game = True
                break
            else:
                while True:
                    print("Invalid choice . Expected: 'Y' or 'N'!")
                    new_try = input("\nDo you want to try your luck again? (Y/N): ")
                    if new_try == "Y" or new_try == "y":
                        break
                    elif new_try == "N" or new_try == "n":
                        stop_game = True
                        break
                break
    else:
        print("\nSorry ! You can't guess the number after 7 tries. Good luck in the next game !\n")
        new_try = input("Do you want to try your luck again? (Y/N): ")
        if new_try == "Y" or new_try == "y":
            continue
        elif new_try == "N" or new_try == "n":
            break
        else:
            while True:
                print("Invalid choice . Expected: 'Y' or 'N'!")
                new_try = input("\nDo you want to try your luck again? (Y/N): ")
                if new_try == "Y" or new_try == "y":
                    break
                elif new_try == "N" or new_try == "n":
                    stop_game = True
                    break
            continue
