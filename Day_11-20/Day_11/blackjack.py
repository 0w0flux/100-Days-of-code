import art
import random
import sys


def rules():
    print("\n***********************The Rules***********************")
    print("1. The deck is unlimited in size.")
    print("2. Cards are not removed from the deck as they are drawn.")
    print("3. There are no jokers.")   
    print("4. The Jack/Queen/King all count as 10.")
    print("5. The Ace can count as 11 or 1.")
    print("6. The cards are: [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]")
    print("7. The cards have equal probability of being drawn. \n")   

def welcome():
    game = input("Do you want to play a game of Blackjack? Type \"y\", \"n\" or \"r\" for the rules: ").lower()
    while True:
        if game == "n":
            sys.exit()
        elif game == "r":
            rules()
            game = input("Do you want to play a game of Blackjack? Type \"y\", \"n\" or \"r\" for the rules: ").lower()
        elif game == "y":
            break
        else:
            print("Invalid input!")
            game = input("Do you want to play a game of Blackjack? Type \"y\", \"n\" or \"r\" for the rules: ").lower()
            continue

def deal_card():
    """Returns a random card from the deck"""
    #        Ace                                   Jack    Queen   King 
    cards = [11,    2, 3, 4, 5, 6, 7, 8, 9, 10,    10,     10,     10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    global balance
    global bet_amount
    if u_score == c_score:
        balance + bet_amount
        return "\nDraw"
    elif c_score == 0:
        return "\nLose, opponent has Blackjack"
    elif u_score == 0:
        balance + bet_amount * 2
        return "\nWin with a Blackjack"
    elif u_score > 21:
        return "\nYou went over. You lose"
    elif c_score > 21:
        balance + bet_amount * 2
        return "\nOpponent went over. You win"
    elif u_score > c_score:
        balance + bet_amount * 2
        return "\nYou win"
    else:
        return "\nYou lose"

def main():
    global balance
    global bet_amount
    balance = 1000
    player_cards = []
    computer_cards = []
    player_score = -1
    computer_score = -1
    welcome()
    print(f"\nYour balance is: {balance}€\n")

    while True:
        try:
            bet_amount = float(input("How much do you want to bet? €"))
            
            if bet_amount > balance:
                print("Insufficient funds!")
                continue
            if bet_amount < 1:
                print("You can't bet 0€ or less!")
                continue

            balance -= bet_amount
            print(f"\nYour balance is: {balance}€ \nYour bet is: {bet_amount}\n")
            break
            
        except ValueError:
            print("Invalid input!")

    for i in range(2):
        computer_cards.append(deal_card())
        player_cards.append(deal_card())

    while True:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            break 
        else:
            player_should_deal = input("Type \"y\" to get another card, type \"n\" to pass: ")
            
            if player_should_deal == "y":
                player_cards.append(deal_card())
            else:
                break


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))
    print(f"Your balance: €{balance}")


    # Implement a "play again" option!

if __name__ == "__main__":
    print(art.logo)
    main()