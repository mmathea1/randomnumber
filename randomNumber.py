from random import randint

random = randint(1,100)
guess = int(input("Guess a number between 0 and 100: "))
    
if guess < random:
    print 'Sorry but %d is LESSER than the number' % guess
        
elif guess > random:
    print 'Sorry but %d is GREATER than the number' % guess
        
elif guess == random:
    print 'Yes! You got it! Your guess, %d is %d ' %guess %random
       
else:
    print 'I didnt catch that, try again please'
 
