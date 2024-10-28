def study_quiz():
    # Define a dictionary with trivia questions and answers
    questions = {
        "What is the capital of France?": "Paris",
        "What is the largest planet in our solar system?": "Jupiter",
        "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
        "What is the boiling point of water in Celsius?": "100",
        "Who painted the Mona Lisa?": "Leonardo da Vinci"
    }

    # Greet the user
    print("Welcome to the Study Quiz!")
    print("Try to answer each question. Let's begin!\n")

    # Loop through the questions dictionary
    for question, correct_answer in questions.items():
        # Display the question and prompt the user for an answer
        user_answer = input(question + " ").strip()

        # Check if the answer is correct and provide feedback
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer is '{correct_answer}'.\n")

    # Farewell message
    print("Thanks for playing! Good luck with your studies!")

# Run the quiz
study_quiz()
