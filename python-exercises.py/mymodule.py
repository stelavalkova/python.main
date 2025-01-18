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


def sum(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
print(sum(2,3)) # 5
print(sub(2,3)) # -1
print(mul(2,3)) # 6
print(div(2,3)) # 0.6666666666666666

    
    