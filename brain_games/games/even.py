import prompt
from random import randint

name = ''

def greet():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I  have your name? ')
    return (f'Hello, {name}!')


def rules_of_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):
  return number % 2 == 0


def guess_even_number():
  count = 0
  while count <= 3:
    random_num = randint(0,100)
    print(f'Question: {random_num}')
    answer = prompt.string('Your answer: ')
    if (is_even(random_num) == True and answer == 'yes') or (is_even(random_num) == False and answer == 'no'):
      print('Correct!')
      count += 1
    if count == 3:
      print('Congratulations, ', name, '!')
      break
    if (is_even(random_num) == True and answer == 'no'):
      print(f'"{answer}" is wrong answer ;(. Correct answer was "yes".\nLet\'s try again, {name}')
      break
    if (is_even(random_num) == False and answer == 'yes'):
      print(f'"{answer}" is wrong answer ;(. Correct answer was "no".\nLet\'s try again, {name}')
      break
    if answer != 'yes' and answer != 'no':
      print(f'"{answer}" is wrong answer ;(.\nLet\'s try again, {name}')
      break

