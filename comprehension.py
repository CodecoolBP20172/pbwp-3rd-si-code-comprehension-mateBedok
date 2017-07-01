import random  # imports random module

guessesTaken = 0  # assign 0 to guessesTaken variable

print('Hello! What is your name?')  # prints out msg
myName = input()  # assign a user input to myName variable

number = random.randint(1, 20)  # assign a random integer from 1 to 20 to number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # prints msg with myName variable

while guessesTaken < 6:  # loop until variable is smaller than 6
    print('Take a guess.')  # prints msg
    guess = input()  # assign a user input to guess variable
    guess = int(guess)  # converts string variable to integer

    guessesTaken += 1  # adds 1 to variable

    if guess < number:  # executes if guess var is smaller than number var
        print('Your guess is too low.')  # prints msg

    if guess > number:  # executes if guess var is greater than number var
        print('Your guess is too high.')  # prints msg

    if guess == number:  # executes if guess var equals number var
        break # breaks the loop

if guess == number:  # executes if guess var is equal to number var
    guessesTaken = str(guessesTaken)  # converts integer variable to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # prints msg with 2 variables

if guess != number:  # executes if guess var is not equal to number var
    number = str(number)  # converts integer variable to string
    print('Nope. The number I was thinking of was ' + number)  # prints msg with number variable
