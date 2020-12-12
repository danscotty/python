import time

print("Welcome to Adventurenow!")
time.sleep(1)
print("If this game is not good sorry im just 13 years old")
time.sleep(1)

name = input("Whats youre name? ")
age = int(input("whats youre age? "))
time.sleep(1)
print("hello", name, "you are", age, "years old, lets see if youre old enough to play")
time.sleep(1)

if age >= 10 :
  print("You are old enough to play!")
  time.sleep(1)

  choice1 = input("Choice 1... left or right (left/right)")
  time.sleep(1)
  if choice1 == "left":
    print("You walk across a lake then you trip on a stone and fall in the river")
    time.sleep(1)
    print("You faint and you lose 2 hp")
    time.sleep(1)
    Health = 8
    choiceleft = input("You see a house and a forest where do you want to go (house/forest)")
    time.sleep(1)
    if choiceleft == "forest":
      print("You suvived but get stupid and bash youre head on a stone and loose 5 Health")
      time.sleep(1)
      Health = 3
      choice2 = input("wanna bash youre head on a rock again or do you want to go to a village (again/village)")
      time.sleep(1)
      if choice2 == "village":
        print("You enter the village and some farmers attack you for stepping on there crops.")
        print("Died for stepping on crops Oof")
      elif choice2 == "again":
        print("you bash your head on a stone again you died")
    elif choiceleft == "house":
      print("You enter the house and a old man takes his shotgin and shoots you")
      time.sleep(1)
      print("You entered someones property you idiot! You died...")
  elif choice1 == "right":
    print("You walk across a lake and trip on a stone and fall in the river and a shark attacks you")
    time.sleep(1)
    print("You lost 9 HP")
    Health = 1
    time.sleep(1)
    choiceRight = input("Do you want to go to a house or do you want to go in a forest? (house/forest)")
    time.sleep(1)
    if choiceRight == "house":
      print("You knock on the door and a kind old man opens the door for you, you rest and gain 5 hp")
      time.sleep(1)
      print("You tell the old man he was too kind and you have to leave so you hire a soldier to take care of him")
      time.sleep(1)
      choice3 = input("Do you want to go into the village or do you want to go in the forest? (village/forest)")
      if choice3 == "forest":
        print("You enter and you build youre own house and live youre life and get married and have kids ")
        time.sleep(1)
        print("You win!!")
      elif choice3 == "village":
        print("You get killed by wolves on youre way there")
        time.sleep(1)
        print("shouldov toulkin the path")

      else:
        print("Restart the game and next time type village or forest")
    elif choiceRight == "forest":
      print("You go in the forest and you get attacked by wolves")
      time.sleep(1)
      print("Oof")
    else:
      print("Restart the game and next time type house or forest")
    
  else:
    print("Pls restart the game and next time type left or right.")
else:
  print("You are not old enough to play...")