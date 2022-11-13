#5-1: Conditional Tests
#Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:nderstand why each line evaluates to True or False.
#• Create at least 10 tests. Have at least 5 tests evaluate to True and another
#5 tests evaluate to False.







#5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
#• Tests for equality and inequality with strings
#• Tests using the lower() function
#• Numerical tests involving equality and inequality, greater than and
#less than, greater than or equal to, and less than or equal to
#• Tests using the and keyword and the or keyword
#• Test whether an item is in a list
#• Test whether an item is not in a list

 
#5-3: Alien Colors #1
#alien_color = ["green", "yellow", "red"]

#for color in alien_color:
   # if color == "green":
       # print("You just earned 5 points")
#Another part that will fail the test i.e no output
 #   elif color == "grey":
  #      print("Oops ! What are you doing?")

#5-4: Alien colors #2
alien_color = ["green", "yellow", "red"]

#for color in alien_color:
if "green" in alien_color :
    print("You just earned 5 points for shooting down the alien")
if "grey" in alien_color:
    print("You just earned 10 points")

#if-else chain
if "green" in alien_color:
        print("You just earned 5 points for shooting down the alien")
elif "grey" in alien_color:
    print("You just earned 10 points")

#5-5: Alien colors #3:
if "green" in alien_color:
    print("You just earned 5 points")
elif "yellow" in alien_color:
    print("You just earned 10 points")
elif "red" in alien_color:
    print("You just earned 15 points")
else:
    print("Wow you didnt shoot any")

#with an if chain
if "green" in alien_color:
    print("You just earned 5 points")
if "yellow" in alien_color:
    print("You just earned 10 points")
if "red" in alien_color:
    print("You just earned 15 points")

#5-6: Stages of life
user_age = int(input("Please enter your current age: "))

if user_age <= 2:
    print("You are a baby!")
elif user_age <= 4:
    print("You are a toddler!")
elif user_age <= 13:
    print("You are a still a kid!")
elif user_age <= 20:
    print("You are still a teenager!")
elif user_age <= 65:
    print("You are an adult!")
else:
    print("You are an elder!")

#5-7: Favourite fruit
favourite_fruits = ["bananas", "apples", "avocado"]
user_fruits = input("What are your favourite fruits?")
if "mangoes" in favourite_fruits:
    print("You really like mangoes")
if "kiwi" in favourite_fruits:
    print("You really like kiwi")
if user_fruits in favourite_fruits:
    print(f"You really like {user_fruits}")



