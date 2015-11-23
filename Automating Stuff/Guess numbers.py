import random
print('Hello, what is your name? ')
name = input()
secret_number = random.randint(1, 7)
print('Well, ' + name + ' I\'m thinking of a number between 1 and 7')

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())
    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('Your guess is too high')
    else:
       break

if guess == secret_number:
    print('Good job, ' + name + ' You guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope, the number I was thinking of was ' + str(secret_number))