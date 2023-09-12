import prompt
from random import randint
from random import choice
import operator

name = ''


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}

def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    print('What is the result of the expression?')
    attempt = 1
    while attempt <= 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        operator = choice(list(operators))
        print(f'Question: {number1} {operator} {number2}')
        answer = prompt.string('Your answer: ')
        result = str(operators.get(operator)(number1, number2))
        if answer == result:
            print('Correct!')
        attempt += 1
        if answer != result:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}.")
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')
