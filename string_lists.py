#String Lists  
#strings lists index
#Exercise 6 (and Solution)
#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

#PSEUDOCODE
#1. user input , get a string
#2. determine whether it is a palindrome using a for loop

#Getting user input
user_input = input("Please enter your favourite word: ")
print(user_input)

#Looping through the user-input to find if its a palindrome
for item in user_input:
    print(item)
    if item == user_input.reverse():
        print(f"{user_input} is a palindrome")
    elif item != user_input.reverse:
        print(f"{user_input} is just a regular word")
    
