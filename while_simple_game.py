Secret_number = 7
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess number: '))
    guess_count += 1
    if guess == Secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed!')
