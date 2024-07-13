"""
url: https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
des: Trolls are attacking your comment section!
    A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

    Your task is to write a function that takes a string and return a new string with all vowels removed.

    For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

    Note: for this kata y isn't considered a vowel.
"""


# solution 1

def disemvowel(string_):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in string_ if char not in vowels)


# solution 2

import re


def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags=re.IGNORECASE)
