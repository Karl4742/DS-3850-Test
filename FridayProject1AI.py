def mad_lib_game():
    # Game instructions
    print("Welcome to the Mad Lib Game!")
    print("Fill in the blanks with words as prompted to create a funny story.\n")

    # Prompting the player for each word
    large_object = input("Enter a large object: ")
    large_objects_plural = input("Enter large objects (plural): ")
    adjective = input("Enter an adjective: ")
    body_part = input("Enter a body part: ")
    restaurant = input("Enter the name of a restaurant: ")
    food1 = input("Enter a type of food: ")
    food2 = input("Enter another type of food: ")

    # Creating the story using formatted strings
    story = (
        f"I’ve had a very {adjective} day. "
        f"This morning, I dropped a box of {large_objects_plural} on my {body_part}. "
        f"Then, at lunch, I went to {restaurant} for their delicious {food1}, "
        f"but the waiter brought me {food2}, which I was not hungry for. "
        f"Finally, on my way home, I was cut off by a van with a large {large_object} "
        f"strapped to the roof."
    )

    # Display the story to the player
    print("\nHere’s your Mad Lib story:\n")
    print(story)

# Run the Mad Lib game
mad_lib_game()
