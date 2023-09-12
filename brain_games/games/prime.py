from random import randint
import prompt

name = ''


def greet():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def rules_of_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_simple(x):
    numbers = range(2, x)
    for num in numbers:
        if x % num == 0:
            return 'no'
    return 'yes'


def brain_prime():
    count = 1
    while count <= 3:
        number = randint(2, 50)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        result = is_simple(number)
        if answer == result:
            print('Correct!')
            count += 1
        else:
            print(f'"{answer}" is wrong answer ;(.')
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')
