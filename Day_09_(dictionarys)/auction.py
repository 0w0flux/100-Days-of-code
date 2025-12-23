import art


game = True
final = {}

def new_bid():
    global final

    name = input("What is your Name? ")
        
    while True:
        try:
            bid = int(input("What is your bid in €? "))
            break
        except ValueError:
            print("Please choose a valid input!")
            continue

    final[name] = bid

def main():
    global game
    global final

    print(art.logo)
    print("--------Blind Auction--------\n")
    
    while game:

        new_bid()

        choice = input("Are there other bidders? (y/n) ")
        while True:
            if choice == "n":
                game = False
                break
            elif choice == "y":
                print("\n" * 100)
                break
            else:
                choice = input("Invalid choice. Please choose between \"y\" and \"n\" ")



    highest_bidder = max(final, key=final.get)  # outputs the name of the highest bidder
    highest_bid = final[highest_bidder]  # ouputs the bid of the highest bidder
    print("\n" * 100)
    print(f"The winner is {highest_bidder} with a bid of {highest_bid}€.")


if __name__ == "__main__":
    main()
    