"""
Depending on the input parameter, the class can give the temperature in different scales or not at all.
"""
import check_python_version


class Termometr(object):
    def __init__(self, temperature):
        self._temperature = temperature

    def __getattr__(self, item):
        if item == "kelvin":
            return self._temperature + 273
        elif item == "fahrengeit":
            return self._temperature * 1.8 + 32
        elif item == "celsius":
            return self._temperature
        else:
            return "Sorry"


t = Termometr(100)
print(t.celsius)
print(t.fahrengeit)
print(t.kelvin)
print(t.parrots)
