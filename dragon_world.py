import random
import time

def displayIntro():
    print("You are in a land full of dragons. In front of you, you see two caves. in one cave , the dragon is friendly and will share his treasure with you. The other dragons is greedy and hungry, and will eat you on sight.")
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print("which cave will you go into? (1 or 2)")
        cave = input()


    return cave

def checkCave(chosenCave):
    print("you approach the cave")
    time.sleep(2)
    print("it is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws")
    print()
    time.sleep(2)

    freindlyCave = random.randint(1, 2)

    if chosenCave == str(freindlyCave):
        print("Gives you his treasure!")
    else:
        print("Gobbles you in one bite!")

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Do you wan't to play again?")
    playAgain = input()