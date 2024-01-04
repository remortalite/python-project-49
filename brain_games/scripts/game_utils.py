import prompt


def get_name() -> str:
    name = prompt.string("May I have your name? ")
    return name


def get_answer() -> str:
    return prompt.string("Your answer: ")


def is_answer_correct(user_answer, correct_answer):
    if user_answer.strip() != correct_answer:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False
    print("Correct!")
    return True
