/**
 * Jest unit tests for StringService
 */

const StringService = require('../../src/stringService');

describe('StringService', () => {
  let stringService;

  beforeEach(() => {
    stringService = new StringService();
  });

  describe('Reverse', () => {
    test('should reverse a string correctly', () => {
      const result = stringService.reverse('hello');
      expect(result).toBe('olleh');
    });

    test('should reverse a string correctly - INTENTIONALLY FAILING', () => {
      const result = stringService.reverse('hello');
      expect(result).toBe('hello'); // This will fail - should be 'olleh'
    });

    test('should handle empty string', () => {
      const result = stringService.reverse('');
      expect(result).toBe('');
    });

    test('should handle single character', () => {
      const result = stringService.reverse('a');
      expect(result).toBe('a');
    });

    test('should handle null input', () => {
      const result = stringService.reverse(null);
      expect(result).toBeNull();
    });

    test('should handle undefined input', () => {
      const result = stringService.reverse(undefined);
      expect(result).toBeNull();
    });

    test.each([
      ['hello', 'olleh'],
      ['world', 'dlrow'],
      ['12345', '54321'],
      ['racecar', 'racecar'],
      ['A', 'A']
    ])('should reverse "%s" to "%s"', (input, expected) => {
      const result = stringService.reverse(input);
      expect(result).toBe(expected);
    });
  });

  describe('Palindrome', () => {
    test('should identify palindromes correctly', () => {
      expect(stringService.isPalindrome('racecar')).toBe(true);
      expect(stringService.isPalindrome('level')).toBe(true);
    });

    test('should identify non-palindromes correctly', () => {
      expect(stringService.isPalindrome('hello')).toBe(false);
      expect(stringService.isPalindrome('world')).toBe(false);
    });

    test('should handle palindrome with spaces and punctuation', () => {
      expect(stringService.isPalindrome('A man, a plan, a canal: Panama')).toBe(true);
    });

    test('should handle null input', () => {
      expect(stringService.isPalindrome(null)).toBe(false);
    });

    test('should handle undefined input', () => {
      expect(stringService.isPalindrome(undefined)).toBe(false);
    });

    test.each([
      ['racecar', true],
      ['level', true],
      ['deed', true],
      ['noon', true],
      ['civic', true],
      ['radar', true],
      ['hello', false],
      ['world', false],
      ['test', false],
      ['java', false]
    ])('should identify "%s" as palindrome: %s', (input, expected) => {
      const result = stringService.isPalindrome(input);
      expect(result).toBe(expected);
    });
  });

  describe('Count Vowels', () => {
    test('should count vowels correctly', () => {
      const result = stringService.countVowels('hello');
      expect(result).toBe(2);
    });

    test('should handle string with no vowels', () => {
      const result = stringService.countVowels('rhythm');
      expect(result).toBe(0);
    });

    test('should handle null input', () => {
      const result = stringService.countVowels(null);
      expect(result).toBe(0);
    });

    test('should handle undefined input', () => {
      const result = stringService.countVowels(undefined);
      expect(result).toBe(0);
    });

    test.each([
      [2, 'hello'],
      [1, 'world'],
      [5, 'aeiou'],
      [0, 'rhythm'],
      [3, 'programming'],
      [1, 'TEST']
    ])('should count %i vowels in "%s"', (expected, input) => {
      const result = stringService.countVowels(input);
      expect(result).toBe(expected);
    });
  });

  describe('Title Case', () => {
    test('should convert to title case correctly', () => {
      const result = stringService.toTitleCase('hello world');
      expect(result).toBe('Hello World');
    });

    test('should handle single word', () => {
      const result = stringService.toTitleCase('hello');
      expect(result).toBe('Hello');
    });

    test('should handle empty string', () => {
      const result = stringService.toTitleCase('');
      expect(result).toBe('');
    });

    test('should handle null input', () => {
      const result = stringService.toTitleCase(null);
      expect(result).toBeNull();
    });

    test('should handle undefined input', () => {
      const result = stringService.toTitleCase(undefined);
      expect(result).toBeUndefined();
    });

    test.each([
      ['hello world', 'Hello World'],
      ['JAVA PROGRAMMING', 'Java Programming'],
      ['test case', 'Test Case'],
      ['single', 'Single'],
      ['multiple   spaces', 'Multiple   Spaces']
    ])('should convert "%s" to "%s"', (input, expected) => {
      const result = stringService.toTitleCase(input);
      expect(result).toBe(expected);
    });
  });

  describe('Remove Duplicates', () => {
    test('should remove duplicate characters correctly', () => {
      const result = stringService.removeDuplicates('hello');
      expect(result).toBe('helo');
    });

    test('should handle string with no duplicates', () => {
      const result = stringService.removeDuplicates('world');
      expect(result).toBe('world');
    });

    test('should handle null input', () => {
      const result = stringService.removeDuplicates(null);
      expect(result).toBeNull();
    });

    test('should handle undefined input', () => {
      const result = stringService.removeDuplicates(undefined);
      expect(result).toBeNull();
    });

    test.each([
      ['hello', 'helo'],
      ['world', 'world'],
      ['programming', 'progamin'],
      ['test', 'tes'],
      ['aaaaa', 'a'],
      ['abcabc', 'abc']
    ])('should remove duplicates from "%s" to get "%s"', (input, expected) => {
      const result = stringService.removeDuplicates(input);
      expect(result).toBe(expected);
    });
  });

  describe('Find Longest Word', () => {
    test('should find longest word correctly', () => {
      const result = stringService.findLongestWord('hello world programming');
      expect(result).toBe('programming');
    });

    test('should handle single word', () => {
      const result = stringService.findLongestWord('hello');
      expect(result).toBe('hello');
    });

    test('should handle empty string', () => {
      const result = stringService.findLongestWord('');
      expect(result).toBe('');
    });

    test('should handle null input', () => {
      const result = stringService.findLongestWord(null);
      expect(result).toBe('');
    });

    test('should handle undefined input', () => {
      const result = stringService.findLongestWord(undefined);
      expect(result).toBe('');
    });

    test.each([
      ['hello world programming', 'programming'],
      ['test case example', 'example'],
      ['java python javascript', 'javascript'],
      ['a bb ccc', 'ccc'],
      ['short medium long', 'medium']
    ])('should find longest word in "%s" as "%s"', (input, expected) => {
      const result = stringService.findLongestWord(input);
      expect(result).toBe(expected);
    });
  });

  describe('Count Words', () => {
    test('should count words correctly', () => {
      const result = stringService.countWords('hello world programming');
      expect(result).toBe(3);
    });

    test('should handle single word', () => {
      const result = stringService.countWords('hello');
      expect(result).toBe(1);
    });

    test('should handle empty string', () => {
      const result = stringService.countWords('');
      expect(result).toBe(0);
    });

    test('should handle null input', () => {
      const result = stringService.countWords(null);
      expect(result).toBe(0);
    });

    test('should handle undefined input', () => {
      const result = stringService.countWords(undefined);
      expect(result).toBe(0);
    });
  });

  describe('Anagram', () => {
    test('should identify anagrams correctly', () => {
      expect(stringService.isAnagram('listen', 'silent')).toBe(true);
      expect(stringService.isAnagram('debit card', 'bad credit')).toBe(true);
    });

    test('should identify non-anagrams correctly', () => {
      expect(stringService.isAnagram('hello', 'world')).toBe(false);
    });

    test('should handle null inputs', () => {
      expect(stringService.isAnagram(null, 'test')).toBe(false);
      expect(stringService.isAnagram('test', null)).toBe(false);
    });

    test('should handle undefined inputs', () => {
      expect(stringService.isAnagram(undefined, 'test')).toBe(false);
      expect(stringService.isAnagram('test', undefined)).toBe(false);
    });

    test.each([
      ['listen', 'silent', true],
      ['hello', 'world', false],
      ['debit card', 'bad credit', true],
      ['funeral', 'real fun', true],
      ['school master', 'the classroom', true]
    ])('should identify "%s" and "%s" as anagrams: %s', (text1, text2, expected) => {
      const result = stringService.isAnagram(text1, text2);
      expect(result).toBe(expected);
    });
  });

  describe('Capitalize Words', () => {
    test('should capitalize words correctly', () => {
      const result = stringService.capitalizeWords('hello world');
      expect(result).toBe('Hello World');
    });

    test('should handle null input', () => {
      const result = stringService.capitalizeWords(null);
      expect(result).toBeNull();
    });

    test('should handle undefined input', () => {
      const result = stringService.capitalizeWords(undefined);
      expect(result).toBeNull();
    });

    test.each([
      ['hello world', 'Hello World'],
      ['python programming', 'Python Programming'],
      ['test case', 'Test Case'],
      ['single', 'Single']
    ])('should capitalize "%s" to "%s"', (input, expected) => {
      const result = stringService.capitalizeWords(input);
      expect(result).toBe(expected);
    });
  });

  describe('Count Occurrences', () => {
    test('should count occurrences correctly', () => {
      const result = stringService.countOccurrences('hello world hello', 'hello');
      expect(result).toBe(2);
    });

    test('should handle null inputs', () => {
      expect(stringService.countOccurrences(null, 'test')).toBe(0);
      expect(stringService.countOccurrences('test', null)).toBe(0);
    });

    test('should handle undefined inputs', () => {
      expect(stringService.countOccurrences(undefined, 'test')).toBe(0);
      expect(stringService.countOccurrences('test', undefined)).toBe(0);
    });

    test.each([
      [2, 'hello', 'hello world hello'],
      [3, 'test', 'test test test'],
      [1, 'python', 'python programming'],
      [0, 'missing', 'no match']
    ])('should count %i occurrences of "%s" in "%s"', (expected, substring, text) => {
      const result = stringService.countOccurrences(text, substring);
      expect(result).toBe(expected);
    });
  });

  describe('Valid Email', () => {
    test('should validate emails correctly', () => {
      expect(stringService.isValidEmail('test@example.com')).toBe(true);
      expect(stringService.isValidEmail('user.name@domain.co.uk')).toBe(true);
    });

    test('should reject invalid emails', () => {
      expect(stringService.isValidEmail('invalid-email')).toBe(false);
      expect(stringService.isValidEmail('@domain.com')).toBe(false);
    });

    test('should handle null input', () => {
      expect(stringService.isValidEmail(null)).toBe(false);
    });

    test('should handle undefined input', () => {
      expect(stringService.isValidEmail(undefined)).toBe(false);
    });

    test.each([
      ['test@example.com', true],
      ['user.name@domain.co.uk', true],
      ['invalid-email', false],
      ['@domain.com', false],
      ['test@', false],
      ['test.domain.com', false]
    ])('should validate "%s" as email: %s', (email, expected) => {
      const result = stringService.isValidEmail(email);
      expect(result).toBe(expected);
    });
  });

  describe('Extract Numbers', () => {
    test('should extract numbers correctly', () => {
      const result = stringService.extractNumbers('hello 123 world 456');
      expect(result).toEqual([123, 456]);
    });

    test('should handle null input', () => {
      const result = stringService.extractNumbers(null);
      expect(result).toEqual([]);
    });

    test('should handle undefined input', () => {
      const result = stringService.extractNumbers(undefined);
      expect(result).toEqual([]);
    });

    test.each([
      ['hello 123 world 456', [123, 456]],
      ['test 1 2 3', [1, 2, 3]],
      ['no numbers here', []],
      ['42 is the answer', [42]]
    ])('should extract numbers from "%s" as %p', (text, expected) => {
      const result = stringService.extractNumbers(text);
      expect(result).toEqual(expected);
    });
  });

  describe('Remove Special Characters', () => {
    test('should remove special characters correctly', () => {
      const result = stringService.removeSpecialChars('hello@world!');
      expect(result).toBe('hello world');
    });

    test('should handle null input', () => {
      const result = stringService.removeSpecialChars(null);
      expect(result).toBeNull();
    });

    test('should handle undefined input', () => {
      const result = stringService.removeSpecialChars(undefined);
      expect(result).toBeNull();
    });

    test.each([
      ['hello@world!', 'hello world'],
      ['test#case$', 'test case'],
      ['no-special-chars', 'no special chars'],
      ['clean text', 'clean text']
    ])('should remove special chars from "%s" to "%s"', (input, expected) => {
      const result = stringService.removeSpecialChars(input);
      expect(result).toBe(expected);
    });
  });
});
