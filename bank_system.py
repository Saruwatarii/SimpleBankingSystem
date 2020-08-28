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
        sumer = 1
        flag = True
        while flag:
            ran_card_num = str(random.randrange(100000000, 999999999))
            iint_n = list(iin)
            summing = list(ran_card_num)
            begge = iint_n + summing
            begge_int = [int(x) for x in begge]
            intsumming = "".join([str(x) for x in begge])

            sumer = sum(begge_int)
            if sumer % 10 != 0:
                flag

            pin_card_num = str(random.randint(0000, 9999))
            org_num = intsumming
            liste = list(org_num)
            odd_multi_2 = [int(x) * 2 if i % 2 == 0 else int(x) for i, x in enumerate(liste)]
            substract_9 = [x - 9 if x > 9 else x for x in odd_multi_2]
            check_sum = sum(substract_9)
            adder = 0

            if check_sum % 10 == 0:
                check_sum = 0
            while check_sum % 10 != 0:
                check_sum += 1
                adder += 1
                continue

            full_ran_card = iin + ran_card_num + str(adder)
            card_info[full_ran_card] = pin_card_num
            num = ""
            chekinger = pin_card_num

            for i in range(len(chekinger)):
                if len(chekinger) != 4:
                    num += '0'
                    chekinger += "1"
                else:
                    break

            pin_card_num = num + str(pin_card_num)
            flag = False

        print("\nYour card has been created")
        print(f"Your card number:\n{full_ran_card}")
        print(f"Your card PIN:\n{pin_card_num}\n")

    elif user_input == 2:
        print("\nEnter your card number:")
        card_number = input()
        print("Enter your PIN: ")
        pin_number = input()
        if card_number in card_info and card_info[
            card_number] == pin_number:  # and card_info[card_number] == pin_number:
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

