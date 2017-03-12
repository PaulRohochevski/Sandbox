"""
Connect the imported variable with the local, calculate the total length of the string and the number of vowels,
print each 18th position with its number starting at 18.
"""
import check_python_version
import import_this_as_var

L = import_this_as_var.L
M = "paul.rohochevski@gmail.com"
L = L + M

print("length of L = " + str(len(L)))


# Counts the number of vowels
def count(word):
    vowels = 0
    for letter in word:
        if letter.isalpha():
            if letter.lower() in 'aeiouy':
                vowels += 1

    return vowels


print ("vowels = " + str(count(L)))

each18 = L[17::18]

swap = each18.swapcase()


# Add a number to the position of letter
def letnum(word):
    num = 18
    for letter in word:
        if letter is not None:
            print ("{}".format(num) + letter)
            num += 18


letnum(swap)
