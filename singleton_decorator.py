def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Single(object):
    def __init__(self, name):
        self.name = name


a = Single("Cat")
b = Single("Dog")

print(a.name)
print(b.name)

assert (b.name == "Cat")
assert id(a) == id(b)
