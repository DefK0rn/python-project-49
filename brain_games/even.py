import random

import prompt

MAX_ITER = 3
ANSWERS = {
    True: 'yes',
    False: 'no'
}


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


def is_even(number):
    return True if number % 2 == 0 else False


def check_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    iter = 1

    while iter <= MAX_ITER:
        number = random.randint(1, 100)

        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        correct_answer = ANSWERS.get(is_even(number))

        if not answer == correct_answer:
            return wrong_answer(name, answer, correct_answer)
        else:
            print('Correct!')

        iter += 1

    right_answer(name)