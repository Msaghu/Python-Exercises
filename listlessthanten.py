#Exercise 3 
#Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

#PSEUDOCODE
#1.loop through the list to get all elements
#2.weed any values less than 5 print(<5)
#3. print the weeded out values in one by one 
#4. print the weeded values a new list

new_list = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for number in a:
    if number < 5:
        new_list.append(number)
#        print(new_list)

#Extras:
#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
print(new_list)
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
#PSEUDOCODE
#1.use input to get user number
#2.use a loop to compare user number and the list

#Getting user number (WRONG WAY)
#another_number = []
#user_number = int(input("Please enter any number: "))
#number1 = list(user_number)
#for another_number:
#    for user_number < a:
#        another_number.append(a)
#        print(another_number)
#print(another_number)

another_number = []
user_number = int(input("Please enter any number: "))
for item in a:
    if item < user_number:
        another_number.append(item)
        #print(another_number)
print(another_number)
    
