from brain_games.scripts import utils

import prompt


TRY_NUMBER = 3


def game_step(game):

    question, answer = game.get_question_and_answer()

    print("Question:", question)

    user_answer = prompt.string("Your answer: ")
    result = utils.is_answer_correct(user_answer, answer)
    if result:
        return True
    return False


def is_win(game) -> bool:
    for _ in range(TRY_NUMBER):
        if not game_step(game):
            return False
    return True


def run(game):
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game.DESCRIPTION)

    result = is_win(game)
    if result:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
