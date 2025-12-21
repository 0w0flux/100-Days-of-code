import random


list_of_words = ["apple", "banana", "cherry", "bottle", "window", "laptop", "pencil", "orange", "silver", "rocket", "flower", "candle", "pocket", "mirror", "finger", "garden", "thunder", "blanket", "diamond", "glasses", "holiday", "horizon", "penguin", "fiction", "gravity", "lantern", "mailbox", "monster", "network", "octopus", "perfume", "plastic", "quantum", "recycle", "scholar", "texture", "tornado", "unicorn", "victory", "welcome", "zephyr", "blanket", "charger", "develop", "express", "fortune", "harmony", "instant", "justice", "kitchen", "liberty", "monitor", "nervous", "outcome", "prepare", "quantum", "refrain", "station", "thunder", "upgrade", "vitamin", "witness", "youthful", "antique", "balance", "capture", "daylight", "eclipse", "feature", "gigabit", "horizon", "immerse", "jigsaw", "kingdom", "laundry", "magnet", "natural", "organic", "passive", "quality", "reunion", "science", "texture", "upgrade", "venture", "whistler", "zealous","acoustic", "battery", "capsule", "dignity", "eclipse", "freedom", "gateway", "history", "iceberg", "journey", "lantern", "mystery", "network"]

secret_word = random.choice(list_of_words)
guessed_word = ["_"] * len(secret_word)
tries = 0
wrong_letters = []

def start():
    global tries
    print("**********Hangman in Python**********")
    while True:
        try:
            difficulty = int(input("Please choose a difficulty:\n1. Easy (20 tries) \n2. Normal (15 tries) \n3. Hard (10 tries) \n"))
            match difficulty:
                case 1:
                    tries = 20
                case 2:
                    tries = 15
                case 3:
                    tries = 10
                case _:
                    print("Invalid input! Please enter a number (1, 2, or 3).\n")
                    continue
            break

        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).\n")


def main():
    global tries
    start()

    while "_" in guessed_word and tries > 0:
        print(f"\nYour word: {' '.join(guessed_word)} ({len(secret_word)})\n")
        print(f"Wrong letters: {wrong_letters}")
        print(f"Tries left: {tries}")
        guess = input(f"What is your guess (only write one character at a time): ").lower()

        if guess == "quit":
            break

        elif guess == "_":
            print(f"{secret_word}\n")
        
        elif len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.\n")
            print(f"You still have {tries} tries.")
            continue

        elif guess in secret_word:
            print(f"\nNice! {guess} is in the word.")
            
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[index] = guess

        else:
            if guess in wrong_letters:
                print("\n----------------------------------------------------------")
                print("You already tried this letter! You will not get a penalty!")
                print("----------------------------------------------------------")
            else:    
                print(f"\n{guess} is not in the word.")  
                tries -= 1  
                wrong_letters.append(guess)
                continue

    if "_" not in guessed_word:
        print("\n***********************************************")
        print(f"Wow! You did it :D the secret word is {secret_word.capitalize()}.")
        print("***********************************************")
    else:
        print(f"You ran out of tries! The secret word was \"{secret_word}\".")

if __name__ == "__main__":
    main()
