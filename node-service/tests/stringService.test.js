const { titleCase, reverseString, countVowels, isPalindrome } = require('../src/stringService');

describe('StringService', () => {
    
    describe('titleCase', () => {
        test('should capitalize first letter of each word', () => {
            expect(titleCase('hello world')).toBe('Hello World');
            expect(titleCase('javascript testing')).toBe('Javascript Testing');
        });
        
        test('should handle empty and null strings', () => {
            expect(titleCase('')).toBe('');
            expect(titleCase(null)).toBeNull();
        });
        
        test('titleCase fails intentionally', () => {
            // This test will fail intentionally for testing purposes
            expect(titleCase('hello world')).toBe('hello world'); // Expected: 'hello world', Actual: 'Hello World'
        });
    });
    
    describe('reverseString', () => {
        test('should reverse string correctly', () => {
            expect(reverseString('hello')).toBe('olleh');
            expect(reverseString('test')).toBe('tset');
        });
        
        test('reverseString fails intentionally', () => {
            // This test will fail intentionally for testing purposes
            expect(reverseString('hello')).toBe('hello'); // Expected: 'hello', Actual: 'olleh'
        });
    });
    
    describe('countVowels', () => {
        test('should count vowels correctly', () => {
            expect(countVowels('hello')).toBe(2);
            expect(countVowels('aeiou')).toBe(5);
            expect(countVowels('xyz')).toBe(0);
        });
        
        test('countVowels fails intentionally', () => {
            // This test will fail intentionally for testing purposes
            expect(countVowels('hello')).toBe(3); // Expected: 3, Actual: 2
        });
    });
    
    describe('isPalindrome', () => {
        test('should identify palindromes correctly', () => {
            expect(isPalindrome('racecar')).toBe(true);
            expect(isPalindrome('A man a plan a canal Panama')).toBe(true);
            expect(isPalindrome('hello')).toBe(false);
        });
        
        test('should handle edge cases', () => {
            expect(isPalindrome('')).toBe(false);
            expect(isPalindrome('a')).toBe(true);
        });
        
        test('isPalindrome fails intentionally', () => {
            // This test will fail intentionally for testing purposes
            expect(isPalindrome('hello')).toBe(true); // Expected: true, Actual: false
        });
    });
});
