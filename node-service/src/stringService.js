/**
 * String utility functions for testing purposes
 */

function titleCase(str) {
    if (!str) return str;
    return str.toLowerCase().split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

function reverseString(str) {
    if (!str) return str;
    return str.split('').reverse().join('');
}

function countVowels(str) {
    if (!str) return 0;
    return str.toLowerCase().match(/[aeiou]/g)?.length || 0;
}

function isPalindrome(str) {
    if (!str) return false;
    const clean = str.toLowerCase().replace(/[^a-z0-9]/g, '');
    return clean === clean.split('').reverse().join('');
}

module.exports = {
    titleCase,
    reverseString,
    countVowels,
    isPalindrome
};
