cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car)

#Checking for inequality
requested_topping = "mushrooms"

if requested_topping != 'anchovies':
        print(f"Hold the anchovies")

#Checking numerical comparisons
answer = int(input("Please enter a number here: "))

if answer != 42:
    print("That is not the correct number. Please try again")

#Checking whether a value is not a list
banned_users = ["andrew", "carolina", "david"]
user = input("Please enter you name here, ")

if user not in banned_users:
    print(f"{user.title()} You are allowed to to access this website")

