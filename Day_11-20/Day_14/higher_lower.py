# higherlowergame.com

# Stats are from 2020
from data import data
from art import logo, vs
import random


def compare(choice_a, choice_b):
    global score
    global game
    if choice_a > choice_b:
        score += 1
        return score
    else:
        game = False
        return score, game

def main():
    global score
    global game
    score = 0
    game = True

    while game == True:
        name_1 = random.choice(data)
        follower_1 = name_1["follower_count"]

        name_2 = random.choice(data)
        follower_2 = name_2["follower_count"]

        if name_1 == name_2:
            name_2 = random.choice(data)
            follower_2 = name_2["follower_count"]

        print(f"\nCurrent Score: {score}")

        print(f"Compare A: {name_1['name']}, a {name_1['description']}, from {name_1['country']}")
        print(vs)
        print(f"Compare B: {name_2['name']}, a {name_2['description']}, from {name_2['country']}")

        while True:
            choice = input("Who has more followers? Type \"A\" or \"B\": ").lower()

            if choice == "a":
                compare(follower_1, follower_2)
                break

            elif choice == "b":
                compare(follower_2, follower_1)
                break

            else:
                print("\nInvalid input!\n")
                print(f"Compare A: {name_1['name']}, a {name_1['description']}, from {name_1['country']}")
                print(vs)
                print(f"Compare B: {name_2['name']}, a {name_2['description']}, from {name_2['country']}")
                continue

        if game == False:
            break

    print("\n")
    print(f"Sorry, that's wrong. Final score: {score}")


if __name__ == "__main__":
    print(logo)
    main()
