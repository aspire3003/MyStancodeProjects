"""
File: boggle.py
Name: David Lin
----------------------------------------
This is the boggle game which can find out the all words combination from the dictionary through a 2D string input
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    word_lst = []
    lst_of_str = []
    str_per_input = ""
    row_count = 1
    switch = True
    # Input constraint and make input as a list with 4 strings
    while True:
        if row_count <= 4:
            s = (str(input(str(row_count) + ' row of letters : '))).lower()
            row_count += 1
            if len(s) < 7:
                print('Illegal format')
                switch = False
                break
            elif len(s) > 7:
                if s[len(s)-1].isalpha():
                    print('Illegal format')
                    switch = False
                    break
            elif len(s) == 7:
                for i in range(0, len(s)-1, 2):
                    if s[i].isalpha() and s[i+1].isspace():
                        pass
                    else:
                        print('Illegal format')
                        switch = False
                        break
                for ch in s:
                    if ch.isalpha():
                        str_per_input += ch
                lst_of_str.append(str_per_input)
                str_per_input = ""
        else:
            break
    # boggle algo start
    if switch:
        start = time.time()
        read_dictionary(word_lst)
        count = boggle(lst_of_str, word_lst)
        print("There are " + str(count) + " words in total.")
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(lst_of_str, word_lst):
    d = {}
    tup_list = []   # used tuple list
    anagrams_lst = []   # all found anagrams

    # make dictionary for recursion
    for i in range(4):
        for j in range(4):
            tup = (i, j)
            d[tup] = lst_of_str[i][j]
    for tup, ch in d.items():
        tup_list.append(tup)

    # check each (x,y) from input , total 16 start point
    for i in range(4):
        for j in range(4):
            boggle_helper(d, i, j, word_lst, "", [], anagrams_lst)
    return len(anagrams_lst)


def boggle_helper(d, i, j, word_lst, anagram, recur_checked_tup_lst, anagrams_lst):
    """
    d = {}
    key is tuple , val is ch. Ex: (0,0) : f  , (1,0) : y ...etc
      0 1 2 3
    0 f y c l
    1 i o m g
    2 o r i l
    3 h j h u
    """
    # Base case
    if len(anagram) >= 4 and anagram in word_lst:
        if anagram not in anagrams_lst:  # prevent print duplicate words
            print("Found: " + '"' + anagram + '"')
            anagrams_lst.append(anagram)
    # Choose
    tup = (i, j)
    anagram += d[tup]
    recur_checked_tup_lst.append(tup)  # append used tuple
    # adding (-1 , 0 , 1) as new tuple to search neighbor ch
    for a in range(-1, 2):
        for b in range(-1, 2):
            m = i+a
            n = j+b
            if 0 <= m <= 3 and 0 <= n <= 3:     # boundary condition
                if (m, n) in recur_checked_tup_lst:
                    pass
                # Explore
                else:
                    if has_prefix(anagram, word_lst):
                        boggle_helper(d, m, n, word_lst, anagram, recur_checked_tup_lst, anagrams_lst)
    # Un-choose
    recur_checked_tup_lst.pop()


def read_dictionary(word_lst):
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for words in f:
            words = words.strip()
            word_lst.append(words)
    return word_lst


def has_prefix(sub_s, word_lst):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in word_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
