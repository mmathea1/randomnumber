from random import randint

random = randint(0,100)
print random
guess = int(input("Guess a number between 0 and 100: "))
if guess < random:
    print 'Sorry but ' +guess+ 'is lower than the number'
elif guess > random:
    print 'Sorry but ' +guess+ 'is greater than the number'
elif guess == random:
    print 'Yes! You got it! Your guess, ' +guess+ ' is ' + random
else:
    print 'I didnt catch that, try again please'
