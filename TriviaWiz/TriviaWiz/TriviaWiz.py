#TriviaWiz
#Programmed by Joel Serfoss
#CS 1411
#Professor: Cyril Harris
import random

# List of questions (you can add more)
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Jurassic Park'?",
        "choices": ["A. Michael Crichton", "B. James Patterson", "C. Jane Austen", "D. Mark Twain"],
        "answer": "A"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "choices": ["A. Gold", "B. Oxygen", "C. Silver", "D. Hydrogen"],
        "answer": "B"
    },
    {
        "question": "How many continents are there?",
        "choices": ["A. Five", "B. Six", "C. Seven", "D. Eight"],
        "answer": "C"
    },
    {
    "question": "The Seven Dwarfs are characters from which fairy tale?",
    "choices": ["A. Cinderella", "B. Sleeping Beauty", "C. Rapunzel", "D. Snow White"],
    "answer": "D"
    },
]

def main():
    while True:
        try:
            used_indexes = []
            score = 0
            question_count = 0

            print("\nWelcome to the Random Trivia Quiz Game!")
            print("You'll be asked 5 random questions. Try to get as many right as you can.")

            while question_count < 5:
                index = random.randint(0, len(questions) - 1)
                if index not in used_indexes:
                    used_indexes.append(index)
                    question = questions[index]

                    print(f"\nQuestion {question_count + 1}: {question['question']}")
                    for choice in question['choices']:
                        print(choice)

                    answer = input("Your answer (A/B/C/D): ").upper()
                    if answer not in ['A', 'B', 'C', 'D']:
                        raise ValueError("Answer must be A, B, C, or D.")

                    if answer == question['answer']:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Incorrect. The correct answer was {question['answer']}.")

                    question_count += 1

            print(f"\nYou got {score} out of 5 questions correct.")

            play_again = input("\nDo you want to play again? (Y/N): ").lower()
            if play_again != 'y':
                print("Thanks for playing!")
                break

        except ValueError as e:
            print("Error:", e)

main()