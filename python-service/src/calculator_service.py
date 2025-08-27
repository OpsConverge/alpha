"""
Calculator Service for pytest unit testing
"""

import math
from typing import Union, List


class CalculatorService:
    """Service class for mathematical calculations"""
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Add two numbers"""
        return float(a + b)
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Subtract two numbers"""
        return float(a - b)
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Multiply two numbers"""
        return float(a * b)
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return float(a / b)
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> float:
        """Calculate power of a number"""
        return float(base ** exponent)
    
    def sqrt(self, number: Union[int, float]) -> float:
        """Calculate square root of a number"""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return float(math.sqrt(number))
    
    def factorial(self, n: int) -> int:
        """Calculate factorial of a number"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)
    
    def average(self, numbers: List[Union[int, float]]) -> float:
        """Calculate average of a list of numbers"""
        if not numbers:
            raise ValueError("Cannot calculate average of empty list")
        return float(sum(numbers) / len(numbers))
    
    def max_number(self, numbers: List[Union[int, float]]) -> Union[int, float]:
        """Find maximum number in a list"""
        if not numbers:
            raise ValueError("Cannot find maximum of empty list")
        return max(numbers)
    
    def min_number(self, numbers: List[Union[int, float]]) -> Union[int, float]:
        """Find minimum number in a list"""
        if not numbers:
            raise ValueError("Cannot find minimum of empty list")
        return min(numbers)
    
    def gcd(self, a: int, b: int) -> int:
        """Calculate greatest common divisor"""
        if a == 0:
            return abs(b)
        if b == 0:
            return abs(a)
        return self.gcd(b, a % b)
    
    def lcm(self, a: int, b: int) -> int:
        """Calculate least common multiple"""
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.gcd(a, b)
    
    def is_prime(self, n: int) -> bool:
        """Check if a number is prime"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
