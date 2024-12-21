# operations.py
class Add:
    def execute(self, a, b):
        return a + b

class Subtract:
    def execute(self, a, b):
        return a - b

class Multiply:
    def execute(self, a, b):
        return a * b

class Divide:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("На нуль ділити не можна!")
        return a / b
