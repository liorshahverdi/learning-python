import random
guess = ''
options = ['heads', 'tails']
while guess not in options:
	print('Guess the coin toss! Enter heads or tails:')
	guess = str(raw_input())

toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 0 and guess == 'tails':
    print('You got it!')
elif toss == 1 and guess == 'heads':
	print('You got it!')
else:
    print('Nope! Guess again!')
    guess = str(raw_input())
    while guess not in options:
    	guess = str(raw_input())
    if toss == 0 and guess == 'tails' or toss == 1 and guess == 'heads':
    	print('You got it!')
    else:
		print('Nope! You\'re really bad at this game.')