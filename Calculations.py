# Calculations
# Project by MozzarellaMonster
import math

class Calc:
    def __init__(self):
        self.memory = []
    
    def read(self):
        # Implement reading of the text input here
        pass

    # Arithmetic operations
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero!"
        return a/b
        
    # More complex operations
    def root(self, a):
        return math.sqrt(a)
    
    def square(self, a):
        return pow(a, 2)
    
    def frac(self, a):
        if a == 0:
            return "Cannot divide by zero!"
        return 1/a

    # Memory management
    def store(self, a):
        self.memory.append(a)

    def delete(self):
        self.memory.pop()

    def recall(self):
        return self.memory[-1]

    def clear(self):
        self.memory.clear()