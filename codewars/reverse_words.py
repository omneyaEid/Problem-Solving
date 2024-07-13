"""
url: https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
des: Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
        Examples
        "This is an example!" ==> "sihT si na !elpmaxe"
        "double  spaces"      ==> "elbuod  secaps"
"""


# solution 1
def reverse_words(text):
    words = text.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


# solution 2
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))
