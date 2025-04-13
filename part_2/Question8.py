import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        try:
            # Prompt user for guess
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Enter your guess: "))
            
            # Check the guess
            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number}!")
                return
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
            
            attempts += 1
            
        except ValueError:
            print("Please enter a valid number!")
    
    # If all attempts are used
    print(f"\nGame Over! The secret number was {secret_number}.")

# Start the game
number_guessing_game()
