/**
 * String Service for Jest unit testing
 */

class StringService {
  /**
   * Reverse a string
   * @param {string} text - Text to reverse
   * @returns {string} Reversed text or null if input is null
   */
  reverse(text) {
    if (text === null || text === undefined) {
      return null;
    }
    return text.split('').reverse().join('');
  }

  /**
   * Check if a string is palindrome
   * @param {string} text - Text to check
   * @returns {boolean} True if palindrome, false otherwise
   */
  isPalindrome(text) {
    if (text === null || text === undefined) {
      return false;
    }
    const cleaned = text.toLowerCase().replace(/[^a-zA-Z0-9]/g, '');
    return cleaned === this.reverse(cleaned);
  }

  /**
   * Count vowels in a string
   * @param {string} text - Text to count vowels in
   * @returns {number} Number of vowels
   */
  countVowels(text) {
    if (text === null || text === undefined || typeof text !== 'string') {
      return 0;
    }
    const vowels = 'aeiouAEIOU';
    return text.split('').filter(char => vowels.includes(char)).length;
  }

  /**
   * Convert string to title case
   * @param {string} text - Text to convert
   * @returns {string} Title case text or original if null/empty
   */
  toTitleCase(text) {
    if (text === null || text === undefined || text.trim() === '') {
      return text;
    }
    return text.toLowerCase().replace(/\b\w/g, char => char.toUpperCase());
  }

  /**
   * Remove duplicate characters from string
   * @param {string} text - Text to remove duplicates from
   * @returns {string} Text with duplicates removed or null if input is null
   */
  removeDuplicates(text) {
    if (text === null || text === undefined) {
      return null;
    }
    const seen = new Set();
    const result = [];
    for (const char of text) {
      if (!seen.has(char)) {
        seen.add(char);
        result.push(char);
      }
    }
    return result.join('');
  }

  /**
   * Find the longest word in a string
   * @param {string} text - Text to find longest word in
   * @returns {string} Longest word or empty string if no words
   */
  findLongestWord(text) {
    if (text === null || text === undefined || text.trim() === '') {
      return '';
    }
    const words = text.split(/\s+/);
    if (words.length === 0) {
      return '';
    }
    return words.reduce((longest, current) => 
      current.length > longest.length ? current : longest
    );
  }

  /**
   * Count words in a string
   * @param {string} text - Text to count words in
   * @returns {number} Number of words
   */
  countWords(text) {
    if (text === null || text === undefined || text.trim() === '') {
      return 0;
    }
    return text.trim().split(/\s+/).length;
  }

  /**
   * Check if two strings are anagrams
   * @param {string} text1 - First text
   * @param {string} text2 - Second text
   * @returns {boolean} True if anagrams, false otherwise
   */
  isAnagram(text1, text2) {
    if (text1 === null || text2 === null || text1 === undefined || text2 === undefined) {
      return false;
    }
    const clean1 = text1.toLowerCase().replace(/\s/g, '');
    const clean2 = text2.toLowerCase().replace(/\s/g, '');
    return clean1.split('').sort().join('') === clean2.split('').sort().join('');
  }

  /**
   * Capitalize first letter of each word
   * @param {string} text - Text to capitalize
   * @returns {string} Text with capitalized words or null if input is null
   */
  capitalizeWords(text) {
    if (text === null || text === undefined) {
      return null;
    }
    return text.split(' ').map(word => 
      word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
    ).join(' ');
  }

  /**
   * Count occurrences of a substring in a string
   * @param {string} text - Text to search in
   * @param {string} substring - Substring to count
   * @returns {number} Number of occurrences
   */
  countOccurrences(text, substring) {
    if (text === null || substring === null || text === undefined || substring === undefined || typeof text !== 'string') {
      return 0;
    }
    const regex = new RegExp(substring, 'g');
    const matches = text.match(regex);
    return matches ? matches.length : 0;
  }

  /**
   * Check if email is valid
   * @param {string} email - Email to validate
   * @returns {boolean} True if valid email, false otherwise
   */
  isValidEmail(email) {
    if (email === null || email === undefined) {
      return false;
    }
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
  }

  /**
   * Extract all numbers from a string
   * @param {string} text - Text to extract numbers from
   * @returns {number[]} Array of numbers found
   */
  extractNumbers(text) {
    if (text === null || text === undefined) {
      return [];
    }
    const numbers = text.match(/\d+/g);
    return numbers ? numbers.map(num => parseInt(num, 10)) : [];
  }

  /**
   * Remove special characters from string
   * @param {string} text - Text to clean
   * @returns {string} Text with special characters removed or null if input is null
   */
  removeSpecialChars(text) {
    if (text === null || text === undefined) {
      return null;
    }
    // Replace special characters with spaces, then clean up
    let result = text.replace(/[^a-zA-Z0-9\s]/g, ' ');
    // Replace multiple spaces with single space
    result = result.replace(/\s+/g, ' ');
    return result.trim();
  }
}

module.exports = StringService;
