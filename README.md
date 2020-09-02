# SimpleBankingSystem
A program that allow customers to create a new account in the bank system. When creating an account, the program will generate a new card number which satisfies certain condition within the bank system. After that, a PIN  code gets generated that belongs to the card. If the user chooses login instead of new account, the program is asked for card number information.

The condition it goes through is the **Luhn Algortihm**

This algorithm is used to validate the number created in this program.
It works like this:
- Check the sum of the digits in the number
- Check if the sum matches the expected result or if any error in the digit sequence
- If the sum % 10 = 0, then the number is valid according to the Luhm method.

The steps in the Algorithm: (example)
- Original number = 4000008449433403
- Drop the last digit = 400000844943340
- Multiply odd index in the number(not the odd number itself) by 2 = 8000001648983640
- Substract 9 if the digit is over 9 = 800000748983640
- Sum the digits = 57

In order to find that last digit (checksum), We must find the control number of the number for 400000844943340 through the Luhm algorithm.
The checksum is equal to '57+X', where x is the checksum digit. In order for it to be a valid number, the check number must be a multiplier of 10.
The number that satisfies that condition is the digit 3. Therefore, the checksum of the number 400000844943340 is 3.

The program stores the card number, pin code and balance of each created accounts in a database. The database used in this program is SQLite3.

**Creating a new account**
```  
The program start with a main menu: 
1. Create an account
2. Log into account
0. 0 Exit
```  
**Log in**
```  
Output: You have successfully logged in!
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. 0 Exit
```  
When choosing 1: 
Output: 'Balance {account.balance}'
And go back to the log in menu.

When choosing 2:
``` 
Enter income:
>10000
Income was added! 
```  
And go back into the log in menu

When choosing 3:
```  
Transfer
Enter card number:
>4000003305160034
Enter how much money you want to transfer:
>5000
Success!
 ```
 Ask the user to type in a card, go through Luhm method to check if its valid and check if the card number is stored in the database. It it is valid and stored, it check if its enough money in the card to make the transfer, if not, a the user will get an error:  ```Not enough money! ``` If it is, then they get:  ```Success! ```
When choosing 4:
``` 
The account has been closed!
``` 
And go back to the main menu
When choosing 5:
The user goes back to the main menu for creating an account.

When choosing 0:
Output: 'Bye!'
The user exit the program.
 ```
Examples: 
1. Create an account
2. Log into account
0. Exit
>1

Your card have been created
Your card number:
4000009455296122
Your card PIN:
1961

1. Create an account
2. Log into account
0. Exit
>1

Your card have been created
Your card number:
4000003305160034
Your card PIN:
5639

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000009455296122
Enter your PIN:
>1961

You have successfully logged in!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>2

Enter income:
>10000
Income was added!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>1

Balance: 10000

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305160035
Probably you made a mistake in the card number. Please try again!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305061034
Such a card does not exist.

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305160034
Enter how much money you want to transfer:
>15000
Not enough money!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305160034
Enter how much money you want to transfer:
>5000
Success!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>1

Balance: 5000

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit

>0
Bye!
 ```
