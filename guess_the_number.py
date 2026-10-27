import random

def guess_the_number():
    # Generate a random integer between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    
    # Loop until the player guesses correctly
    while True:
        # Prompt the player to enter their guess
        guess_str = input("Enter your guess: ")
        
        # Convert the player's guess to an integer
        try:
            guess = int(guess_str)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        # Check if the guess is too high, too low, or correct
        if guess > secret_number:
            print("Your guess is too high. Guess again.")
        elif guess < secret_number:
            print("Your guess is too low. Guess again.")
        else:
            print("Congratulations! You guessed the number correctly!")
            break

if __name__ == "__main__":
    guess_the_number()

