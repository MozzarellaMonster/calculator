# Calculations
# Project by MozzarellaMonster
import math

class Calc:
    def __init__(self):
        self.memory = [] # Holds numbers saved to memory
        self.temp = None # Holds temporary numeric value
        self.op = None # Holds current operation
    
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
    
    # Temporary Memory
    def set_temp(self, a):
        self.temp = a
    def get_temp(self):
        return self.temp

    # Memory management
    def mem_not_empty(self):
        return len(self.memory) > 0

    def store(self, a):
        self.memory.append(a)

    def delete(self):
        if self.mem_not_empty():
            self.memory.pop()
        else:
            pass

    def recall(self):
        if self.mem_not_empty():
            return self.memory[-1]
        else:
            return 0

    def clear(self):
        self.memory.clear()