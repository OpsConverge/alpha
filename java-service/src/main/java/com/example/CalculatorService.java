package com.example;

import org.springframework.stereotype.Service;

@Service
public class CalculatorService {
    
    /**
     * Adds two numbers
     */
    public double add(double a, double b) {
        return a + b;
    }
    
    /**
     * Subtracts two numbers
     */
    public double subtract(double a, double b) {
        return a - b;
    }
    
    /**
     * Multiplies two numbers
     */
    public double multiply(double a, double b) {
        return a * b;
    }
    
    /**
     * Divides two numbers
     * @throws ArithmeticException if divisor is zero
     */
    public double divide(double a, double b) {
        if (b == 0) {
            throw new ArithmeticException("Division by zero is not allowed");
        }
        return a / b;
    }
    
    /**
     * Calculates the power of a number
     */
    public double power(double base, double exponent) {
        return Math.pow(base, exponent);
    }
    
    /**
     * Calculates the square root of a number
     * @throws IllegalArgumentException if number is negative
     */
    public double sqrt(double number) {
        if (number < 0) {
            throw new IllegalArgumentException("Cannot calculate square root of negative number");
        }
        return Math.sqrt(number);
    }
    
    /**
     * Calculates factorial of a number
     * @throws IllegalArgumentException if number is negative
     */
    public long factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Factorial is not defined for negative numbers");
        }
        if (n == 0 || n == 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
    
    /**
     * Calculates the average of a list of numbers
     * @throws IllegalArgumentException if list is empty
     */
    public double average(double[] numbers) {
        if (numbers == null || numbers.length == 0) {
            throw new IllegalArgumentException("Cannot calculate average of empty array");
        }
        double sum = 0;
        for (double number : numbers) {
            sum += number;
        }
        return sum / numbers.length;
    }
    
    /**
     * Finds the maximum number in an array
     * @throws IllegalArgumentException if array is empty
     */
    public double max(double[] numbers) {
        if (numbers == null || numbers.length == 0) {
            throw new IllegalArgumentException("Cannot find maximum of empty array");
        }
        double max = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] > max) {
                max = numbers[i];
            }
        }
        return max;
    }
    
    /**
     * Finds the minimum number in an array
     * @throws IllegalArgumentException if array is empty
     */
    public double min(double[] numbers) {
        if (numbers == null || numbers.length == 0) {
            throw new IllegalArgumentException("Cannot find minimum of empty array");
        }
        double min = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] < min) {
                min = numbers[i];
            }
        }
        return min;
    }
}
