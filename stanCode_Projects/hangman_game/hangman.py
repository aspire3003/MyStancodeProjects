"""
File: hangman.py
Name:David Lin
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():

    """
    Before first guess
    """
    ans = random_word()
    dashed_ans = first_dashed_word(ans)
    print(ans)
    print('The word looks like : ' + dashed_ans)
    print('You have ' + str(N_TURNS) + ' guesses left')

    """
    Start guessing
    """
    ori_turns_count = N_TURNS
    while True:
        guess = input('Your guess: ')
        if not guess.isalpha() or len(guess) != 1:
            print('illegal format')
        else:
            guess = guess.upper()
            if guess_check(ans, guess) == False :
                ori_turns_count -= 1
            print('You have ' + str(ori_turns_count) + ' guesses left')
            dashed_ans = dashed_word(ans, guess, dashed_ans)
            print('The word looks like : ' + str(dashed_ans))
            if ori_turns_count == 0 :
                print('You are completely hung :(')
                print('The word is ' + ans)
                break
            if dashed_ans == ans:
                print('You Win!!')
                print('The word was: ' + ans)
                break

def first_dashed_word(ans):
    masked_str = ''
    for i in range(len(ans)):
        masked_str += '-'
    return masked_str


def dashed_word(ans, guess, dashed_ans):
    j = 0   # dashed
    temp_idx = -1 # marginal condition index
    while True:
        substitute_str = ''
        ans_idx = ans[j:].find(guess)  # find guess in the answer
        temp_idx += (ans_idx+1)        # GLAMOROUS 找到的
        if ans_idx != -1:              # guess exist in the answer string
            for i in range(len(dashed_ans)):   # assign new chr
                if temp_idx != i:       # if different index assign same letter as before the guessing
                    substitute_str += dashed_ans[i]
                else:                  # same index assign the guess
                    substitute_str += guess
            dashed_ans = substitute_str # assign the after-guessed str back
            j += (ans_idx+1)    # after adding the all letters , cut out the str before the next index of the guess
        else:
            break
    return dashed_ans


def guess_check(ans, guess):
    correct_bool = False
    if guess not in ans:
        print('There is no ' + guess + '\'s in the word')
        return correct_bool
    else:
        correct_bool = True
        print('You are correct !')
        return correct_bool



def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
