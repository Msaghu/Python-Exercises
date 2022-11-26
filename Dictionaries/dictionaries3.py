#Nesting
#A list of dictionaries
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'green', 'points':10}
alien_2 = {'color':'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#    print(alien)

#Make an empty list for storing aliens
aliens = []

#Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5 ,'speed':'slow'}
    aliens.append(new_alien)

#changing the alien colours as the game progresses
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

#Show the first 5 aliens
for alien in aliens[0:5]:
    print(alien)
print("....")

#Show how many aliens have been created 
print("Total number of aliens: " + str(len(aliens)))

#A list in a dictionary
#Store information about a pizza being ordered
pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
        }

#Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

#
favourite_languages = {
        'jen':['python','ruby'],
        'sarah':['c'],
        'edward':['ruby', 'go'],
        'phil': ['python', 'haskell']
        }

for name, languages in favourite_languages.items():
    print("\n" + name.title() + "'s favourite languages are: ")
    for language in languages:
        print("\t" + language.title())

#A dictionary in a dictionary
users = {
        'aeinstein':{
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
            },
        'ncurie':{
            'first': 'marie',
            'last': 'curie',
            'location': 'parts',
            },
        }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
