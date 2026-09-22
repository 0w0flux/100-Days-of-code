from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def main():
    question_bank = []

    for question in question_data:
        text = question["question"]
        answer = question["correct_answer"]
        q = Question(text, answer)
        question_bank.append(q)


    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions(): # If quiz still has questions remaining
        quiz.next_question()


    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    main()
