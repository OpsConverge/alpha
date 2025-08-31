package com.example.unit;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import static org.junit.jupiter.api.Assertions.*;

import com.example.CalculatorService;

@DisplayName("Calculator Service Unit Tests - Failing Version")
public class CalculatorServiceTestFailing {
    
    private CalculatorService calculator;
    
    @BeforeEach
    void setUp() {
        calculator = new CalculatorService();
    }
    
    @Test
    @DisplayName("Should add two positive numbers correctly - INTENTIONALLY FAILING")
    void shouldAddTwoPositiveNumbers() {
        double result = calculator.add(5.0, 3.0);
        assertEquals(10.0, result, "This test is intentionally failing - expected 10.0 but got " + result);
    }
    
    @Test
    @DisplayName("Should add negative numbers correctly - INTENTIONALLY FAILING")
    void shouldAddNegativeNumbers() {
        double result = calculator.add(-5.0, -3.0);
        assertEquals(0.0, result, "This test is intentionally failing - expected 0.0 but got " + result);
    }
    
    @Test
    @DisplayName("Should add zero correctly")
    void shouldAddZero() {
        double result = calculator.add(5.0, 0.0);
        assertEquals(5.0, result, "5.0 + 0.0 should equal 5.0");
    }
    
    @ParameterizedTest
    @CsvSource({
        "1.0, 2.0, 4.0",  // Intentionally wrong - should be 3.0
        "0.5, 0.3, 1.0",  // Intentionally wrong - should be 0.8
        "-1.0, 1.0, 2.0", // Intentionally wrong - should be 0.0
        "100.0, 200.0, 400.0", // Intentionally wrong - should be 300.0
        "0, 0, 1.0"  // Intentionally wrong - should be 0.0
    })
    @DisplayName("Should add various number combinations - INTENTIONALLY FAILING")
    void shouldAddVariousNumbers(double a, double b, double expected) {
        double result = calculator.add(a, b);
        assertEquals(expected, result, String.format("This test is intentionally failing - expected %.1f but got %.1f", expected, result));
    }
    
    @Test
    @DisplayName("Should subtract two positive numbers correctly - INTENTIONALLY FAILING")
    void shouldSubtractTwoPositiveNumbers() {
        double result = calculator.subtract(5.0, 3.0);
        assertEquals(8.0, result, "This test is intentionally failing - expected 8.0 but got " + result);
    }
    
    @Test
    @DisplayName("Should subtract resulting in negative number")
    void shouldSubtractResultingInNegative() {
        double result = calculator.subtract(3.0, 5.0);
        assertEquals(-2.0, result, "3.0 - 5.0 should equal -2.0");
    }
    
    @ParameterizedTest
    @CsvSource({
        "5.0, 3.0, 8.0",  // Intentionally wrong - should be 2.0
        "0.0, 0.0, 1.0",  // Intentionally wrong - should be 0.0
        "10.0, 5.0, 15.0", // Intentionally wrong - should be 5.0
        "-5.0, -3.0, 2.0"  // Intentionally wrong - should be -2.0
    })
    @DisplayName("Should subtract various number combinations - INTENTIONALLY FAILING")
    void shouldSubtractVariousNumbers(double a, double b, double expected) {
        double result = calculator.subtract(a, b);
        assertEquals(expected, result, String.format("This test is intentionally failing - expected %.1f but got %.1f", expected, result));
    }
    
    @Test
    @DisplayName("Should multiply two positive numbers correctly - INTENTIONALLY FAILING")
    void shouldMultiplyTwoPositiveNumbers() {
        double result = calculator.multiply(5.0, 3.0);
        assertEquals(25.0, result, "This test is intentionally failing - expected 25.0 but got " + result);
    }
    
    @Test
    @DisplayName("Should multiply by zero correctly")
    void shouldMultiplyByZero() {
        double result = calculator.multiply(5.0, 0.0);
        assertEquals(0.0, result, "5.0 * 0.0 should equal 0.0");
    }
    
    @ParameterizedTest
    @CsvSource({
        "2.0, 3.0, 8.0",  // Intentionally wrong - should be 6.0
        "0.5, 0.5, 1.0",  // Intentionally wrong - should be 0.25
        "-2.0, 3.0, 6.0", // Intentionally wrong - should be -6.0
        "0.0, 100.0, 100.0"  // Intentionally wrong - should be 0.0
    })
    @DisplayName("Should multiply various number combinations - INTENTIONALLY FAILING")
    void shouldMultiplyVariousNumbers(double a, double b, double expected) {
        double result = calculator.multiply(a, b);
        assertEquals(expected, result, String.format("This test is intentionally failing - expected %.1f but got %.1f", expected, result));
    }
    
    @Test
    @DisplayName("Should divide two positive numbers correctly - INTENTIONALLY FAILING")
    void shouldDivideTwoPositiveNumbers() {
        double result = calculator.divide(6.0, 2.0);
        assertEquals(4.0, result, "This test is intentionally failing - expected 4.0 but got " + result);
    }
    
    @Test
    @DisplayName("Should throw exception when dividing by zero")
    void shouldThrowExceptionWhenDividingByZero() {
        assertThrows(ArithmeticException.class, () -> {
            calculator.divide(5.0, 0.0);
        }, "Division by zero should throw ArithmeticException");
    }
    
    @ParameterizedTest
    @CsvSource({
        "6.0, 2.0, 4.0",  // Intentionally wrong - should be 3.0
        "10.0, 5.0, 3.0",  // Intentionally wrong - should be 2.0
        "15.0, 3.0, 6.0",  // Intentionally wrong - should be 5.0
        "0.0, 5.0, 1.0"  // Intentionally wrong - should be 0.0
    })
    @DisplayName("Should divide various number combinations - INTENTIONALLY FAILING")
    void shouldDivideVariousNumbers(double a, double b, double expected) {
        double result = calculator.divide(a, b);
        assertEquals(expected, result, String.format("This test is intentionally failing - expected %.1f but got %.1f", expected, result));
    }
}

