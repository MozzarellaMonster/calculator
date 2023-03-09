# Calculations

class Calc:
    def __init__(self):
        self.memory = []
    
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print("Cannot divide by zero!")
        else:
            return a/b
    def store(self, a):
        self.memory.append(a)
