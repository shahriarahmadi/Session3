import random
x = random.randint(0, 20)
r=0
while True:
   
    n = int(input("Enter num = "))
    r += 1
    if x > n:
        print("Higher")
    if x == n:
        print("You Won!")
        print(r)
        break
    if x < n:
        print("Lower")