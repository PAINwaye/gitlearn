import random
try:
    number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    if guess == number:
        print(" Correct! You guessed it.")
    else:
        print(f"Wrong! The number was {number}.")
finally:
    print("Game Over!")