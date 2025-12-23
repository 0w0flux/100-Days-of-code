import random
import art

ascii = ['5', ';', 'U', '&', 'Y', 'D', '8', 'K', '(', 'J', 'G', 'X', '_', '\\', 'x', 'o', '#', '%', '}', 'E', '"', 'A', 'r', '$', '[', 'F', '>', "'", 'V', 'n', '?', '+', '6', 'b', 'w', 'Z', 'P', '!', 'Q', ' ', 's', 'd', '<', 'j', 'a', '.', 'g', '=', 'C', ']', '~', '*', 
'@', '|', ',', 'H', 'O', 'W', '{', 'R', '3', 'l', '2', 'y', '^', 'N', 'u', ':', '4', 'i', 't', ')', 'p', 'e', 'c', 'T', 'm', 'M', 'f', 'L', 'v', 'B', 'h', 'k', 'z', 'q', '7', 'I', '/', '9', '-', 'S', '`', '1', '0']

def encrypt():
    message = input("\nWhat message do you want to encrypt: \n")
    encrypted_message = ""
    encrypt_done = False
    while not encrypt_done:
        while True:
            shift_decision = input("\nWhat type of shift do you want?:\n1. Random \n2. Manual\n")

            match shift_decision:
                case "1":
                    shift_amount = random.randint(1, 95)
                    print(f"\nRandom shift: {shift_amount}")

                    # Look at this again 
                    for letter in message:
                        if letter not in ascii:
                            encrypted_message += letter
                        else:
                            shifted_index = ascii.index(letter) + shift_amount 
                            shifted_index %= len(ascii) # Important to not get an "Index out of range" error
                            encrypted_message += ascii[shifted_index]

                    print(f"Your encrypted message is: {encrypted_message}\n")
                    break  

                case "2":
                    try:
                        shift_amount = int(input("Please choose a shift (1-95): "))
                        if 1 <= shift_amount <= 95:

                            for letter in message:
                                shifted_index = ascii.index(letter) + shift_amount
                                shifted_index %= len(ascii)
                                encrypted_message += ascii[shifted_index]

                            print(f"\nYour encrypted message is: {encrypted_message}\n")
                            break
                        else:
                            print("Invalid shift! Please enter a number between 1 and 95.")
                    except ValueError:
                        print("Invalid input! Please enter a valid number.")

                case _:
                    print("Invalid choice! Please enter 1 or 2.")
        encrypt_done = True 

def decrypt():
    message = input("\nWhat message do you want to decrypt: \n")
    decrypted_message = ""
    decrypt_done = False
    while not decrypt_done:
        try:
            shift_amount = int(input("Shift: "))
            if shift_amount <= 0 or shift_amount > 95:
                print("Invalid Number! Choose a Number between 1 - 95")
                continue
 
            for letter in message:
                shifted_index = ascii.index(letter) - shift_amount
                shifted_index %= len(ascii)
                decrypted_message += ascii[shifted_index]

            print(f"\nYour decrypted message is: {decrypted_message}\n")
            break
        except ValueError:
            print("Invalid Value! Choose a Number between 1 - 95")

def main():
    print(art.logo)
    while True:
        decision = input("Please choose what you want to do: \n1. Encrypt \n2. Decrypt \n3. Quit\n")
        match decision:
            case "1":
                encrypt()
            case "2":
                decrypt()
            case "3" | "q":
                break
            case _:
                print("\nNot a valid input!\n")


if __name__ == "__main__":
    main()
    