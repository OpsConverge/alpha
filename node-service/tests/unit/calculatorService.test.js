/**
 * Jest unit tests for CalculatorService
 */

const CalculatorService = require('../../src/calculatorService');

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

    test('should add two positive numbers correctly - INTENTIONALLY FAILING', () => {
      const result = calculator.add(5, 3);
      expect(result).toBe(10); // This will fail - should be 8
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
    ])('should add %i and %i to get %i', (a, b, expected) => {
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
    ])('should subtract %i from %i to get %i', (a, b, expected) => {
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
    ])('should multiply %i by %i to get %i', (a, b, expected) => {
      const result = calculator.multiply(a, b);
      expect(result).toBe(expected);
    });
  });

  describe('Division', () => {
    test('should divide two positive numbers correctly', () => {
      const result = calculator.divide(6, 2);
      expect(result).toBe(3);
    });

    test('should throw error when dividing by zero', () => {
      expect(() => {
        calculator.divide(5, 0);
      }).toThrow('Division by zero is not allowed');
    });

    test.each([
      [6, 2, 3],
      [5, 2, 2.5],
      [0, 5, 0],
      [-6, 2, -3]
    ])('should divide %i by %i to get %i', (a, b, expected) => {
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
    ])('should calculate %i to the power of %i to get %i', (base, exponent, expected) => {
      const result = calculator.power(base, exponent);
      expect(result).toBe(expected);
    });
  });

  describe('Square Root', () => {
    test('should calculate square root correctly', () => {
      const result = calculator.sqrt(16);
      expect(result).toBe(4);
    });

    test('should throw error for negative number', () => {
      expect(() => {
        calculator.sqrt(-4);
      }).toThrow('Cannot calculate square root of negative number');
    });

    test.each([
      [0, 0],
      [1, 1],
      [4, 2],
      [9, 3],
      [16, 4],
      [25, 5]
    ])('should calculate square root of %i to get %i', (number, expected) => {
      const result = calculator.sqrt(number);
      expect(result).toBe(expected);
    });
  });

  describe('Factorial', () => {
    test('should calculate factorial correctly', () => {
      const result = calculator.factorial(5);
      expect(result).toBe(120);
    });

    test('should handle factorial of zero', () => {
      const result = calculator.factorial(0);
      expect(result).toBe(1);
    });

    test('should handle factorial of one', () => {
      const result = calculator.factorial(1);
      expect(result).toBe(1);
    });

    test('should throw error for negative number', () => {
      expect(() => {
        calculator.factorial(-5);
      }).toThrow('Factorial is not defined for negative numbers');
    });

    test.each([
      [0, 1],
      [1, 1],
      [2, 2],
      [3, 6],
      [4, 24],
      [5, 120]
    ])('should calculate factorial of %i to get %i', (n, expected) => {
      const result = calculator.factorial(n);
      expect(result).toBe(expected);
    });
  });

  describe('Array Operations', () => {
    describe('Average', () => {
      test('should calculate average correctly', () => {
        const result = calculator.average([1, 2, 3, 4, 5]);
        expect(result).toBe(3);
      });

      test('should throw error for empty array', () => {
        expect(() => {
          calculator.average([]);
        }).toThrow('Cannot calculate average of empty array');
      });

      test('should throw error for null array', () => {
        expect(() => {
          calculator.average(null);
        }).toThrow('Cannot calculate average of empty array');
      });
    });

    describe('Maximum', () => {
      test('should find maximum correctly', () => {
        const result = calculator.max([1, 5, 3, 9, 2]);
        expect(result).toBe(9);
      });

      test('should throw error for empty array', () => {
        expect(() => {
          calculator.max([]);
        }).toThrow('Cannot find maximum of empty array');
      });

      test('should throw error for null array', () => {
        expect(() => {
          calculator.max(null);
        }).toThrow('Cannot find maximum of empty array');
      });
    });

    describe('Minimum', () => {
      test('should find minimum correctly', () => {
        const result = calculator.min([1, 5, 3, 9, 2]);
        expect(result).toBe(1);
      });

      test('should throw error for empty array', () => {
        expect(() => {
          calculator.min([]);
        }).toThrow('Cannot find minimum of empty array');
      });

      test('should throw error for null array', () => {
        expect(() => {
          calculator.min(null);
        }).toThrow('Cannot find minimum of empty array');
      });
    });
  });

  describe('GCD', () => {
    test('should calculate GCD of positive numbers', () => {
      const result = calculator.gcd(48, 18);
      expect(result).toBe(6);
    });

    test('should handle GCD with zero', () => {
      const result = calculator.gcd(0, 5);
      expect(result).toBe(5);
    });

    test.each([
      [48, 18, 6],
      [54, 24, 6],
      [7, 13, 1],
      [0, 0, 0]
    ])('should calculate GCD of %i and %i to get %i', (a, b, expected) => {
      const result = calculator.gcd(a, b);
      expect(result).toBe(expected);
    });
  });

  describe('LCM', () => {
    test('should calculate LCM of positive numbers', () => {
      const result = calculator.lcm(12, 18);
      expect(result).toBe(36);
    });

    test('should handle LCM with zero', () => {
      const result = calculator.lcm(0, 5);
      expect(result).toBe(0);
    });

    test.each([
      [12, 18, 36],
      [8, 12, 24],
      [7, 13, 91],
      [0, 0, 0]
    ])('should calculate LCM of %i and %i to get %i', (a, b, expected) => {
      const result = calculator.lcm(a, b);
      expect(result).toBe(expected);
    });
  });

  describe('Prime Numbers', () => {
    test('should identify prime numbers correctly', () => {
      expect(calculator.isPrime(2)).toBe(true);
      expect(calculator.isPrime(3)).toBe(true);
      expect(calculator.isPrime(17)).toBe(true);
    });

    test('should identify non-prime numbers correctly', () => {
      expect(calculator.isPrime(1)).toBe(false);
      expect(calculator.isPrime(4)).toBe(false);
      expect(calculator.isPrime(15)).toBe(false);
    });

    test.each([
      [2, true],
      [3, true],
      [4, false],
      [5, true],
      [6, false],
      [7, true],
      [8, false],
      [9, false],
      [10, false],
      [11, true]
    ])('should identify %i as prime: %s', (n, expected) => {
      const result = calculator.isPrime(n);
      expect(result).toBe(expected);
    });
  });
});
