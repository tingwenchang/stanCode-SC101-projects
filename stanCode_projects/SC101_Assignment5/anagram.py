"""
File: anagram.py
Name: Tingwen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO: This function recursively finds all the anagram(s) for the word input by user
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')

    while True:
        word = input('Find anagram for: ')
        if word == EXIT:
            break
        else:
            start = time.time()
            python_list = read_dictionary(word)
            find_anagrams(word, python_list)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary(s):
    """
    :param s: str, the word that the user put in
    :return: list, the word in dictionary.txt
    """
    python_list = []
    with open(FILE, "r") as f:
        for data in f:
            data = data.strip()
            if len(s) == len(data):
                python_list.append(data)
    return python_list


def find_anagrams(s, python_list):
    """
    :param s: str, the word that the user put in
    :param python_list: list, the word in dictionary.txt
    :return:
    """
    word_list = []
    current_s = ''
    helper(len(s), s, word_list, python_list, current_s)
    print(len(word_list), 'anagrams: ', word_list)


def helper(len_s, s, word_list, python_list, current_s):
    """
    :param len_s: int, the word length that the user put in
    :param s: str, the word that the user put in
    :param word_list: list, the anagram(s) of word that the user put in
    :param python_list: list, the word in dictionary.txt
    :param current_s: str, the start letter(s) of the word
    :return:
    """
    # base case
    if len(current_s) == len_s:
        if current_s in python_list and current_s not in word_list:
            print("Searching ...")
            print("Found: ", current_s)
            word_list.append(current_s)

    # Backtracking
    else:
        for i in range(len(s)):
            current_s += s[i]
            if has_prefix(current_s, python_list) is True:
                helper(len_s, s[:i] + s[i+1:], word_list, python_list, current_s)
            current_s = current_s[:-1]


def has_prefix(sub_s, python_list):
    """
    :param sub_s: str, the start letter(s) of the word
    :param python_list: list, the word in dictionary.txt
    :return: bool, whether the word is in python_list or not
    """
    for word in python_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
