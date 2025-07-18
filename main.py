import random
def guessthenumber():
    print("🎲 Welcome to the number guessing game")
    print("im thinking of a number between 1-10 Can you guess it?")
    numtoguess = random.randint(1,10)
    attempts = 0
    guessed = False
    while not guessed:
        try:
            guess = int(input("Enter Your Guess: \n"))
            attempts = attempts + 1

            if guess > numtoguess:
                print("too high try again")
            elif guess < numtoguess:
                print("too low try again")
            else:
                print(f"Correct!✅ The Number was:{numtoguess}. you guessed it in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid Number")

guessthenumber()