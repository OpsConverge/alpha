"""
pytest unit tests for CalculatorService
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
        
        # def test_.*_failing(self, calculator):
            """Test adding two positive numbers - INTENTIONALLY FAILING"""
            result = calculator.add(5.0, 3.0)
            assert result == 10.0  # This will fail - should be 8.0
        
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
        
        def test_divide_by_zero_raises_error(self, calculator):
            """Test that division by zero raises ValueError"""
            with pytest.raises(ValueError, match="Division by zero is not allowed"):
                calculator.divide(5.0, 0.0)
        
        @pytest.mark.parametrize("a, b, expected", [
            (6.0, 2.0, 3.0),
            (5.0, 2.0, 2.5),
            (0.0, 5.0, 0.0),
            (-6.0, 2.0, -3.0)
        ])
        def test_divide_various_numbers(self, calculator, a, b, expected):
            """Test dividing various number combinations"""
            result = calculator.divide(a, b)
            assert result == expected
    
    class TestPower:
        """Test power operations"""
        
        def test_power_calculation(self, calculator):
            """Test power calculation"""
            result = calculator.power(2.0, 3.0)
            assert result == 8.0
        
        def test_power_of_zero(self, calculator):
            """Test power of zero"""
            result = calculator.power(5.0, 0.0)
            assert result == 1.0
        
        @pytest.mark.parametrize("base, exponent, expected", [
            (2.0, 3.0, 8.0),
            (5.0, 0.0, 1.0),
            (2.0, -1.0, 0.5),
            (0.0, 5.0, 0.0)
        ])
        def test_power_various_combinations(self, calculator, base, exponent, expected):
            """Test various power combinations"""
            result = calculator.power(base, exponent)
            assert result == expected
    
    class TestSquareRoot:
        """Test square root operations"""
        
        def test_square_root_calculation(self, calculator):
            """Test square root calculation"""
            result = calculator.sqrt(16.0)
            assert result == 4.0
        
        def test_square_root_negative_raises_error(self, calculator):
            """Test that square root of negative number raises ValueError"""
            with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
                calculator.sqrt(-4.0)
        
        @pytest.mark.parametrize("number, expected", [
            (0.0, 0.0),
            (1.0, 1.0),
            (4.0, 2.0),
            (9.0, 3.0),
            (16.0, 4.0),
            (25.0, 5.0)
        ])
        def test_square_root_perfect_squares(self, calculator, number, expected):
            """Test square root of perfect squares"""
            result = calculator.sqrt(number)
            assert result == expected
    
    class TestFactorial:
        """Test factorial operations"""
        
        def test_factorial_calculation(self, calculator):
            """Test factorial calculation"""
            result = calculator.factorial(5)
            assert result == 120
        
        def test_factorial_of_zero(self, calculator):
            """Test factorial of zero"""
            result = calculator.factorial(0)
            assert result == 1
        
        def test_factorial_of_one(self, calculator):
            """Test factorial of one"""
            result = calculator.factorial(1)
            assert result == 1
        
        def test_factorial_negative_raises_error(self, calculator):
            """Test that factorial of negative number raises ValueError"""
            with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
                calculator.factorial(-5)
        
        @pytest.mark.parametrize("n, expected", [
            (0, 1),
            (1, 1),
            (2, 2),
            (3, 6),
            (4, 24),
            (5, 120)
        ])
        def test_factorial_various_numbers(self, calculator, n, expected):
            """Test factorial for various numbers"""
            result = calculator.factorial(n)
            assert result == expected
    
    class TestListOperations:
        """Test operations on lists of numbers"""
        
        def test_average_calculation(self, calculator):
            """Test average calculation"""
            result = calculator.average([1, 2, 3, 4, 5])
            assert result == 3.0
        
        def test_average_empty_list_raises_error(self, calculator):
            """Test that average of empty list raises ValueError"""
            with pytest.raises(ValueError, match="Cannot calculate average of empty list"):
                calculator.average([])
        
        def test_max_number(self, calculator):
            """Test finding maximum number"""
            result = calculator.max_number([1, 5, 3, 9, 2])
            assert result == 9
        
        def test_max_number_empty_list_raises_error(self, calculator):
            """Test that max of empty list raises ValueError"""
            with pytest.raises(ValueError, match="Cannot find maximum of empty list"):
                calculator.max_number([])
        
        def test_min_number(self, calculator):
            """Test finding minimum number"""
            result = calculator.min_number([1, 5, 3, 9, 2])
            assert result == 1
        
        def test_min_number_empty_list_raises_error(self, calculator):
            """Test that min of empty list raises ValueError"""
            with pytest.raises(ValueError, match="Cannot find minimum of empty list"):
                calculator.min_number([])
    
    class TestGCD:
        """Test greatest common divisor operations"""
        
        def test_gcd_positive_numbers(self, calculator):
            """Test GCD of positive numbers"""
            result = calculator.gcd(48, 18)
            assert result == 6
        
        def test_gcd_with_zero(self, calculator):
            """Test GCD with zero"""
            result = calculator.gcd(0, 5)
            assert result == 5
        
        @pytest.mark.parametrize("a, b, expected", [
            (48, 18, 6),
            (54, 24, 6),
            (7, 13, 1),
            (0, 0, 0)
        ])
        def test_gcd_various_numbers(self, calculator, a, b, expected):
            """Test GCD for various number combinations"""
            result = calculator.gcd(a, b)
            assert result == expected
    
    class TestLCM:
        """Test least common multiple operations"""
        
        def test_lcm_positive_numbers(self, calculator):
            """Test LCM of positive numbers"""
            result = calculator.lcm(12, 18)
            assert result == 36
        
        def test_lcm_with_zero(self, calculator):
            """Test LCM with zero"""
            result = calculator.lcm(0, 5)
            assert result == 0
        
        @pytest.mark.parametrize("a, b, expected", [
            (12, 18, 36),
            (8, 12, 24),
            (7, 13, 91),
            (0, 0, 0)
        ])
        def test_lcm_various_numbers(self, calculator, a, b, expected):
            """Test LCM for various number combinations"""
            result = calculator.lcm(a, b)
            assert result == expected
    
    class TestPrime:
        """Test prime number operations"""
        
        def test_is_prime_true(self, calculator):
            """Test that prime numbers return True"""
            assert calculator.is_prime(2) is True
            assert calculator.is_prime(3) is True
            assert calculator.is_prime(17) is True
        
        def test_is_prime_false(self, calculator):
            """Test that non-prime numbers return False"""
            assert calculator.is_prime(1) is False
            assert calculator.is_prime(4) is False
            assert calculator.is_prime(15) is False
        
        @pytest.mark.parametrize("n, expected", [
            (2, True),
            (3, True),
            (4, False),
            (5, True),
            (6, False),
            (7, True),
            (8, False),
            (9, False),
            (10, False),
            (11, True)
        ])
        def test_is_prime_various_numbers(self, calculator, n, expected):
            """Test is_prime for various numbers"""
            result = calculator.is_prime(n)
            assert result == expected
