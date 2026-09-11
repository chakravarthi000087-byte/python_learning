import random

number = random.randint(1, 10)

guess = int(input("Guess the number (1-10): "))

if guess == number:
    print("Correct! You guessed it!")
else:
    print("Wrong! The number was:", number)