/**
 * Jest unit tests for StringService - Working Version
 */

const StringService = require('./stringService');

describe('StringService', () => {
  let stringService;

  beforeEach(() => {
    stringService = new StringService();
  });

  describe('Reverse', () => {
    test('should reverse a simple string correctly', () => {
      const result = stringService.reverse('hello');
      expect(result).toBe('olleh');
    });

    test('should handle empty string', () => {
      const result = stringService.reverse('');
      expect(result).toBe('');
    });

    test('should handle single character', () => {
      const result = stringService.reverse('a');
      expect(result).toBe('a');
    });

    test.each([
      ['hello', 'olleh'],
      ['world', 'dlrow'],
      ['python', 'nohtyp'],
      ['12345', '54321'],
      ['', ''],
      ['a', 'a']
    ])('should reverse %s to %s', (input, expected) => {
      const result = stringService.reverse(input);
      expect(result).toBe(expected);
    });
  });

  describe('To Upper Case', () => {
    test('should convert string to uppercase', () => {
      const result = stringService.toUpperCase('hello');
      expect(result).toBe('HELLO');
    });

    test('should handle already uppercase string', () => {
      const result = stringService.toUpperCase('HELLO');
      expect(result).toBe('HELLO');
    });

    test('should handle mixed case string', () => {
      const result = stringService.toUpperCase('HeLLo WoRLd');
      expect(result).toBe('HELLO WORLD');
    });

    test.each([
      ['hello', 'HELLO'],
      ['world', 'WORLD'],
      ['python', 'PYTHON'],
      ['HELLO', 'HELLO'],
      ['', ''],
      ['a', 'A']
    ])('should convert %s to uppercase %s', (input, expected) => {
      const result = stringService.toUpperCase(input);
      expect(result).toBe(expected);
    });
  });

  describe('To Lower Case', () => {
    test('should convert string to lowercase', () => {
      const result = stringService.toLowerCase('HELLO');
      expect(result).toBe('hello');
    });

    test('should handle already lowercase string', () => {
      const result = stringService.toLowerCase('hello');
      expect(result).toBe('hello');
    });

    test('should handle mixed case string', () => {
      const result = stringService.toLowerCase('HeLLo WoRLd');
      expect(result).toBe('hello world');
    });

    test.each([
      ['HELLO', 'hello'],
      ['WORLD', 'world'],
      ['PYTHON', 'python'],
      ['hello', 'hello'],
      ['', ''],
      ['A', 'a']
    ])('should convert %s to lowercase %s', (input, expected) => {
      const result = stringService.toLowerCase(input);
      expect(result).toBe(expected);
    });
  });

  describe('Count Vowels', () => {
    test('should count vowels in simple string', () => {
      const result = stringService.countVowels('hello');
      expect(result).toBe(2);
    });

    test('should handle string with no vowels', () => {
      const result = stringService.countVowels('rhythm');
      expect(result).toBe(0);
    });

    test('should handle string with all vowels', () => {
      const result = stringService.countVowels('aeiou');
      expect(result).toBe(5);
    });

    test.each([
      ['hello', 2],
      ['world', 1],
      ['python', 1],
      ['aeiou', 5],
      ['rhythm', 0],
      ['', 0],
      ['a', 1]
    ])('should count %i vowels in %s', (expected, input) => {
      const result = stringService.countVowels(input);
      expect(result).toBe(expected);
    });
  });

  describe('Remove Special Characters', () => {
    test('should remove special characters from string', () => {
      const result = stringService.removeSpecialChars('hello@world!');
      expect(result).toBe('helloworld');
    });

    test('should handle string with no special characters', () => {
      const result = stringService.removeSpecialChars('hello world');
      expect(result).toBe('helloworld');
    });

    test('should handle string with only special characters', () => {
      const result = stringService.removeSpecialChars('@#$%^&*()');
      expect(result).toBe('');
    });

    test.each([
      ['hello@world!', 'helloworld'],
      ['python#123', 'python123'],
      ['test$string%', 'teststring'],
      ['no_special_chars', 'nospecialchars'],
      ['', ''],
      ['a', 'a']
    ])('should remove special chars from %s to get %s', (input, expected) => {
      const result = stringService.removeSpecialChars(input);
      expect(result).toBe(expected);
    });
  });

  describe('Remove Duplicates', () => {
    test('should remove duplicate characters', () => {
      const result = stringService.removeDuplicates('hello');
      expect(result).toBe('helo');
    });

    test('should handle string with no duplicates', () => {
      const result = stringService.removeDuplicates('python');
      expect(result).toBe('python');
    });

    test('should handle empty string', () => {
      const result = stringService.removeDuplicates('');
      expect(result).toBe('');
    });

    test.each([
      ['hello', 'helo'],
      ['world', 'world'],
      ['mississippi', 'misp'],
      ['aabbcc', 'abc'],
      ['', ''],
      ['a', 'a']
    ])('should remove duplicates from %s to get %s', (input, expected) => {
      const result = stringService.removeDuplicates(input);
      expect(result).toBe(expected);
    });
  });

  describe('Title Case', () => {
    test('should convert string to title case', () => {
      const result = stringService.titleCase('hello world');
      expect(result).toBe('Hello World');
    });

    test('should handle single word', () => {
      const result = stringService.titleCase('hello');
      expect(result).toBe('Hello');
    });

    test('should handle multiple spaces', () => {
      const result = stringService.titleCase('hello   world');
      expect(result).toBe('Hello   World');
    });

    test.each([
      ['hello world', 'Hello World'],
      ['python programming', 'Python Programming'],
      ['javascript is awesome', 'Javascript Is Awesome'],
      ['', ''],
      ['a', 'A']
    ])('should convert %s to title case %s', (input, expected) => {
      const result = stringService.titleCase(input);
      expect(result).toBe(expected);
    });
  });
});

