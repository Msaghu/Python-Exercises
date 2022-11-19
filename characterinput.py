#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.

#PSEUDOCODE
#1.input age & name

user_age = int(input("Please enter your age: "))
user_name = input("Please enter your name: ")

#2.print out the age & name 

print(f"Hi my name is {user_name}.title and I am {user_age}.")

#3.print out the year they will turn 100, calculate to find this

import datetime 
today = datetime.date.today()
year = today.strftime("%Y")
years_to_100 = 100 - user_age
year_turning_100 = int(year) + int(years_to_100) 

answer = f"\nI will be turning 100 in {year_turning_100}"
print(answer)

#Extras:

#Add on to the previous program by askiing the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

user_number = int(input("Please enter any number: "))
print( user_number * answer)
