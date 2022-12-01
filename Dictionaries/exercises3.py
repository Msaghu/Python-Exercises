#6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
#Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
person_1 = {'name': 'sharon', 'height': 2, 'age': 22 }
person_2 = {'name': 'Ted', 'height': 0.3, 'age': 1.75}
person_3 = {'name': 'the cat', 'height': 0.15, 'age': 0.75}

all_people = [person_1, person_2, person_3]

for people in all_people:
    print(people)
    print("This is " + people['name'].title() + " who is " + str(people['height']) + " meters tall, and " + str(people['age']) + " years old.")
    
#6-8. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.

pet_1 = {'type': 'dog', 'name': 'lucky', 'owner': 'maureen' , 'colour': 'brown'}
pet_2 = {'type': 'cat', 'name': 'meow', 'owner': 'no one', 'colour': 'grey'}
pet_3 = {'type': 'cat', 'name': 'puss', 'owner': 'feral', 'colour': 'calico'}

pets = [pet_1, pet_2, pet_3]

for attributes in pets:
    print(attributes)
    print('Hey, I know that ' + attributes['colour'] + " "+ attributes['type'] + " !. It's name is " + attributes['name'] + " and it belongs to " + attributes['owner'] + " !.")


#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favourite_places = {
        'Wanjiru': ['diani', 'seychelles', 'zanzibar'],
        'njoki': ['uganda'],
        'wangari': ['ghana', 'toGO'],
        }

for names, places in favourite_places.items():
    print("Hi " + names.title()  + " !how was your vacation?. Did you manage to visit: ")
    for place in places:
        print(place.title())

#6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.


#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city.The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
        'kigali': {
            'country': 'rwanda',
            'population': '2,605,000' ,
            'fun fact': 'the cleanest city in africa',
            },
        'accra': {
            'country': 'ghana',
            'population': '1,208,000' ,
            'fun fact': 'home to the azonto dance',
            },
        'nairobi': {
            'country': 'kenya',
            'population': '5,119,000' ,
            'fun fact': "the name means 'cool waters' in maa",
            },
        }


for key,values in cities.items():
    print("Here are some random facts: " + key.title())
    data = values['country'].title() + ', ' + values['population'] + ', ' + values['fun fact']

    print(data)


#6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output
