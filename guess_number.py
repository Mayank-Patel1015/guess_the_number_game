import random

def guess_number(largest_number):
    random_number = random.randint(1,largest_number)
    guess = 0
    guess = int(input("What number would you like to guess?: "))
    while random_number != guess:
        if(guess < random_number):
            print("Guess a higher number")
        if(guess > random_number):
            print("Guess a lower number")
        print("Guess again")
        guess = int(input("What number would you like to guess?: "))
    print(f"Congrats!! You guessed the random number ({str(guess)}) correctly.")

largest_number = int(input("What is the largest number you would like to guess?"))
guess_number(largest_number)
