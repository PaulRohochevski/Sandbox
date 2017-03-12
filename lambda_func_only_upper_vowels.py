"""
Create a lambda function that would take a name at the input, and at the output receive vowels in uppercase.
"""
import check_python_version

name = "Paul"
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
# Put away all consonants
only_vowels = list(filter(lambda x: x in vowels, name))
# Bring all vowels to the upper case
upper_vowels = list(map(lambda x: x.upper(), only_vowels))

print(upper_vowels)
