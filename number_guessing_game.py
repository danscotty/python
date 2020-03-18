import random
secret_number = random.randint(1,25)
guess = 0
tries = 0

print("what is your name?")
myName = input()

print ("Welcome to the number guessing game, " + myName)
print ("I am thinking of a number between 1 and 25.")
print ("I will give you four tries to get it. Good luck!")
while int(guess) != secret_number and tries < 4:
    guess = input("what is your guess?")
    if int(guess) > secret_number:
      print ("That is too high.")
    elif int(guess) < secret_number:
        print ("That is too low.")
    tries = tries + 1
if int(guess) == secret_number:
    print ("Holy cow, you guessed my number!, " + myName)
else:
    print ("Better luck next time " + myName)
    print ("The secret number was", secret_number)