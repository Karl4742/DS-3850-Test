import random

def generate_lottery_numbers():
    # Generate 5 unique white ball numbers between 1 and 69
    white_balls = random.sample(range(1, 70), 5)
    # Sort the white ball numbers for readability
    white_balls.sort()
    
    # Generate a single red ball number between 1 and 26
    red_ball = random.randint(1, 26)
    
    # Display the results
    print("Your lottery numbers are:")
    print("White balls:", white_balls)
    print("Red ball:", red_ball)

# Run the function to generate lottery numbers
generate_lottery_numbers()
