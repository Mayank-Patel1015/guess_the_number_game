import random

def guess_number(x):
    random_number = random.randint(1,x)
    guess = 0
    guess = int(input("What number would you like to guess?: "))
    while random_number != guess:
        if(guess < random_number):
            print("Guess a higher number")
        elif(guess > random_number):
            print("Guess a lower number")
        print("Guess again")
        guess = int(input("What number would you like to guess?: "))
    print(f"Congrats!! You guessed the random number ({str(guess)}) correctly.")

x = int(input("What is the largest number you would like to guess?"))
guess_number(x)
