import random

while True:
    b = input("to roll the dice enter r")
    if b == "r":
        a = random.randint(1, 6)
        print("Dice is ", a)
        if a == 6:
            print("one more time!")

        else:
            print("Next person!")
            break