"""
pytest unit tests for CalculatorService - Working Version
"""

import pytest
from src.calculator_service import CalculatorService


class TestCalculatorService:
    """Test class for CalculatorService"""
    
    @pytest.fixture
    def calculator(self):
        """Fixture to create CalculatorService instance"""
        return CalculatorService()
    
    class TestAddition:
        """Test addition operations"""
        
        def test_add_positive_numbers(self, calculator):
            """Test adding two positive numbers"""
            result = calculator.add(5.0, 3.0)
            assert result == 8.0
        
        def test_add_negative_numbers(self, calculator):
            """Test adding negative numbers"""
            result = calculator.add(-5.0, -3.0)
            assert result == -8.0
        
        def test_add_zero(self, calculator):
            """Test adding zero"""
            result = calculator.add(5.0, 0.0)
            assert result == 5.0
        
        @pytest.mark.parametrize("a, b, expected", [
            (1.0, 2.0, 3.0),
            (0.5, 0.3, 0.8),
            (-1.0, 1.0, 0.0),
            (100.0, 200.0, 300.0),
            (0, 0, 0.0)
        ])
        def test_add_various_numbers(self, calculator, a, b, expected):
            """Test adding various number combinations"""
            result = calculator.add(a, b)
            assert result == expected
    
    class TestSubtraction:
        """Test subtraction operations"""
        
        def test_subtract_positive_numbers(self, calculator):
            """Test subtracting two positive numbers"""
            result = calculator.subtract(5.0, 3.0)
            assert result == 2.0
        
        def test_subtract_negative_result(self, calculator):
            """Test subtraction resulting in negative number"""
            result = calculator.subtract(3.0, 5.0)
            assert result == -2.0
        
        @pytest.mark.parametrize("a, b, expected", [
            (5.0, 3.0, 2.0),
            (0.0, 0.0, 0.0),
            (10.0, 5.0, 5.0),
            (-5.0, -3.0, -2.0)
        ])
        def test_subtract_various_numbers(self, calculator, a, b, expected):
            """Test subtracting various number combinations"""
            result = calculator.subtract(a, b)
            assert result == expected
    
    class TestMultiplication:
        """Test multiplication operations"""
        
        def test_multiply_positive_numbers(self, calculator):
            """Test multiplying two positive numbers"""
            result = calculator.multiply(5.0, 3.0)
            assert result == 15.0
        
        def test_multiply_by_zero(self, calculator):
            """Test multiplication by zero"""
            result = calculator.multiply(5.0, 0.0)
            assert result == 0.0
        
        @pytest.mark.parametrize("a, b, expected", [
            (2.0, 3.0, 6.0),
            (0.5, 0.5, 0.25),
            (-2.0, 3.0, -6.0),
            (0.0, 100.0, 0.0)
        ])
        def test_multiply_various_numbers(self, calculator, a, b, expected):
            """Test multiplying various number combinations"""
            result = calculator.multiply(a, b)
            assert result == expected
    
    class TestDivision:
        """Test division operations"""
        
        def test_divide_positive_numbers(self, calculator):
            """Test dividing two positive numbers"""
            result = calculator.divide(6.0, 2.0)
            assert result == 3.0
        
        def test_divide_by_zero(self, calculator):
            """Test division by zero raises exception"""
            with pytest.raises(ValueError, match="Cannot divide by zero"):
                calculator.divide(5.0, 0.0)
        
        @pytest.mark.parametrize("a, b, expected", [
            (6.0, 2.0, 3.0),
            (10.0, 5.0, 2.0),
            (15.0, 3.0, 5.0),
            (0.0, 5.0, 0.0)
        ])
        def test_divide_various_numbers(self, calculator, a, b, expected):
            """Test dividing various number combinations"""
            result = calculator.divide(a, b)
            assert result == expected
