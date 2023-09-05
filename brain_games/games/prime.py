from random import randint
import prompt

name = ''

def greet():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    return (f'Hello, {name}!')


def rules_of_game():
    print('Answer "yes" if the number is prime, otherwise answer "no".')


def is_simple(x):
    numbers = range(2, x)
    for num in numbers:
      if x % num == 0:
        return False
    return True


def brain_prime():
    count = 0
    while count <= 3:
        number = randint(2,50)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ' )
        if answer == 'yes' and is_simple(number) == True or answer == 'no' and is_simple(number) == False:
            print('Correct!')
            count += 1
            if count == 3:
                print('Congratulations, ', name, '!')
                break
        else:
            print(f'"{answer}" is wrong answer ;(.\nLet\'s try again, {name}')
            break

