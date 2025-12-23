import random


def main():
    number = random.randint(1, 100)
    attempts = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    while True:
        try:
            difficulty = int(input("Choose a difficulty. \n1. Easy \n2. Hard \n"))

            if difficulty == 1:
                attempts = 10
                break
            elif difficulty == 2:
                attempts = 5
                break
            else:
                print("\nInvalid input! \n")
                continue

        except ValueError:
            print("\nInvaild input! \n")
            continue


    while attempts > 0:
            
        try:
            print(f"\nYou have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))

            if guess == number:
                break
            elif guess > number:
                print("\nToo high!")
                attempts -= 1
            elif guess < number:
                print("\nToo low!")
                attempts -= 1


        except ValueError:
            print("Invalid input! \n")
            continue

    if attempts == 0:
        print("\nYou lost!")
    else:
        print("\nYou won!")


if __name__ == "__main__":
    main()