import random

def guessing_game():
    # Greeting and asking if the user wants to play
    print("Welcome to the Number Guessing Game!")
    play_game = input("Do you want to play? (yes/no): ").strip().lower()

    # Check if the user wants to play
    if play_game == "yes":
        print("Great! I'm thinking of a number between 1 and 10.")
        
        # Generate a random number between 1 and 10
        secret_number = random.randint(1, 10)
        
        # Initialize the loop for guessing
        while True:
            try:
                # Prompt the user to guess the number
                guess = int(input("Take a guess: "))
                
                # Check if the guess is correct
                if guess == secret_number:
                    print("Congratulations! You've guessed the number!")
                    break
                # Give hints if the guess is incorrect
                elif guess < secret_number:
                    print("Too low. Try again!")
                else:
                    print("Too high. Try again!")
            except ValueError:
                print("Please enter a valid number between 1 and 10.")
        
    else:
        print("Maybe next time!")

    # Farewell message
    print("Thank you for playing! Goodbye!")

# Run the game
guessing_game()
