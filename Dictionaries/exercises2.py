#6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements with a loop that runs through the dictionary’s keys and values.
east_africa = {
        'kenya':'nairobi',
        'uganda':'jinja',
        'tanzania':'dar e-salaam',
        'rwanda':'kigali',}

for cou,cities in east_africa.items():
    print(cities.title() + " is the capitali city of " + cou.title() + " .")

#When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.
east_africa['ethiopia'] = 'addis ababa'
east_africa['somalia'] = 'mogadishu'
east_africa['burundi'] = 'bujumbura'
for c,cities in east_africa.items():
    print('I would love to visit ' + cities.title() )

#6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
rivers = {
        'nile':'egypt',
        'delta':'nigeria',
        'volta':'ghana',}

#• Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for r,c in rivers.items():
    print("The " + r.title() + " runs through " + c.title())

#• Use a loop to print the name of each river included in the dictionary.
#• Use a loop to print the name of each country included in the dictionary.
#6-6. Polling: Use the code in favorite_languages.py (page 104).
#• Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
#• Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding.
#If they have not yet taken the poll, print a message inviting them to take the poll.
favourite_languages = {
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python',
        }
new_list = ['josephine', 'phil', 'joshua', 'amara', 'sarah']
for name,langs in favourite_languages.items():
    print(name.title())
    if name in new_list:
        print("Thank you " + name.title() + " for taking the poll about" + langs.title())

