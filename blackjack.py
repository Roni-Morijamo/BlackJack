from random import *

print("Welcome to Blackjack House!")

repeat = False

while not False:
    user_name = input("What is your name? ")
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    random_cards_user = [choice(cards), choice(cards)]
    print(f"Your cards: {random_cards_user}")
    random_cards_computer = [choice(cards)]
    print(f"Dealer's cards: {random_cards_computer}")

    hint_card = input("Do you want hint a card? ")
    if hint_card == "yes":
        random_cards_user.append(choice(cards))

    while sum(random_cards_user) < 17:
        ask = input("You will need more cards. Hint well card: yes or no? ")
        if ask == "yes":
            random_cards_user.append(choice(cards))
    print(f"{user_name} finally cards: {random_cards_user}")


    while sum(random_cards_computer) < 17:
        random_cards_computer.append(choice(cards))
    print(f"Dealer's finlly cards: {random_cards_computer}")

    sum_user = sum(random_cards_user)
    sum_computer = sum(random_cards_computer)

    if 21 >= sum_user >= sum_computer >= 0 or sum_computer > 21:
        print(f"{user_name} win!")
        if sum_user == 21:
            print("BLACKJACK USER")
    elif 21 >= sum_computer >= sum_user >= 0 or sum_user > 21:
        print("Dealer win!")
        if sum_computer == 21:
            print("BLACKJACK DEALER")
    elif sum_computer > 21 and sum_user > 21:
        print("Both bust! It's a draw.")
    else:
        print("Draw")

    repeat_game = input("Do you want again play? yes or no: ")
    if repeat_game == "yes":
        repeat = True
    else:
        print("Thank you!")
    break


