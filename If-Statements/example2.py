#Checking fro special items
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for toppings in requested_toppings:
    print("Adding " + toppings + ".")

print("Finished making your pizza!")

#If they run out of green peppers

for toppings in requested_toppings:
    if toppings == "green peppers":
        print("Sorry we are out of green peppers right now.")
    else: 
        print("Adding " + toppings + ".")

print("Finished making your pizza!.")

#With user input
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
toppings = input("Please enter your favourite toppings: ")

for topping in toppings:
    if topping in requested_toppings:
        print(f"Adding {toppings} .")
    if toppings not in requested_toppings:
        print(f"Sorry, we are out of {toppings}")

print("Finished making your pizza!.")

#Checking that a list is not empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested-toppings:
        print("Adding " + requested_topping + ".")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Using multiple lists
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we dont have " + requested_topping + ".")
print("Finished making your pizza!")
