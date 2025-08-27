package com.example.unit;

import com.example.CalculatorService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("CalculatorService Unit Tests")
class CalculatorServiceTest {

    private CalculatorService calculatorService;

    @BeforeEach
    void setUp() {
        calculatorService = new CalculatorService();
    }

    @Nested
    @DisplayName("Addition Tests")
    class AdditionTests {

        @Test
        @DisplayName("Should add two positive numbers correctly")
        void shouldAddTwoPositiveNumbers() {
            // Given
            double a = 5.0;
            double b = 3.0;

            // When
            double result = calculatorService.add(a, b);

            // Then
            assertEquals(8.0, result, 0.001);
        }

        @Test
        @DisplayName("Should add negative numbers correctly")
        void shouldAddNegativeNumbers() {
            // Given
            double a = -5.0;
            double b = -3.0;

            // When
            double result = calculatorService.add(a, b);

            // Then
            assertEquals(-8.0, result, 0.001);
        }

        @Test
        @DisplayName("Should add zero correctly")
        void shouldAddZero() {
            // Given
            double a = 5.0;
            double b = 0.0;

            // When
            double result = calculatorService.add(a, b);

            // Then
            assertEquals(5.0, result, 0.001);
        }

        @ParameterizedTest
        @CsvSource({
            "1.0, 2.0, 3.0",
            "0.5, 0.3, 0.8",
            "-1.0, 1.0, 0.0",
            "100.0, 200.0, 300.0"
        })
        @DisplayName("Should add various number combinations")
        void shouldAddVariousNumbers(double a, double b, double expected) {
            // When
            double result = calculatorService.add(a, b);

            // Then
            assertEquals(expected, result, 0.001);
        }
    }

    @Nested
    @DisplayName("Subtraction Tests")
    class SubtractionTests {

        @Test
        @DisplayName("Should subtract two positive numbers correctly")
        void shouldSubtractTwoPositiveNumbers() {
            // Given
            double a = 5.0;
            double b = 3.0;

            // When
            double result = calculatorService.subtract(a, b);

            // Then
            assertEquals(2.0, result, 0.001);
        }

        @Test
        @DisplayName("Should handle negative result")
        void shouldHandleNegativeResult() {
            // Given
            double a = 3.0;
            double b = 5.0;

            // When
            double result = calculatorService.subtract(a, b);

            // Then
            assertEquals(-2.0, result, 0.001);
        }

        @ParameterizedTest
        @CsvSource({
            "5.0, 3.0, 2.0",
            "0.0, 0.0, 0.0",
            "10.0, 5.0, 5.0",
            "-5.0, -3.0, -2.0"
        })
        @DisplayName("Should subtract various number combinations")
        void shouldSubtractVariousNumbers(double a, double b, double expected) {
            // When
            double result = calculatorService.subtract(a, b);

            // Then
            assertEquals(expected, result, 0.001);
        }
    }

    @Nested
    @DisplayName("Multiplication Tests")
    class MultiplicationTests {

        @Test
        @DisplayName("Should multiply two positive numbers correctly")
        void shouldMultiplyTwoPositiveNumbers() {
            // Given
            double a = 5.0;
            double b = 3.0;

            // When
            double result = calculatorService.multiply(a, b);

            // Then
            assertEquals(15.0, result, 0.001);
        }

        @Test
        @DisplayName("Should handle multiplication by zero")
        void shouldHandleMultiplicationByZero() {
            // Given
            double a = 5.0;
            double b = 0.0;

            // When
            double result = calculatorService.multiply(a, b);

            // Then
            assertEquals(0.0, result, 0.001);
        }

        @ParameterizedTest
        @CsvSource({
            "2.0, 3.0, 6.0",
            "0.5, 0.5, 0.25",
            "-2.0, 3.0, -6.0",
            "0.0, 100.0, 0.0"
        })
        @DisplayName("Should multiply various number combinations")
        void shouldMultiplyVariousNumbers(double a, double b, double expected) {
            // When
            double result = calculatorService.multiply(a, b);

            // Then
            assertEquals(expected, result, 0.001);
        }
    }

    @Nested
    @DisplayName("Division Tests")
    class DivisionTests {

        @Test
        @DisplayName("Should divide two positive numbers correctly")
        void shouldDivideTwoPositiveNumbers() {
            // Given
            double a = 6.0;
            double b = 2.0;

            // When
            double result = calculatorService.divide(a, b);

            // Then
            assertEquals(3.0, result, 0.001);
        }

        @Test
        @DisplayName("Should throw exception when dividing by zero")
        void shouldThrowExceptionWhenDividingByZero() {
            // Given
            double a = 5.0;
            double b = 0.0;

            // When & Then
            ArithmeticException exception = assertThrows(ArithmeticException.class, () -> {
                calculatorService.divide(a, b);
            });

            assertEquals("Division by zero is not allowed", exception.getMessage());
        }

        @ParameterizedTest
        @CsvSource({
            "6.0, 2.0, 3.0",
            "5.0, 2.0, 2.5",
            "0.0, 5.0, 0.0",
            "-6.0, 2.0, -3.0"
        })
        @DisplayName("Should divide various number combinations")
        void shouldDivideVariousNumbers(double a, double b, double expected) {
            // When
            double result = calculatorService.divide(a, b);

            // Then
            assertEquals(expected, result, 0.001);
        }
    }

    @Nested
    @DisplayName("Power Tests")
    class PowerTests {

        @Test
        @DisplayName("Should calculate power correctly")
        void shouldCalculatePowerCorrectly() {
            // Given
            double base = 2.0;
            double exponent = 3.0;

            // When
            double result = calculatorService.power(base, exponent);

            // Then
            assertEquals(8.0, result, 0.001);
        }

        @Test
        @DisplayName("Should handle power of zero")
        void shouldHandlePowerOfZero() {
            // Given
            double base = 5.0;
            double exponent = 0.0;

            // When
            double result = calculatorService.power(base, exponent);

            // Then
            assertEquals(1.0, result, 0.001);
        }

        @ParameterizedTest
        @CsvSource({
            "2.0, 3.0, 8.0",
            "5.0, 0.0, 1.0",
            "2.0, -1.0, 0.5",
            "0.0, 5.0, 0.0"
        })
        @DisplayName("Should calculate various power combinations")
        void shouldCalculateVariousPowerCombinations(double base, double exponent, double expected) {
            // When
            double result = calculatorService.power(base, exponent);

            // Then
            assertEquals(expected, result, 0.001);
        }
    }

    @Nested
    @DisplayName("Square Root Tests")
    class SquareRootTests {

        @Test
        @DisplayName("Should calculate square root correctly")
        void shouldCalculateSquareRootCorrectly() {
            // Given
            double number = 16.0;

            // When
            double result = calculatorService.sqrt(number);

            // Then
            assertEquals(4.0, result, 0.001);
        }

        @Test
        @DisplayName("Should throw exception for negative number")
        void shouldThrowExceptionForNegativeNumber() {
            // Given
            double number = -4.0;

            // When & Then
            IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> {
                calculatorService.sqrt(number);
            });

            assertEquals("Cannot calculate square root of negative number", exception.getMessage());
        }

        @ParameterizedTest
        @ValueSource(doubles = {0.0, 1.0, 4.0, 9.0, 16.0, 25.0})
        @DisplayName("Should calculate square root of perfect squares")
        void shouldCalculateSquareRootOfPerfectSquares(double number) {
            // When
            double result = calculatorService.sqrt(number);

            // Then
            double expected = Math.sqrt(number);
            assertEquals(expected, result, 0.001);
        }
    }

    @Nested
    @DisplayName("Factorial Tests")
    class FactorialTests {

        @Test
        @DisplayName("Should calculate factorial correctly")
        void shouldCalculateFactorialCorrectly() {
            // Given
            int n = 5;

            // When
            long result = calculatorService.factorial(n);

            // Then
            assertEquals(120L, result);
        }

        @Test
        @DisplayName("Should handle factorial of zero")
        void shouldHandleFactorialOfZero() {
            // Given
            int n = 0;

            // When
            long result = calculatorService.factorial(n);

            // Then
            assertEquals(1L, result);
        }

        @Test
        @DisplayName("Should handle factorial of one")
        void shouldHandleFactorialOfOne() {
            // Given
            int n = 1;

            // When
            long result = calculatorService.factorial(n);

            // Then
            assertEquals(1L, result);
        }

        @Test
        @DisplayName("Should throw exception for negative number")
        void shouldThrowExceptionForNegativeNumber() {
            // Given
            int n = -5;

            // When & Then
            IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> {
                calculatorService.factorial(n);
            });

            assertEquals("Factorial is not defined for negative numbers", exception.getMessage());
        }

        @ParameterizedTest
        @CsvSource({
            "0, 1",
            "1, 1",
            "2, 2",
            "3, 6",
            "4, 24",
            "5, 120"
        })
        @DisplayName("Should calculate factorial for various numbers")
        void shouldCalculateFactorialForVariousNumbers(int n, long expected) {
            // When
            long result = calculatorService.factorial(n);

            // Then
            assertEquals(expected, result);
        }
    }

    @Nested
    @DisplayName("Array Operations Tests")
    class ArrayOperationsTests {

        @Test
        @DisplayName("Should calculate average correctly")
        void shouldCalculateAverageCorrectly() {
            // Given
            double[] numbers = {1.0, 2.0, 3.0, 4.0, 5.0};

            // When
            double result = calculatorService.average(numbers);

            // Then
            assertEquals(3.0, result, 0.001);
        }

        @Test
        @DisplayName("Should throw exception for empty array average")
        void shouldThrowExceptionForEmptyArrayAverage() {
            // Given
            double[] numbers = {};

            // When & Then
            IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> {
                calculatorService.average(numbers);
            });

            assertEquals("Cannot calculate average of empty array", exception.getMessage());
        }

        @Test
        @DisplayName("Should find maximum correctly")
        void shouldFindMaximumCorrectly() {
            // Given
            double[] numbers = {1.0, 5.0, 3.0, 9.0, 2.0};

            // When
            double result = calculatorService.max(numbers);

            // Then
            assertEquals(9.0, result, 0.001);
        }

        @Test
        @DisplayName("Should find minimum correctly")
        void shouldFindMinimumCorrectly() {
            // Given
            double[] numbers = {1.0, 5.0, 3.0, 9.0, 2.0};

            // When
            double result = calculatorService.min(numbers);

            // Then
            assertEquals(1.0, result, 0.001);
        }
    }
}
