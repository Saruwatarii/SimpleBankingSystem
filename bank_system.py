import random
import sys
import sqlite3

conn = sqlite3.connect("card.s3db")
# Cursor object-**
cur = conn.cursor()
# Execute the query
'''
sql_drop_card_table = """DROP TABLE card;"""
cur.execute(sql_drop_card_table)
conn.commit()
'''
card_info = {}

def create_sql_table():
    "Creating a table called card"
    sql_create_card_table = """CREATE TABLE IF NOT EXISTS card (
                                    id integer PRIMARY KEY,
                                    number text,
                                    pin text,
                                    balance integer DEFAULT 0 ); """
    cur.execute(sql_create_card_table)
    # When changes have been made in DB, remember to commit
    conn.commit()

def luhm_algo_checker():
    '''Using the luhm algorithm to check if a number is valid.
    If the number pass the luhm algorithm, the number gets returned.
    ALso generating a 4 digit number for the pin code, which also gets returned'''
    iin = "400000"
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
        pin_card_num = str(random.randint(0000, 9999))
        num = ""
        temporary_pin = pin_card_num

        for i in range(len(temporary_pin)):
            if len(temporary_pin) != 4:
                num += '0'
                temporary_pin += "1"
            else:
                break

        pin_card_num = num + str(pin_card_num)
        card_info[full_ran_card] = pin_card_num
        flag = False

    return full_ran_card, pin_card_num

def valid_luhm(valid):
    flag = True
    while flag:

        begge = list(str(valid))

        begge_int = [int(x) for x in begge]
        intsumming = "".join([str(x) for x in begge])

        org_num = intsumming
        liste = list(org_num)
        odd_multi_2 = [int(x) * 2 if i % 2 == 0 else int(x) for i, x in enumerate(liste)]
        substract_9 = [x - 9 if x > 9 else x for x in odd_multi_2]
        check_sum = sum(substract_9)
        adder = 0

        if check_sum % 10 == 0:
            check_sum = 0
            flag = False
        else:
            print("Probably you made a mistake in the card number. Please try again!\n")
            flag = False
            logged_in()

def balance():
    'Fetching the balance from the database corresponding to the account'
    cur.execute(f"""SELECT 
                        balance
                    FROM
                        card
                    WHERE
                        number = {card_number} AND pin = {pin_number}""")
    conn.commit()
    print(f"\nBalance: {cur.fetchone()[0]}\n")

def add_income():
    "Deposit money into the account"
    income = int(input("\nEnter income:\n"))
    cur.execute(f"""UPDATE 
                       card 
                    SET 
                       balance = balance + {income}""")
    conn.commit()
    print("Income was added!\n")
    logged_in()

def logged_in():
    'The menu after the user has logged in'
    flag = True
    while True:
        print("1. Balance")
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close account")
        print("5. Log out")
        print("0. Exit")
        login_success = int(input())
        if login_success == 1:
            balance()
        elif login_success == 2:
            add_income()
        elif login_success == 3:
            transfer()
        elif login_success == 4:
            close_account()
        elif login_success == 5:
            print("\nYou have successfully logged out\n")
            main_menu()
        elif login_success == 0:
            print("\nBye!")
            sys.exit()

def close_account():
    "Delete row from database and delete key,value from card_info from the user logged in."
    cur.execute(f"""DELETE FROM card
                WHERE number = {card_number}""")
    conn.commit()
    #  removing = card_number.pop("card_number")
    del card_info[card_number]
    print("\nThe account has been closed!\n")
    main_menu()

def transfer():
    "Transfer money to another account if enough money."
    print("Transfer")
    transfer_number = int(input("Enter card number: "))
    valid_luhm(transfer_number)
    print(card_number)
    if str(transfer_number) == card_number:
        print("You can't transfer money to the same account!")
        logged_in()
    if str(transfer_number) not in card_info:
        print("Such a card does not exist")
        logged_in()

    cur.execute(f"""SELECT 
                            balance
                        FROM
                            card
                        WHERE
                            number = {card_number} AND pin = {pin_number}""")
    conn.commit()
    transfer_money = int(input("Enter how much money you want to transfer:"))
    if str(transfer_number) in card_info:
        if (cur.fetchone()[0]) < transfer_money:
            print("Not enough money!")
            logged_in()
        else:
            print("Success")
            cur.execute(f"""UPDATE 
                                   card 
                               SET 
                                   balance = balance - {transfer_money}
                            """)
            conn.commit()
            logged_in()

def create_account():
    '''number variable passes to the luhm_algo_checker function which return a valid card number and a pin code.
    the card and pin number gets added into the database.'''
    global number
    number = luhm_algo_checker()
    cur.execute("INSERT INTO card (number, pin) VALUES (?, ?)", (number[0], number[1]))
    conn.commit()
    print("\nYour card has been created")
    print(f"Your card number:\n{number[0]}")
    print(f"Your card PIN:\n{number[1]}\n")

def main_menu():
    "The main menu for creating an account."
    while True:
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        user_input = int(input())
        if user_input == 1:
            flag = True
            while flag:
                create_account()
                flag = False
        elif user_input == 2:
            print("\nEnter your card number:")
            global card_number
            card_number = input()
            print("Enter your PIN: ")
            global pin_number
            pin_number = input()
            if card_number in card_info and card_info[card_number] == pin_number:
                print("\nYou have successfully logged in!\n")
                logged_in()
            else:
                print("\nWrong card number or PIN!\n")
                True
        elif user_input == 0:
            print("\nBye!")
            sys.exit()

create_sql_table()
main_menu()