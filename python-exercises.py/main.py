import random

targetNumber = 6
guess = random.randint(0, 750)
counter = 1
# Comparison Operator != means not equal to == means equal to
while guess != targetNumber:
    print("Sorry, that's not it.")
    counter += 1 # Increment the counter
    guess = random.randint(0, 750)
    print("Guess again as your guess was ",guess)
    
    
print("You got it after ",counter," tries!")