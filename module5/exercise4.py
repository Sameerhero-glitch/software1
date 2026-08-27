import random
num = random.randint(1,10)

number = int(input("Guess a number (1-10): "))

while number != num:

    if number>num:
        print("Too high")

    else:
        print("Too low")

    number = int(input("Guess a number (1-10): "))

print("Correct")   


