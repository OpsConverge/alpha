/**
 * Jest unit tests for CalculatorService - Working Version
 */

const CalculatorService = require('./calculatorService');

describe('CalculatorService', () => {
  let calculator;

  beforeEach(() => {
    calculator = new CalculatorService();
  });

  describe('Addition', () => {
    test('should add two positive numbers correctly', () => {
      const result = calculator.add(5, 3);
      expect(result).toBe(8);
    });

    test('should add negative numbers correctly', () => {
      const result = calculator.add(-5, -3);
      expect(result).toBe(-8);
    });

    test('should add zero correctly', () => {
      const result = calculator.add(5, 0);
      expect(result).toBe(5);
    });

    test.each([
      [1, 2, 3],
      [0.5, 0.3, 0.8],
      [-1, 1, 0],
      [100, 200, 300],
      [0, 0, 0]
    ])('should add %i and %i to equal %i', (a, b, expected) => {
      const result = calculator.add(a, b);
      expect(result).toBe(expected);
    });
  });

  describe('Subtraction', () => {
    test('should subtract two positive numbers correctly', () => {
      const result = calculator.subtract(5, 3);
      expect(result).toBe(2);
    });

    test('should handle negative result', () => {
      const result = calculator.subtract(3, 5);
      expect(result).toBe(-2);
    });

    test.each([
      [5, 3, 2],
      [0, 0, 0],
      [10, 5, 5],
      [-5, -3, -2]
    ])('should subtract %i from %i to equal %i', (a, b, expected) => {
      const result = calculator.subtract(a, b);
      expect(result).toBe(expected);
    });
  });

  describe('Multiplication', () => {
    test('should multiply two positive numbers correctly', () => {
      const result = calculator.multiply(5, 3);
      expect(result).toBe(15);
    });

    test('should handle multiplication by zero', () => {
      const result = calculator.multiply(5, 0);
      expect(result).toBe(0);
    });

    test.each([
      [2, 3, 6],
      [0.5, 0.5, 0.25],
      [-2, 3, -6],
      [0, 100, 0]
    ])('should multiply %i by %i to equal %i', (a, b, expected) => {
      const result = calculator.multiply(a, b);
      expect(result).toBe(expected);
    });
  });

  describe('Division', () => {
    test('should divide two positive numbers correctly', () => {
      const result = calculator.divide(6, 2);
      expect(result).toBe(3);
    });

    test('should handle division by zero', () => {
      expect(() => {
        calculator.divide(5, 0);
      }).toThrow('Cannot divide by zero');
    });

    test.each([
      [6, 2, 3],
      [10, 5, 2],
      [15, 3, 5],
      [0, 5, 0]
    ])('should divide %i by %i to equal %i', (a, b, expected) => {
      const result = calculator.divide(a, b);
      expect(result).toBe(expected);
    });
  });

  describe('Power', () => {
    test('should calculate power correctly', () => {
      const result = calculator.power(2, 3);
      expect(result).toBe(8);
    });

    test('should handle power of zero', () => {
      const result = calculator.power(5, 0);
      expect(result).toBe(1);
    });

    test.each([
      [2, 3, 8],
      [5, 0, 1],
      [2, -1, 0.5],
      [0, 5, 0]
    ])('should calculate %i to the power of %i to equal %i', (base, exponent, expected) => {
      const result = calculator.power(base, exponent);
      expect(result).toBe(expected);
    });
  });

  describe('Square Root', () => {
    test('should calculate square root correctly', () => {
      const result = calculator.sqrt(16);
      expect(result).toBe(4);
    });

    test('should handle negative number', () => {
      expect(() => {
        calculator.sqrt(-4);
      }).toThrow('Cannot calculate square root of negative number');
    });

    test.each([0, 1, 4, 9, 16, 25])('should calculate square root of %i', (number) => {
      const result = calculator.sqrt(number);
      expect(result).toBe(Math.sqrt(number));
    });
  });
});
