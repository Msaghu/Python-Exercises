#Divisors  
#Exercise 4 
#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

#PSEUDOCODE
#1. Get user input ;input(enter number)
#2. print out all divisors of user number
#2 (i) user number % random number here
#2 (ii) use range function to get divisors = range (1, user number)
#2 (iii) for loop:.....for number in range(...) 
# if number % range == 0   then day ....

#Getting user_input
user_input = int(input("Please enter any random number here: "))
print(user_input)
divisors_of_userinput = []
for number in range(1, (user_input + 1)):
    if user_input % number == 0:
        divisors_of_userinput.append(number)
print(divisors_of_userinput)
