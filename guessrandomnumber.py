import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a nummber 1 and{x}:'))
        if guess < random_number:
            print('Sorry guess agai too low')
        elif guess > random_number:
            print('sorry  guess agai too high')

            print(f'Yay congrates you have guessed the number {random_number}')
            guess(10)
            