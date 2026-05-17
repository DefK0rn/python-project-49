import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def wrong_answer(name, answer, correct_answer):
    print(f"'{answer}' is wrong answer ;(.", end=" ")
    print(f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")


def right_answer(name):
    print(f'Congratulations, {name}!')