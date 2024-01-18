import prompt


TRY_NUMBER = 3


def run(game):
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game.DESCRIPTION)

    result = None
    # run several times
    for _ in range(TRY_NUMBER):

        question, answer = game.get_question_and_answer()

        print("Question:", question)
        user_answer = prompt.string("Your answer: ")

        result = str(user_answer).strip() == str(answer).strip()

        if not result:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
