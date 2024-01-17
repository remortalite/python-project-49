def is_answer_correct(user_answer, correct_answer):
    if user_answer.strip() != str(correct_answer):
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False
    print("Correct!")
    return True
