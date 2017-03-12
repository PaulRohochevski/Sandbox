"""
Function to_weird that accepts any number of strings, and returns the same strings with all even indexed characters
in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained
is zero based, so the index 0 is even, therefore that character should be upper cased.
The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present
if there are multiple words. Words will be separated by a single space(' ').

Examples:
to_weird ("String") -> returns "StRiNg"
to_weird ("Weird string case") -> returns "WeIrD StRiNg CaSe"
"""


# Translate all even-numbered positions and zero to uppercase
def swap_letters(word):
    result_str = ""
    index = 0
    for letters in word:
        if (index % 2 == 0):
            result_str += letters.upper()
        else:
            result_str += letters.lower()
        index += 1
    return result_str


# Separate, and then connects words to strings with the required case
def to_weird(some_str):
    splited_string = some_str.split()
    result_string = ""
    for variable_word in splited_string:
        result_string += swap_letters(variable_word) + " "
    return result_string


print (to_weird("String"))
print(to_weird("Weird string case"))
