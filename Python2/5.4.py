favorite_foods = []

#Start a loop to ask user to enter their favorite foods
repeat = True
while repeat == True:
  food = input("Please enter a favorite food or 'done' to end input: ").strip().lower()
  
  #Check if user has entered done so that loop can be stopped if so
  if food == 'done':
    repeat = False
  else:
    #Check if food is already in list
    count = favorite_foods.count(food)
    #If so, give user error message, otherwise add the food and give success message
    if count > 0:
      print("Sorry {} is already on the list!".format(food))
    else:
      favorite_foods.append(food)
      print("{} has been added!".format(food))

#Once user is done, print out their list for them
print("Your favorite foods are: ")

for food in favorite_foods:
  print(food.title()) #Add a capital letter
