#A simple dictionary

alien_0 = {"color":"green", "points":5}

print(alien_0["color"])
print(alien_0["points"])

#Working with dictionaries
#Accessing Values in a dictionary
new_points = alien_0["points"]
print("You just earned " + str(new_points) + " points")

#Adding key-value pairs
alien_0["x-position"] = 0
alien_0["y-position"] = 25
print(alien_0)

#Starting with an empty dictionary
tea = {}
tea["add_1"] = "milk"
tea["add_2"] = "tea_leaves"
tea["add_3"] = "sugar"

print(tea)

#Modyfying values in a dictionary
alien_0 = {"color":"green"}
print("The alien is " + alien_0["color"] + "." )

alien_0["color"] = "yellow"
print("The alien is now " + alien_0["color"] + "." )

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print("Original x_position: " + str(alien_0["x_position"]))

##Moving alien to the right
##Determine how far to move alien baaaased on its current speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    #This must be a fast alien
    x_increment = 3

#The new position is the old position plus the increment
alien_0["x_position"] = alien_0["x_position"] + x_increment
print("New position: " + str(alien_0["x_position"]))

#Removing key-value pairs
alien_0 = {"color":"green", "points":5}
del alien_0["points"]
print(alien_0)

#A dictionary of similar objects
favourite_languages = {
        "jen":"python",
        "sarah": "c",
        "edward":"ruby",
        "phil":"python",
        }
print("Sarah's favourite language is " + favourite_languages['sarah'].title() + ".")
