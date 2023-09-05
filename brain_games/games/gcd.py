from random import randint
import math
import prompt

name = ''

def greet():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    return (f'Hello, {name}!')


def rules():
    print('Find the greatest common divisor of given numbers.')


def gcd_game():
    count = 0
    while count <= 3:
        num1 = randint(1,30)
        num2 = randint(1,30)
        print(f'Question: {num1} {num2}')
        answer = prompt.string('Your answer: ' )
        result = math.gcd(num1, num2)
        if answer == str(result):
            print('Correct!')
            count += 1
            if count == 3:
                print('Congratulations, ', name, '!')
                break
        else:
            print(f'"{answer}" is wrong answer ;(.\nLet\'s try again, {name}')
            break
