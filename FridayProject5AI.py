# Define functions for changing text color
def red_text(text):
    return f"\033[91m{text}\033[0m"

def blue_text(text):
    return f"\033[94m{text}\033[0m"

def green_text(text):
    return f"\033[92m{text}\033[0m"

def yellow_text(text):
    return f"\033[93m{text}\033[0m"

def magenta_text(text):
    return f"\033[95m{text}\033[0m"

# Display each color as an example
print("Example outputs with each color:")
print(red_text("This is red text."))
print(blue_text("This is blue text."))
print(green_text("This is green text."))
print(yellow_text("This is yellow text."))
print(magenta_text("This is magenta text."))
print("\n")

# Main Program Logic
print("Choose a color to display your text.")
print("Options: red, blue, green, yellow, magenta")

# Get user choice of color and input text
color_choice = input("Enter a color: ").strip().lower()
user_text = input("Enter the text you want to display: ").strip()

# Display the text in the chosen color
if color_choice == "red":
    print(red_text(user_text))
elif color_choice == "blue":
    print(blue_text(user_text))
elif color_choice == "green":
    print(green_text(user_text))
elif color_choice == "yellow":
    print(yellow_text(user_text))
elif color_choice == "magenta":
    print(magenta_text(user_text))
else:
    print("Invalid color choice. Please choose from the available options.")

