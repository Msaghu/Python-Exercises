#List Overlap  
#Exercise 5 (and Solution)
#Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#PSEUDOCODE
#1. write a for loop .... for number in a
#2. compare the number in the second list
#3. create an empty list and append them into the new empty list

# Create a for loop for items in list a
common_numbers = []
for number in b:
    if number in a:
        common_numbers.append(number)
print(common_numbers)

#Extras:

#Randomly generate two lists to test this
list1 = int(input("Please enter a range of numbers: "))
random_list1 = list(range(1, list1))
print(random_list1)

list2 = int(input("Please enter another range of numbers: "))
random_list2 = list(range(list1, list2))
print(random_list2)

random_numbers = []
for item in random_list1:
    if item in random_list2:
        random_numbers.append(item)
print(random_numbers)


#Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
