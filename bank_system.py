import random
import sys

iin = "400000"
card_info = {}
balance = 0
while True:
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    user_input = int(input())

    if user_input == 1:
        ran_card_num = str(random.randrange(1000000000, 9999999999))
        pin_card_num = str(random.randint(0000, 9999))
        if len(pin_card_num) != 4:
            pin_card_num = '0' + pin_card_num
        full_ran_card = iin + ran_card_num
        card_info[full_ran_card] = pin_card_num
        print("\nYour card has been created")
        print(f"Your car number:\n{full_ran_card}")
        print(f"Your card PIN:\n{pin_card_num}\n")


    elif user_input == 2:
        print("\nEnter your card number:")
        card_number = input()
        print("Enter your PIN: ")
        pin_number = input()
        if card_number in card_info and card_info[card_number] == pin_number:  # and card_info[card_number] == pin_number:
            print("\nYou have successfully logged in!\n")
            while True:
                print("1. Balance")
                print("2. Log out")
                print("0. Exit")
                login_success = int(input())
                if login_success == 1:
                    print(f"\nBalance: {balance}\n")
                elif login_success == 2:
                    print("\nYou have successfully logged out\n")
                    break
                elif login_success == 0:
                    print("\nBye!")
                    sys.exit()
        else:
            print("Wrong card number or PIN!")
            True

    elif user_input == 0:
        print("\nBye!")
        sys.exit()
