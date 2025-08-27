/**
 * Calculator Service for Jest unit testing
 */

class CalculatorService {
  /**
   * Add two numbers
   * @param {number} a - First number
   * @param {number} b - Second number
   * @returns {number} Sum of the two numbers
   */
  add(a, b) {
    return a + b;
  }

  /**
   * Subtract two numbers
   * @param {number} a - First number
   * @param {number} b - Second number
   * @returns {number} Difference of the two numbers
   */
  subtract(a, b) {
    return a - b;
  }

  /**
   * Multiply two numbers
   * @param {number} a - First number
   * @param {number} b - Second number
   * @returns {number} Product of the two numbers
   */
  multiply(a, b) {
    return a * b;
  }

  /**
   * Divide two numbers
   * @param {number} a - First number
   * @param {number} b - Second number
   * @returns {number} Quotient of the two numbers
   * @throws {Error} When dividing by zero
   */
  divide(a, b) {
    if (b === 0) {
      throw new Error('Division by zero is not allowed');
    }
    return a / b;
  }

  /**
   * Calculate power of a number
   * @param {number} base - Base number
   * @param {number} exponent - Exponent
   * @returns {number} Result of base raised to exponent
   */
  power(base, exponent) {
    return Math.pow(base, exponent);
  }

  /**
   * Calculate square root of a number
   * @param {number} number - Number to find square root of
   * @returns {number} Square root of the number
   * @throws {Error} When number is negative
   */
  sqrt(number) {
    if (number < 0) {
      throw new Error('Cannot calculate square root of negative number');
    }
    return Math.sqrt(number);
  }

  /**
   * Calculate factorial of a number
   * @param {number} n - Number to calculate factorial of
   * @returns {number} Factorial of the number
   * @throws {Error} When number is negative
   */
  factorial(n) {
    if (n < 0) {
      throw new Error('Factorial is not defined for negative numbers');
    }
    if (n === 0 || n === 1) {
      return 1;
    }
    return n * this.factorial(n - 1);
  }

  /**
   * Calculate average of an array of numbers
   * @param {number[]} numbers - Array of numbers
   * @returns {number} Average of the numbers
   * @throws {Error} When array is empty
   */
  average(numbers) {
    if (!numbers || numbers.length === 0) {
      throw new Error('Cannot calculate average of empty array');
    }
    const sum = numbers.reduce((acc, num) => acc + num, 0);
    return sum / numbers.length;
  }

  /**
   * Find maximum number in an array
   * @param {number[]} numbers - Array of numbers
   * @returns {number} Maximum number
   * @throws {Error} When array is empty
   */
  max(numbers) {
    if (!numbers || numbers.length === 0) {
      throw new Error('Cannot find maximum of empty array');
    }
    return Math.max(...numbers);
  }

  /**
   * Find minimum number in an array
   * @param {number[]} numbers - Array of numbers
   * @returns {number} Minimum number
   * @throws {Error} When array is empty
   */
  min(numbers) {
    if (!numbers || numbers.length === 0) {
      throw new Error('Cannot find minimum of empty array');
    }
    return Math.min(...numbers);
  }

  /**
   * Calculate greatest common divisor
   * @param {number} a - First number
   * @param {number} b - Second number
   * @returns {number} Greatest common divisor
   */
  gcd(a, b) {
    if (a === 0) return Math.abs(b);
    if (b === 0) return Math.abs(a);
    return this.gcd(b, a % b);
  }

  /**
   * Calculate least common multiple
   * @param {number} a - First number
   * @param {number} b - Second number
   * @returns {number} Least common multiple
   */
  lcm(a, b) {
    if (a === 0 || b === 0) return 0;
    return Math.abs(a * b) / this.gcd(a, b);
  }

  /**
   * Check if a number is prime
   * @param {number} n - Number to check
   * @returns {boolean} True if prime, false otherwise
   */
  isPrime(n) {
    if (n < 2) return false;
    if (n === 2) return true;
    if (n % 2 === 0) return false;
    
    for (let i = 3; i <= Math.sqrt(n); i += 2) {
      if (n % i === 0) return false;
    }
    return true;
  }
}

module.exports = CalculatorService;
