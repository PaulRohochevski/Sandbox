"""
Create an function int_to_words that translates integers to words.
For a given positive integer convert it into its English representation. All words are lower case and are separated
with one space. No trailing spaces are allowed. Integer will be up to a million (including).

Example: int_to_words(15) # => 'fifteen'

Writing of the word 'and' isn't enforced, but very welcomed.

Example: int_to_words(12356) # => 'twelve thousand three hundred and fifty six'
"""
import check_python_version
import num2words

num_to_word = num2words.num2words


# Replace "," and "-" so that there was everywhere 1 space
def int_to_word(some_int):
    word = num_to_word(some_int)
    changed_word = word.replace(",", "")
    result_word = changed_word.replace("-", " ")
    print (result_word)


int_to_word(1234567)
