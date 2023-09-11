import prompt
from random import randint

name = ''


def is_even(number):
    return number % 2 == 0


def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempt = 1
    while attempt <=3:
        number = randint(1,100)
        print('Question:', number)
        result = prompt.string('Your answer: ')
        if result == 'yes':
            result = True
        if result == 'no':
            result = False
        if is_even(number) == result:
            print('Correct!')
        attempt += 1
        if is_even(number) != result:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')
    