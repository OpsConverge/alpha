"""
pytest unit tests for StringService - Working Version
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
        
        def test_reverse_simple_string(self, string_service):
            """Test reversing a simple string"""
            result = string_service.reverse("hello")
            assert result == "olleh"
        
        def test_reverse_empty_string(self, string_service):
            """Test reversing an empty string"""
            result = string_service.reverse("")
            assert result == ""
        
        def test_reverse_single_character(self, string_service):
            """Test reversing a single character"""
            result = string_service.reverse("a")
            assert result == "a"
        
        @pytest.mark.parametrize("input_str, expected", [
            ("hello", "olleh"),
            ("world", "dlrow"),
            ("python", "nohtyp"),
            ("12345", "54321"),
            ("", ""),
            ("a", "a")
        ])
        def test_reverse_various_strings(self, string_service, input_str, expected):
            """Test reversing various strings"""
            result = string_service.reverse(input_str)
            assert result == expected
    
    class TestToUpperCase:
        """Test to_upper_case operations"""
        
        def test_to_upper_case_simple_string(self, string_service):
            """Test converting simple string to uppercase"""
            result = string_service.to_upper_case("hello")
            assert result == "HELLO"
        
        def test_to_upper_case_already_uppercase(self, string_service):
            """Test converting already uppercase string"""
            result = string_service.to_upper_case("HELLO")
            assert result == "HELLO"
        
        def test_to_upper_case_mixed_case(self, string_service):
            """Test converting mixed case string"""
            result = string_service.to_upper_case("HeLLo WoRLd")
            assert result == "HELLO WORLD"
        
        @pytest.mark.parametrize("input_str, expected", [
            ("hello", "HELLO"),
            ("world", "WORLD"),
            ("python", "PYTHON"),
            ("HELLO", "HELLO"),
            ("", ""),
            ("a", "A")
        ])
        def test_to_upper_case_various_strings(self, string_service, input_str, expected):
            """Test converting various strings to uppercase"""
            result = string_service.to_upper_case(input_str)
            assert result == expected
    
    class TestToLowerCase:
        """Test to_lower_case operations"""
        
        def test_to_lower_case_simple_string(self, string_service):
            """Test converting simple string to lowercase"""
            result = string_service.to_lower_case("HELLO")
            assert result == "hello"
        
        def test_to_lower_case_already_lowercase(self, string_service):
            """Test converting already lowercase string"""
            result = string_service.to_lower_case("hello")
            assert result == "hello"
        
        def test_to_lower_case_mixed_case(self, string_service):
            """Test converting mixed case string"""
            result = string_service.to_lower_case("HeLLo WoRLd")
            assert result == "hello world"
        
        @pytest.mark.parametrize("input_str, expected", [
            ("HELLO", "hello"),
            ("WORLD", "world"),
            ("PYTHON", "python"),
            ("hello", "hello"),
            ("", ""),
            ("A", "a")
        ])
        def test_to_lower_case_various_strings(self, string_service, input_str, expected):
            """Test converting various strings to lowercase"""
            result = string_service.to_lower_case(input_str)
            assert result == expected
    
    class TestCountVowels:
        """Test count_vowels operations"""
        
        def test_count_vowels_simple_string(self, string_service):
            """Test counting vowels in simple string"""
            result = string_service.count_vowels("hello")
            assert result == 2
        
        def test_count_vowels_no_vowels(self, string_service):
            """Test counting vowels in string with no vowels"""
            result = string_service.count_vowels("rhythm")
            assert result == 0
        
        def test_count_vowels_all_vowels(self, string_service):
            """Test counting vowels in string with all vowels"""
            result = string_service.count_vowels("aeiou")
            assert result == 5
        
        @pytest.mark.parametrize("input_str, expected", [
            ("hello", 2),
            ("world", 1),
            ("python", 1),
            ("aeiou", 5),
            ("rhythm", 0),
            ("", 0),
            ("a", 1)
        ])
        def test_count_vowels_various_strings(self, string_service, input_str, expected):
            """Test counting vowels in various strings"""
            result = string_service.count_vowels(input_str)
            assert result == expected
    
    class TestRemoveSpecialChars:
        """Test remove_special_chars operations"""
        
        def test_remove_special_chars_simple_string(self, string_service):
            """Test removing special characters from simple string"""
            result = string_service.remove_special_chars("hello@world!")
            assert result == "helloworld"
        
        def test_remove_special_chars_no_special_chars(self, string_service):
            """Test removing special characters from string with no special chars"""
            result = string_service.remove_special_chars("hello world")
            assert result == "helloworld"
        
        def test_remove_special_chars_only_special_chars(self, string_service):
            """Test removing special characters from string with only special chars"""
            result = string_service.remove_special_chars("@#$%^&*()")
            assert result == ""
        
        @pytest.mark.parametrize("input_str, expected", [
            ("hello@world!", "helloworld"),
            ("python#123", "python123"),
            ("test$string%", "teststring"),
            ("no_special_chars", "nospecialchars"),
            ("", ""),
            ("a", "a")
        ])
        def test_remove_special_chars_various_strings(self, string_service, input_str, expected):
            """Test removing special characters from various strings"""
            result = string_service.remove_special_chars(input_str)
            assert result == expected

