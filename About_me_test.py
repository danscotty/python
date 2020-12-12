import time
points = 5
print("Hey dudes this is a program about me and it will show if you know me or not...")
time.sleep(2)
print("There are points in this game, if you lose a question you lose a point...")
time.sleep(2)
print("First question...")
time.sleep(3)
def Question1():
    Question1 = input("""What would be my dream car be? a) lamborghini averto, b) 2021 Bugatti Chiron
Super Sport, c) 2021 Bugatti Divo, even for me these were hard choises but
i chose a car so pick one! (lamborghini averto, 2021 Bugatti Chiron Super
Sport, 2021 Bugatti Divo)""")
    time.sleep(2)
    if Question1 == "2021 Bugatti Chiron Super Sport":
        print("You got it, now for the next question...")
        time.sleep(2)
    elif Question1 == "2021 Bugatti Divo":
        print("Incorrect, you lost a point")
        global points
        points -= 1
        time.sleep(3)
    elif Question1 == "lamborghini averto":
        print("Incorrect, lose a point...")

        points -= 1
        time.sleep(3)
    else:
        print("Try again next time because you had a typpo...")
        quit
Question1()
def Question2():
    print("So here is the next question...")
    Question2 = input("""Whats the movie/carton/series i want to watch? a) carmen sandiego b) mandalorian c) last kids on earth""")
    time.sleep(2)
    if Question2 == "carmen sandiego":
        print("Incorrect lost a point")
        global points
        points -= 1
        time.sleep(2)
    elif Question2 == "mandalorian":
        print("Correct...")
        time.sleep(2)
    elif Question2 == "last kids on earth":
        print("Incorrect lose a point")

        points -= 1
        time.sleep(2)
    else:
        print("Try again next time because you had a typo...")
        quit
Question2()
print(points)