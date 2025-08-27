"""
String Service for pytest unit testing
"""

import re
from typing import List, Optional


class StringService:
    """Service class for string operations"""
    
    def reverse(self, text: Optional[str]) -> Optional[str]:
        """Reverse a string"""
        if text is None:
            return None
        return text[::-1]
    
    def is_palindrome(self, text: Optional[str]) -> bool:
        """Check if a string is palindrome"""
        if text is None:
            return False
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
        return cleaned == cleaned[::-1]
    
    def count_vowels(self, text: Optional[str]) -> int:
        """Count vowels in a string"""
        if text is None:
            return 0
        vowels = 'aeiouAEIOU'
        return sum(1 for char in text if char in vowels)
    
    def to_title_case(self, text: Optional[str]) -> Optional[str]:
        """Convert string to title case"""
        if text is None or text.strip() == "":
            return text
        return text.title()
    
    def remove_duplicates(self, text: Optional[str]) -> Optional[str]:
        """Remove duplicate characters from string"""
        if text is None:
            return None
        seen = set()
        result = ""
        for char in text:
            if char not in seen:
                seen.add(char)
                result += char
        return result
    
    def find_longest_word(self, text: Optional[str]) -> str:
        """Find the longest word in a string"""
        if text is None or text.strip() == "":
            return ""
        words = text.split()
        if not words:
            return ""
        return max(words, key=len)
    
    def count_words(self, text: Optional[str]) -> int:
        """Count words in a string"""
        if text is None or text.strip() == "":
            return 0
        return len(text.split())
    
    def is_anagram(self, text1: Optional[str], text2: Optional[str]) -> bool:
        """Check if two strings are anagrams"""
        if text1 is None or text2 is None:
            return False
        # Remove spaces and convert to lowercase
        text1_clean = re.sub(r'\s', '', text1.lower())
        text2_clean = re.sub(r'\s', '', text2.lower())
        return sorted(text1_clean) == sorted(text2_clean)
    
    def capitalize_words(self, text: Optional[str]) -> Optional[str]:
        """Capitalize first letter of each word"""
        if text is None:
            return None
        return ' '.join(word.capitalize() for word in text.split())
    
    def count_occurrences(self, text: Optional[str], substring: str) -> int:
        """Count occurrences of a substring in a string"""
        if text is None or substring is None:
            return 0
        return text.count(substring)
    
    def is_valid_email(self, email: Optional[str]) -> bool:
        """Check if email is valid"""
        if email is None:
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def extract_numbers(self, text: Optional[str]) -> List[int]:
        """Extract all numbers from a string"""
        if text is None:
            return []
        numbers = re.findall(r'\d+', text)
        return [int(num) for num in numbers]
    
    def remove_special_chars(self, text: Optional[str]) -> Optional[str]:
        """Remove special characters from string"""
        if text is None:
            return None
        # Replace special characters with spaces, then clean up
        result = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
        # Replace multiple spaces with single space
        result = re.sub(r'\s+', ' ', result)
        return result.strip()
