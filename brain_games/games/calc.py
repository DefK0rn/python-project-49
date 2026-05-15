import random

import prompt

MAX_STEP = 3
SUPPORTED_OPERATIONS = ['+', '-', '*']


def wrong_answer(name, answer, correct_answer):
    print(f"'{answer}' is wrong answer ;(.", end=" ")
    print(f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")


def right_answer(name):
    print(f'Congratulations, {name}!')


def get_result(number1, operation, number2):
    match operation:
        case '+':
            return number1 + number2
        case '-':
            return abs(number1 - number2)
        case '*':
            return number1 * number2


def check_calc(name):
    print('What is the result of the expression?')
    step = 1

    while step <= MAX_STEP:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operation = random.choice(SUPPORTED_OPERATIONS)

        print(f"Question: {number1 if number1 > number2 else number2}", end=" ")
        print(f"{operation} {number2 if number1 > number2 else number1}")
        answer = prompt.integer('Your answer: ')
        correct_answer = get_result(number1, operation, number2)

        if answer != get_result(number1, operation, number2):
            return wrong_answer(name, answer, correct_answer)
        else:
            print('Correct!')

        step += 1

    right_answer(name)