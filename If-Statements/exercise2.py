#5-8: Hello Admin
#usernames = ['admin', 'caretaker', 'cook', 'tailor', 'electrician']
#for user in usernames:
#    if user == 'admin':
#        print(f"Hello {user}, would you like to see a status report.")
 #   else:
  #      print(f"Hello {user}, thank you for logging back in.")

#5-9: No users
usernames = []
if usernames:
    for user in usernames:
        print("Hello there")
else:
    print("We need to find some users!")

#5-10: Checking usernames
current_users = ['Bob', 'Rema', 'Bobrisky', 'Chioma', 'Wizkid']
new_users = ['Bobrisky', 'jacob', 'Asake']

for user in new_users:
    if user in current_users:
        print("Please choose another username")
    else:
        print(f"The '{user.title()}' is available")

#5-11: Ordinal Numbers
numbers = list(range(1,10))
print(numbers)
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
