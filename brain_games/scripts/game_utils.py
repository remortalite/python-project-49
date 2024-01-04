import prompt


def get_name() -> str:
    name = prompt.string("May I have your name? ")
    return name


def greet_user(name: str) -> None:
    print(f"Hello, {name}!")


def get_answer() -> str:
    return prompt.string("Your answer: ")


def is_answer_correct(user_answer, correct_answer):
    if user_answer.strip() != correct_answer:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False
    print("Correct!")
    return True


def print_end_message(result: bool, name: str) -> None:
    if result:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
