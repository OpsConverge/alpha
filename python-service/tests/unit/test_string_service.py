"""
pytest unit tests for StringService
"""

import pytest
from src.string_service import StringService


class TestStringService:
    """Test class for StringService"""
    
    @pytest.fixture
    def string_service(self):
        """Fixture to create StringService instance"""
        return StringService()
    
    class TestReverse:
        """Test reverse operations"""
        
        def test_reverse_string(self, string_service):
            """Test reversing a string"""
            result = string_service.reverse("hello")
            assert result == "olleh"
        
        # def test_.*_failing(self, string_service):
            """Test reversing a string - INTENTIONALLY FAILING"""
            result = string_service.reverse("hello")
            assert result == "hello"  # This will fail - should be "olleh"
        
        def test_reverse_empty_string(self, string_service):
            """Test reversing empty string"""
            result = string_service.reverse("")
            assert result == ""
        
        def test_reverse_single_character(self, string_service):
            """Test reversing single character"""
            result = string_service.reverse("a")
            assert result == "a"
        
        def test_reverse_none(self, string_service):
            """Test reversing None"""
            result = string_service.reverse(None)
            assert result is None
        
        @pytest.mark.parametrize("input_text, expected", [
            ("hello", "olleh"),
            ("world", "dlrow"),
            ("12345", "54321"),
            ("racecar", "racecar"),
            ("A", "A")
        ])
        def test_reverse_various_strings(self, string_service, input_text, expected):
            """Test reversing various strings"""
            result = string_service.reverse(input_text)
            assert result == expected
    
    class TestPalindrome:
        """Test palindrome operations"""
        
        def test_is_palindrome_true(self, string_service):
            """Test that palindromes return True"""
            assert string_service.is_palindrome("racecar") is True
            assert string_service.is_palindrome("level") is True
        
        def test_is_palindrome_false(self, string_service):
            """Test that non-palindromes return False"""
            assert string_service.is_palindrome("hello") is False
            assert string_service.is_palindrome("world") is False
        
        def test_is_palindrome_with_spaces_punctuation(self, string_service):
            """Test palindrome with spaces and punctuation"""
            assert string_service.is_palindrome("A man, a plan, a canal: Panama") is True
        
        def test_is_palindrome_none(self, string_service):
            """Test palindrome with None"""
            assert string_service.is_palindrome(None) is False
        
        @pytest.mark.parametrize("input_text, expected", [
            ("racecar", True),
            ("level", True),
            ("deed", True),
            ("noon", True),
            ("civic", True),
            ("radar", True),
            ("hello", False),
            ("world", False),
            ("test", False),
            ("java", False)
        ])
        def test_is_palindrome_various_strings(self, string_service, input_text, expected):
            """Test is_palindrome for various strings"""
            result = string_service.is_palindrome(input_text)
            assert result == expected
    
    class TestCountVowels:
        """Test vowel counting operations"""
        
        def test_count_vowels(self, string_service):
            """Test counting vowels"""
            result = string_service.count_vowels("hello")
            assert result == 2
        
        def test_count_vowels_no_vowels(self, string_service):
            """Test counting vowels in string with no vowels"""
            result = string_service.count_vowels("rhythm")
            assert result == 0
        
        def test_count_vowels_none(self, string_service):
            """Test counting vowels in None"""
            result = string_service.count_vowels(None)
            assert result == 0
        
        @pytest.mark.parametrize("input_text, expected", [
            ("hello", 2),
            ("world", 1),
            ("aeiou", 5),
            ("rhythm", 0),
            ("programming", 3),
            ("TEST", 1)
        ])
        def test_count_vowels_various_strings(self, string_service, input_text, expected):
            """Test count_vowels for various strings"""
            result = string_service.count_vowels(input_text)
            assert result == expected
    
    class TestTitleCase:
        """Test title case operations"""
        
        def test_to_title_case(self, string_service):
            """Test converting to title case"""
            result = string_service.to_title_case("hello world")
            assert result == "Hello World"
        
        def test_to_title_case_single_word(self, string_service):
            """Test converting single word to title case"""
            result = string_service.to_title_case("hello")
            assert result == "Hello"
        
        def test_to_title_case_empty_string(self, string_service):
            """Test converting empty string to title case"""
            result = string_service.to_title_case("")
            assert result == ""
        
        def test_to_title_case_none(self, string_service):
            """Test converting None to title case"""
            result = string_service.to_title_case(None)
            assert result is None
        
        @pytest.mark.parametrize("input_text, expected", [
            ("hello world", "Hello World"),
            ("JAVA PROGRAMMING", "Java Programming"),
            ("test case", "Test Case"),
            ("single", "Single"),
            ("multiple   spaces", "Multiple   Spaces")
        ])
        def test_to_title_case_various_strings(self, string_service, input_text, expected):
            """Test to_title_case for various strings"""
            result = string_service.to_title_case(input_text)
            assert result == expected
    
    class TestRemoveDuplicates:
        """Test duplicate removal operations"""
        
        def test_remove_duplicates(self, string_service):
            """Test removing duplicate characters"""
            result = string_service.remove_duplicates("hello")
            assert result == "helo"
        
        def test_remove_duplicates_no_duplicates(self, string_service):
            """Test removing duplicates from string with no duplicates"""
            result = string_service.remove_duplicates("world")
            assert result == "world"
        
        def test_remove_duplicates_none(self, string_service):
            """Test removing duplicates from None"""
            result = string_service.remove_duplicates(None)
            assert result is None
        
        @pytest.mark.parametrize("input_text, expected", [
            ("hello", "helo"),
            ("world", "world"),
            ("programming", "progamin"),
            ("test", "tes"),
            ("aaaaa", "a"),
            ("abcabc", "abc")
        ])
        def test_remove_duplicates_various_strings(self, string_service, input_text, expected):
            """Test remove_duplicates for various strings"""
            result = string_service.remove_duplicates(input_text)
            assert result == expected
    
    class TestFindLongestWord:
        """Test longest word finding operations"""
        
        def test_find_longest_word(self, string_service):
            """Test finding longest word"""
            result = string_service.find_longest_word("hello world programming")
            assert result == "programming"
        
        def test_find_longest_word_single_word(self, string_service):
            """Test finding longest word in single word"""
            result = string_service.find_longest_word("hello")
            assert result == "hello"
        
        def test_find_longest_word_empty_string(self, string_service):
            """Test finding longest word in empty string"""
            result = string_service.find_longest_word("")
            assert result == ""
        
        def test_find_longest_word_none(self, string_service):
            """Test finding longest word in None"""
            result = string_service.find_longest_word(None)
            assert result == ""
        
        @pytest.mark.parametrize("input_text, expected", [
            ("hello world programming", "programming"),
            ("test case example", "example"),
            ("java python javascript", "javascript"),
            ("a bb ccc", "ccc"),
            ("short medium long", "medium")
        ])
        def test_find_longest_word_various_strings(self, string_service, input_text, expected):
            """Test find_longest_word for various strings"""
            result = string_service.find_longest_word(input_text)
            assert result == expected
    
    class TestCountWords:
        """Test word counting operations"""
        
        def test_count_words(self, string_service):
            """Test counting words"""
            result = string_service.count_words("hello world programming")
            assert result == 3
        
        def test_count_words_single_word(self, string_service):
            """Test counting words in single word"""
            result = string_service.count_words("hello")
            assert result == 1
        
        def test_count_words_empty_string(self, string_service):
            """Test counting words in empty string"""
            result = string_service.count_words("")
            assert result == 0
        
        def test_count_words_none(self, string_service):
            """Test counting words in None"""
            result = string_service.count_words(None)
            assert result == 0
    
    class TestAnagram:
        """Test anagram operations"""
        
        def test_is_anagram_true(self, string_service):
            """Test that anagrams return True"""
            assert string_service.is_anagram("listen", "silent") is True
            assert string_service.is_anagram("debit card", "bad credit") is True
        
        def test_is_anagram_false(self, string_service):
            """Test that non-anagrams return False"""
            assert string_service.is_anagram("hello", "world") is False
        
        def test_is_anagram_none(self, string_service):
            """Test anagram with None"""
            assert string_service.is_anagram(None, "test") is False
            assert string_service.is_anagram("test", None) is False
        
        @pytest.mark.parametrize("text1, text2, expected", [
            ("listen", "silent", True),
            ("hello", "world", False),
            ("debit card", "bad credit", True),
            ("funeral", "real fun", True),
            ("school master", "the classroom", True)
        ])
        def test_is_anagram_various_strings(self, string_service, text1, text2, expected):
            """Test is_anagram for various string combinations"""
            result = string_service.is_anagram(text1, text2)
            assert result == expected
    
    class TestCapitalizeWords:
        """Test word capitalization operations"""
        
        def test_capitalize_words(self, string_service):
            """Test capitalizing words"""
            result = string_service.capitalize_words("hello world")
            assert result == "Hello World"
        
        def test_capitalize_words_none(self, string_service):
            """Test capitalizing words in None"""
            result = string_service.capitalize_words(None)
            assert result is None
        
        @pytest.mark.parametrize("input_text, expected", [
            ("hello world", "Hello World"),
            ("python programming", "Python Programming"),
            ("test case", "Test Case"),
            ("single", "Single")
        ])
        def test_capitalize_words_various_strings(self, string_service, input_text, expected):
            """Test capitalize_words for various strings"""
            result = string_service.capitalize_words(input_text)
            assert result == expected
    
    class TestCountOccurrences:
        """Test occurrence counting operations"""
        
        def test_count_occurrences(self, string_service):
            """Test counting occurrences"""
            result = string_service.count_occurrences("hello world hello", "hello")
            assert result == 2
        
        def test_count_occurrences_none(self, string_service):
            """Test counting occurrences in None"""
            result = string_service.count_occurrences(None, "test")
            assert result == 0
        
        @pytest.mark.parametrize("text, substring, expected", [
            ("hello world hello", "hello", 2),
            ("test test test", "test", 3),
            ("python programming", "python", 1),
            ("no match", "missing", 0)
        ])
        def test_count_occurrences_various_strings(self, string_service, text, substring, expected):
            """Test count_occurrences for various strings"""
            result = string_service.count_occurrences(text, substring)
            assert result == expected
    
    class TestValidEmail:
        """Test email validation operations"""
        
        def test_is_valid_email_true(self, string_service):
            """Test that valid emails return True"""
            assert string_service.is_valid_email("test@example.com") is True
            assert string_service.is_valid_email("user.name@domain.co.uk") is True
        
        def test_is_valid_email_false(self, string_service):
            """Test that invalid emails return False"""
            assert string_service.is_valid_email("invalid-email") is False
            assert string_service.is_valid_email("@domain.com") is False
        
        def test_is_valid_email_none(self, string_service):
            """Test email validation with None"""
            assert string_service.is_valid_email(None) is False
        
        @pytest.mark.parametrize("email, expected", [
            ("test@example.com", True),
            ("user.name@domain.co.uk", True),
            ("invalid-email", False),
            ("@domain.com", False),
            ("test@", False),
            ("test.domain.com", False)
        ])
        def test_is_valid_email_various_strings(self, string_service, email, expected):
            """Test is_valid_email for various emails"""
            result = string_service.is_valid_email(email)
            assert result == expected
    
    class TestExtractNumbers:
        """Test number extraction operations"""
        
        def test_extract_numbers(self, string_service):
            """Test extracting numbers"""
            result = string_service.extract_numbers("hello 123 world 456")
            assert result == [123, 456]
        
        def test_extract_numbers_none(self, string_service):
            """Test extracting numbers from None"""
            result = string_service.extract_numbers(None)
            assert result == []
        
        @pytest.mark.parametrize("text, expected", [
            ("hello 123 world 456", [123, 456]),
            ("test 1 2 3", [1, 2, 3]),
            ("no numbers here", []),
            ("42 is the answer", [42])
        ])
        def test_extract_numbers_various_strings(self, string_service, text, expected):
            """Test extract_numbers for various strings"""
            result = string_service.extract_numbers(text)
            assert result == expected
    
    class TestRemoveSpecialChars:
        """Test special character removal operations"""
        
        def test_remove_special_chars(self, string_service):
            """Test removing special characters"""
            result = string_service.remove_special_chars("hello@world!")
            assert result == "hello world"
        
        def test_remove_special_chars_none(self, string_service):
            """Test removing special characters from None"""
            result = string_service.remove_special_chars(None)
            assert result is None
        
        @pytest.mark.parametrize("text, expected", [
            ("hello@world!", "hello world"),
            ("test#case$", "test case"),
            ("no-special-chars", "no special chars"),
            ("clean text", "clean text")
        ])
        def test_remove_special_chars_various_strings(self, string_service, text, expected):
            """Test remove_special_chars for various strings"""
            result = string_service.remove_special_chars(text)
            assert result == expected
