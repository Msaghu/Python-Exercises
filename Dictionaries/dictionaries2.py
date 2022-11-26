#Looping through a dictionary

user_0 = {
        "username":"efermi",
        "first":"enrico",
        "last":"fermi",
        }

for key,value in user_0.items():
    print("Key: " + key.title())
    print("Value: " + value.title())

favourite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward':'ruby',
        'phil':'python',
        '':'',}

for n,l in favourite_languages.items():
    print(n.title() + "'s favorite language is " + l.title())

#Looping through all the keys in a dictionary
for name in favourite_languages.keys():
    print(name.title())
for language in favourite_languages.values():
    print(language.title())
#Looping through the keys is the default behaviour for Python i.e below is same as above
friends = ['phil', 'sarah']
for name in favourite_languages:
#for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + ", I see your favourite language is " + favourite_languages[name].title() + "!.")

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")

#Looping through a Dictionary's keys in order
for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#Looping through all values in a dictionary
print("The following languages have been mentioned: ")
for language in favourite_languages.values():
    print(language.title())

#To see each language without repetition 
for language in set(favourite_languages.values()):
    print(language.title())
