"""
Create an autocomplete function that will take in an input string and a dictionary array and return the values from
the dictionary that start with the input string. If there are more than 5 matches, restrict your output to the first
5 results. If there are no matches, return an empty array. Any input that is NOT a letter should be treated as if it is
not there. For example, an input of "$%^" should be treated as "" and an input of "ab*&1cd" should be treated as "abcd".

Example: autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']

For this assignment, the dictionary will always be a valid array of strings. Please return all results in the order
given in the dictionary, even if they're not always alphabetical. The search should NOT be case sensitive, but the case
of the word should be preserved when it's returned. For example, "Apple" and "airport" would both return for an input
of 'a'. However, they should return as "Apple" and "airport" in their original cases.
"""
import check_python_version

my_dict = ["airport", "Ball", "Airplan", "apple", "aider", "Phone", "Aircraft", "aircraft", "Gun", "Aigrette"]


# Return a string that consists only of letters
def valid_arg(some_string):
    result_list = []
    for item in some_string:
        if item.isalpha():
            result_list.append(item)
    result_string = str("".join(result_list))
    return result_string


# Return the first 5 results from the dictionary, which begins with a string, ignoring the case
def autocomplete(args, some_dict):
    filtred_arg = valid_arg(args)
    result_list = []
    for word in some_dict:
        lower_word = word.lower()
        filtred_word = valid_arg(word)
        lower_filtred_word = valid_arg(lower_word)
        lower_filtred_arg = filtred_arg.lower()
        if lower_filtred_word.startswith(lower_filtred_arg):
            result_list.append(filtred_word)
    return result_list[:5]


print(autocomplete("ai123)*-+/", my_dict))
