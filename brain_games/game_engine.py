from brain_games.scripts import utils

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

        result = utils.is_answer_correct(user_answer, answer)

        if not result:
            break

    if result:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
