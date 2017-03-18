"""
We iterate over the number, leaving its odd indices. At the output, we also get the integer.
"""


# Leaved only the necessary indexes
class A_is_int(int):
    def __init__(self, var):
        self.var = var

    def __iter__(self):
        for _ in str(self.var)[1::2]:
            yield _


a = 1234
my_var = A_is_int(a)

# Check type of our class
print(type(my_var))
print(issubclass(A_is_int, int))

# Output condition
assert (isinstance(a, int))
for i in my_var:
    print(i)
