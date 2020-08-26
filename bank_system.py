import random
import sys

iin = 400000
card_info = {}
balance = 0
while True:
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    user_input = int(input())

    if user_input == 1:
        ran_card_num = random.randrange(1000000000, 9999999999)
        pin_card_num = random.randrange(0000, 9999)
        full_ran_card = str(iin) + str(ran_card_num)
        card_info[full_ran_card] = pin_card_num
        print(f"{str(iin) + str(ran_card_num)}")
        print(f"Your card PIN:\n{pin_card_num}")
        # print(card_info)

    elif user_input == 2:
        print("Enter your card number:")
        card_number = input()
        print("Enter your PIN: ")
        pin_number = int(input())
        if card_number in card_info and card_info[
            card_number] == pin_number:  # and card_info[card_number] == pin_number:
            print("You have successfully logged in!\n")
            while True:
                print("1. Balance")
                print("2. Log out")
                print("0. Exit")
                login_success = int(input())
                if login_success == 1:
                    print(f"\nBalance: {balance}\n")
                elif login_success == 2:
                    print("You have successfully logged out\n")
                    False
                elif login_success == 0:
                    print("\nBye!")
                    sys.exit()
        else:
            print("Wrong card number or PIN!")
            True

    elif user_input == 0:
        print("\nBye!")
        sys.exit()
