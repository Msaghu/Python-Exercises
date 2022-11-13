#Simple if statements
age = int(input("Please enter you age: "))
if age>= 21:
    print("You are old enough to get in ")

#if-else statements
 
else:
    print("Sorry you are too young to get in ")
    print("Come back when you are olde ")

#if-elif-else chain
#age = int(input("Please enter your age"))
if age < 4:
    print("Your entry fee is 0 shillings")
elif age <18:
    print("Your admission fee is 180 shillings")
else:
    print("Your admission fee is 500 shillings")
