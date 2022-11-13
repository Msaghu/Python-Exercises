#Exercise 2 

#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

#PSEUDOCODe
#1. Get user input
#2. Determine whether INPUT is opdd or even and print message;(use the modulo operator for this)
#3. If INPUT modulo 4 = 0 , print messaage
#4. ask user fot two numbers, num & check

#.1
user_number = int(input("Please enter any number: "))

#2.1
if user_number % 2 == 0:
    print(f"Number {user_number} is even")
#2.1
else:
    print(f"{user_number} is odd")
#3
Exercise 2 (and Solution)
The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropria
