"""
Create a generator of its own name that would endlessly print out the name by letters and, correspondingly, the value
of the letter in Unicode, until one of the following conditions occurs:
1. There will be a letter 'z'
2. There will be more than 100 characters
"""
import check_python_version


# Create a generator of the name
def name_gen(name):
    while True:
        for item in name:
            yield item


my_infinite_name = name_gen("Paul")


# Set the condition under which the generator will stop and add their number in Unicode to the letters
def stop_condition(infinite_name_generator):
    iterations_count = 0
    while True:
        for letter in infinite_name_generator:
            if iterations_count >= 100 or letter == "z":
                break
            yield (letter, ord(letter))
            iterations_count += 1


name_gen_with_condition = stop_condition(my_infinite_name)

for item in name_gen_with_condition:
    print (item)
