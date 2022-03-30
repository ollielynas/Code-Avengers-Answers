#List of weapons available
weapons_available = ["Dagger", "Lance", "Flail", "Medieval Sword", "Broadsword", "Falchion sword", "Greatsword", "Longsword"]

#Print the position of the Broadsword
print(weapons_available.index("Broadsword"))

#Find the position of the Flail and store as index
index = weapons_available.index("Flail")

#Print the index of the Flail in the sentence.
print("The Flail is in position {}".format(index))