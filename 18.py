def run_quiz(questions):
    score = 0
    for question in questions:
        print(f"\n{question['prompt']}")
        for i, option in enumerate(question['options']):
            print(f"{i + 1}. {option}")

        while True:
            try:
                user_answer = int(input("Enter your answer (number): "))
                if 1 <= user_answer <= len(question['options']):
                    break
                else:
                    print("Invalid input. Please enter a number corresponding to an option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if question['options'][user_answer - 1] == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question['answer']}")
    return score

if __name__ == "__main__":
    # Define your quiz questions
    questions = [
        {
            "prompt": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Rome"],
            "answer": "Paris"
        },
        {
            "prompt": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "prompt": "What is 7 + 8?",
            "options": ["12", "15", "10", "14"],
            "answer": "15"
        },
        {
            "prompt": "Who wrote 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
            "answer": "William Shakespeare"
        }
    ]

    print("Welcome to the Quiz!")
    final_score = run_quiz(questions)
    print(f"\nQuiz finished! You got {final_score} out of {len(questions)} questions correct.")
    print("Thanks for playing!")