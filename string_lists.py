#String Lists  
#strings lists index
#Exercise 6 (and Solution)
#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

#PSEUDOCODE
#1. user input , get a string
#2. determine whether it is a palindrome using a for loop

#Getting user input
user_input = input("Please enter your favourite word: ")
user_input1 = list(user_input)
print(user_input1)
print(type(user_input1))

#Looping through the user-input to find if its a palindrome
palindrome = list(reversed(user_input1))
print(palindrome)
if user_input1 == palindrome:
    print(f"{user_input.title()} is a palindrome")
else:
    print(f"{user_input.title()} is just a regular word")
    
