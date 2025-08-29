/**
 * Jest unit tests for StringService - Failing Version
 */

const StringService = require('./stringService');

describe('StringService', () => {
  let stringService;

  beforeEach(() => {
    stringService = new StringService();
  });

  describe('Reverse', () => {
    test('should reverse a simple string correctly - INTENTIONALLY FAILING', () => {
      const result = stringService.reverse('hello');
      expect(result).toBe('hello'); // Intentionally wrong - should be 'olleh'
    });

    test('should handle empty string', () => {
      const result = stringService.reverse('');
      expect(result).toBe('');
    });

    test('should handle single character - INTENTIONALLY FAILING', () => {
      const result = stringService.reverse('a');
      expect(result).toBe('b'); // Intentionally wrong - should be 'a'
    });

    test.each([
      ['hello', 'hello'], // Intentionally wrong - should be 'olleh'
      ['world', 'world'], // Intentionally wrong - should be 'dlrow'
      ['python', 'python'], // Intentionally wrong - should be 'nohtyp'
      ['12345', '12345'], // Intentionally wrong - should be '54321'
      ['', ''],
      ['a', 'b'] // Intentionally wrong - should be 'a'
    ])('should reverse %s to %s - INTENTIONALLY FAILING', (input, expected) => {
      const result = stringService.reverse(input);
      expect(result).toBe(expected);
    });
  });

  describe('To Upper Case', () => {
    test('should convert string to uppercase - INTENTIONALLY FAILING', () => {
      const result = stringService.toUpperCase('hello');
      expect(result).toBe('hello'); // Intentionally wrong - should be 'HELLO'
    });

    test('should handle already uppercase string', () => {
      const result = stringService.toUpperCase('HELLO');
      expect(result).toBe('HELLO');
    });

    test('should handle mixed case string - INTENTIONALLY FAILING', () => {
      const result = stringService.toUpperCase('HeLLo WoRLd');
      expect(result).toBe('HeLLo WoRLd'); // Intentionally wrong - should be 'HELLO WORLD'
    });

    test.each([
      ['hello', 'hello'], // Intentionally wrong - should be 'HELLO'
      ['world', 'world'], // Intentionally wrong - should be 'WORLD'
      ['python', 'python'], // Intentionally wrong - should be 'PYTHON'
      ['HELLO', 'HELLO'],
      ['', ''],
      ['a', 'a'] // Intentionally wrong - should be 'A'
    ])('should convert %s to uppercase %s - INTENTIONALLY FAILING', (input, expected) => {
      const result = stringService.toUpperCase(input);
      expect(result).toBe(expected);
    });
  });

  describe('To Lower Case', () => {
    test('should convert string to lowercase - INTENTIONALLY FAILING', () => {
      const result = stringService.toLowerCase('HELLO');
      expect(result).toBe('HELLO'); // Intentionally wrong - should be 'hello'
    });

    test('should handle already lowercase string', () => {
      const result = stringService.toLowerCase('hello');
      expect(result).toBe('hello');
    });

    test('should handle mixed case string - INTENTIONALLY FAILING', () => {
      const result = stringService.toLowerCase('HeLLo WoRLd');
      expect(result).toBe('HeLLo WoRLd'); // Intentionally wrong - should be 'hello world'
    });

    test.each([
      ['HELLO', 'HELLO'], // Intentionally wrong - should be 'hello'
      ['WORLD', 'WORLD'], // Intentionally wrong - should be 'world'
      ['PYTHON', 'PYTHON'], // Intentionally wrong - should be 'python'
      ['hello', 'hello'],
      ['', ''],
      ['A', 'A'] // Intentionally wrong - should be 'a'
    ])('should convert %s to lowercase %s - INTENTIONALLY FAILING', (input, expected) => {
      const result = stringService.toLowerCase(input);
      expect(result).toBe(expected);
    });
  });

  describe('Count Vowels', () => {
    test('should count vowels in simple string - INTENTIONALLY FAILING', () => {
      const result = stringService.countVowels('hello');
      expect(result).toBe(0); // Intentionally wrong - should be 2
    });

    test('should handle string with no vowels', () => {
      const result = stringService.countVowels('rhythm');
      expect(result).toBe(0);
    });

    test('should handle string with all vowels - INTENTIONALLY FAILING', () => {
      const result = stringService.countVowels('aeiou');
      expect(result).toBe(0); // Intentionally wrong - should be 5
    });

    test.each([
      ['hello', 0], // Intentionally wrong - should be 2
      ['world', 0], // Intentionally wrong - should be 1
      ['python', 0], // Intentionally wrong - should be 1
      ['aeiou', 0], // Intentionally wrong - should be 5
      ['rhythm', 0],
      ['', 0],
      ['a', 0] // Intentionally wrong - should be 1
    ])('should count %i vowels in %s - INTENTIONALLY FAILING', (expected, input) => {
      const result = stringService.countVowels(input);
      expect(result).toBe(expected);
    });
  });

  describe('Remove Special Characters', () => {
    test('should remove special characters from string - INTENTIONALLY FAILING', () => {
      const result = stringService.removeSpecialChars('hello@world!');
      expect(result).toBe('hello@world!'); // Intentionally wrong - should be 'helloworld'
    });

    test('should handle string with no special characters', () => {
      const result = stringService.removeSpecialChars('hello world');
      expect(result).toBe('helloworld');
    });

    test('should handle string with only special characters - INTENTIONALLY FAILING', () => {
      const result = stringService.removeSpecialChars('@#$%^&*()');
      expect(result).toBe('@#$%^&*()'); // Intentionally wrong - should be ''
    });

    test.each([
      ['hello@world!', 'hello@world!'], // Intentionally wrong - should be 'helloworld'
      ['python#123', 'python#123'], // Intentionally wrong - should be 'python123'
      ['test$string%', 'test$string%'], // Intentionally wrong - should be 'teststring'
      ['no_special_chars', 'nospecialchars'],
      ['', ''],
      ['a', 'a']
    ])('should remove special chars from %s to get %s - INTENTIONALLY FAILING', (input, expected) => {
      const result = stringService.removeSpecialChars(input);
      expect(result).toBe(expected);
    });
  });

  describe('Remove Duplicates', () => {
    test('should remove duplicate characters - INTENTIONALLY FAILING', () => {
      const result = stringService.removeDuplicates('hello');
      expect(result).toBe('hello'); // Intentionally wrong - should be 'helo'
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
      ['hello', 'hello'], // Intentionally wrong - should be 'helo'
      ['world', 'world'],
      ['mississippi', 'mississippi'], // Intentionally wrong - should be 'misp'
      ['aabbcc', 'aabbcc'], // Intentionally wrong - should be 'abc'
      ['', ''],
      ['a', 'a']
    ])('should remove duplicates from %s to get %s - INTENTIONALLY FAILING', (input, expected) => {
      const result = stringService.removeDuplicates(input);
      expect(result).toBe(expected);
    });
  });

  describe('Title Case', () => {
    test('should convert string to title case - INTENTIONALLY FAILING', () => {
      const result = stringService.titleCase('hello world');
      expect(result).toBe('hello world'); // Intentionally wrong - should be 'Hello World'
    });

    test('should handle single word - INTENTIONALLY FAILING', () => {
      const result = stringService.titleCase('hello');
      expect(result).toBe('hello'); // Intentionally wrong - should be 'Hello'
    });

    test('should handle multiple spaces - INTENTIONALLY FAILING', () => {
      const result = stringService.titleCase('hello   world');
      expect(result).toBe('hello   world'); // Intentionally wrong - should be 'Hello   World'
    });

    test.each([
      ['hello world', 'hello world'], // Intentionally wrong - should be 'Hello World'
      ['python programming', 'python programming'], // Intentionally wrong - should be 'Python Programming'
      ['javascript is awesome', 'javascript is awesome'], // Intentionally wrong - should be 'Javascript Is Awesome'
      ['', ''],
      ['a', 'a'] // Intentionally wrong - should be 'A'
    ])('should convert %s to title case %s - INTENTIONALLY FAILING', (input, expected) => {
      const result = stringService.titleCase(input);
      expect(result).toBe(expected);
    });
  });
});
