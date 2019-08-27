#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')
colors = ['red','orange','yellow','green','blue','violet','purple']   # Giving the choices to answer
play_again = ''    # after you played the game, player can pick either play again or not
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'):
    match_color = random.choice(colors)  # making the random choice from the top colors when player start the game
    count = 0
    color = ''
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()
        count += 1   # it adds the count as the player answered
        if (color == match_color):
            print('Correct!')
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    print('\nYou guessed it in {0} tries!'.format(count))
    if (count < best_count):
        print('This was your best guess so far!')   # memorize the best count until the player reaches the answer and tell them the best score
        best_count = count
    play_again = input("\nWould you like to play again? ").lower().strip()   # after the game, giving the player two choices either keep playing or not
print('Thanks for playing!')  #if player choose no, just say thank to play