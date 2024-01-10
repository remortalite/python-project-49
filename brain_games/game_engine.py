from brain_games.scripts import utils


TRY_NUMBER = 3

def game_step(game):

    question, answer = game.get_question_and_answer()

    print("Question:", question)

    user_answer = utils.get_answer()
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
    name = utils.get_name()
    utils.greet_user(name)

    print(game.DESCRIPTION)

    result = is_win(game)
    utils.print_end_message(result, name)