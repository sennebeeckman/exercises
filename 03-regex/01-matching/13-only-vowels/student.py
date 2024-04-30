import re

def only_vowels(string):
    return re.fullmatch("(a|e|u|i|o)*", string)
