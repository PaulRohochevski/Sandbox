"""
Example of decorator.
"""


def decorator(debug=False):
    def higher_wrapper(func):
        def wrapper(some_string):
            print ("Called before main function")
            if debug:
                print ("Intersepted arg: {}".format(some_string))
            func(some_string)
            print ("Called after main function")

        return wrapper

    return higher_wrapper


@decorator(debug=True)
def function(some_string):
    print ("I was called with string {}!".format(some_string))

function("COOL")