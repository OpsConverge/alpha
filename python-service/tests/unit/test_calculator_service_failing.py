"""
pytest unit tests for CalculatorService - Failing Version
"""

import pytest
from src.calculator_service import CalculatorService


class TestCalculatorService:
    """Test class for CalculatorService - Failing Version"""
    
    @pytest.fixture
    def calculator(self):
        """Fixture to create CalculatorService instance"""
        return CalculatorService()
    
    class TestAddition:
        """Test addition operations - Failing Version"""
        
        def test_add_positive_numbers(self, calculator):
            """Test adding two positive numbers - INTENTIONALLY FAILING"""
            result = calculator.add(5.0, 3.0)
            assert result == 10.0, "This test is intentionally failing - expected 10.0 but got " + str(result)
        
        def test_add_negative_numbers(self, calculator):
            """Test adding negative numbers - INTENTIONALLY FAILING"""
            result = calculator.add(-5.0, -3.0)
            assert result == 0.0, "This test is intentionally failing - expected 0.0 but got " + str(result)
        
        def test_add_zero(self, calculator):
            """Test adding zero"""
            result = calculator.add(5.0, 0.0)
            assert result == 5.0
        
        @pytest.mark.parametrize("a, b, expected", [
            (1.0, 2.0, 4.0),  # Intentionally wrong - should be 3.0
            (0.5, 0.3, 1.0),  # Intentionally wrong - should be 0.8
            (-1.0, 1.0, 2.0), # Intentionally wrong - should be 0.0
            (100.0, 200.0, 400.0), # Intentionally wrong - should be 300.0
            (0, 0, 1.0)  # Intentionally wrong - should be 0.0
        ])
        def test_add_various_numbers(self, calculator, a, b, expected):
            """Test adding various number combinations - INTENTIONALLY FAILING"""
            result = calculator.add(a, b)
            assert result == expected, f"This test is intentionally failing - expected {expected} but got {result}"
    
    class TestSubtraction:
        """Test subtraction operations - Failing Version"""
        
        def test_subtract_positive_numbers(self, calculator):
            """Test subtracting two positive numbers - INTENTIONALLY FAILING"""
            result = calculator.subtract(5.0, 3.0)
            assert result == 8.0, "This test is intentionally failing - expected 8.0 but got " + str(result)
        
        def test_subtract_negative_result(self, calculator):
            """Test subtraction resulting in negative number"""
            result = calculator.subtract(3.0, 5.0)
            assert result == -2.0
        
        @pytest.mark.parametrize("a, b, expected", [
            (5.0, 3.0, 8.0),  # Intentionally wrong - should be 2.0
            (0.0, 0.0, 1.0),  # Intentionally wrong - should be 0.0
            (10.0, 5.0, 15.0), # Intentionally wrong - should be 5.0
            (-5.0, -3.0, 2.0)  # Intentionally wrong - should be -2.0
        ])
        def test_subtract_various_numbers(self, calculator, a, b, expected):
            """Test subtracting various number combinations - INTENTIONALLY FAILING"""
            result = calculator.subtract(a, b)
            assert result == expected, f"This test is intentionally failing - expected {expected} but got {result}"
    
    class TestMultiplication:
        """Test multiplication operations - Failing Version"""
        
        def test_multiply_positive_numbers(self, calculator):
            """Test multiplying two positive numbers - INTENTIONALLY FAILING"""
            result = calculator.multiply(5.0, 3.0)
            assert result == 25.0, "This test is intentionally failing - expected 25.0 but got " + str(result)
        
        def test_multiply_by_zero(self, calculator):
            """Test multiplication by zero"""
            result = calculator.multiply(5.0, 0.0)
            assert result == 0.0
        
        @pytest.mark.parametrize("a, b, expected", [
            (2.0, 3.0, 8.0),  # Intentionally wrong - should be 6.0
            (0.5, 0.5, 1.0),  # Intentionally wrong - should be 0.25
            (-2.0, 3.0, 6.0), # Intentionally wrong - should be -6.0
            (0.0, 100.0, 100.0)  # Intentionally wrong - should be 0.0
        ])
        def test_multiply_various_numbers(self, calculator, a, b, expected):
            """Test multiplying various number combinations - INTENTIONALLY FAILING"""
            result = calculator.multiply(a, b)
            assert result == expected, f"This test is intentionally failing - expected {expected} but got {result}"
    
    class TestDivision:
        """Test division operations - Failing Version"""
        
        def test_divide_positive_numbers(self, calculator):
            """Test dividing two positive numbers - INTENTIONALLY FAILING"""
            result = calculator.divide(6.0, 2.0)
            assert result == 4.0, "This test is intentionally failing - expected 4.0 but got " + str(result)
        
        def test_divide_by_zero(self, calculator):
            """Test division by zero raises exception"""
            with pytest.raises(ValueError, match="Cannot divide by zero"):
                calculator.divide(5.0, 0.0)
        
        @pytest.mark.parametrize("a, b, expected", [
            (6.0, 2.0, 4.0),  # Intentionally wrong - should be 3.0
            (10.0, 5.0, 3.0),  # Intentionally wrong - should be 2.0
            (15.0, 3.0, 6.0),  # Intentionally wrong - should be 5.0
            (0.0, 5.0, 1.0)  # Intentionally wrong - should be 0.0
        ])
        def test_divide_various_numbers(self, calculator, a, b, expected):
            """Test dividing various number combinations - INTENTIONALLY FAILING"""
            result = calculator.divide(a, b)
            assert result == expected, f"This test is intentionally failing - expected {expected} but got {result}"
