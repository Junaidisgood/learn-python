#Odd numbers between 1 & 999 using while loop
import random
print("Odd numbers")
counter = 0
while counter<10:
    # Get a random number
    number = random.randint(1, 999)
    if int(number/2) == number/2:
        # if even, dont print
        continue
    # since it skips all even numbers, it should print odd
    print(number)
    # increment the loop counter
    counter += 1
print("Loop is done")