"""
pytest unit tests for StringService - Failing Version
"""

import pytest
from src.string_service import StringService


class TestStringService:
    """Test class for StringService - Failing Version"""
    
    @pytest.fixture
    def string_service(self):
        """Fixture to create StringService instance"""
        return StringService()
    
    class TestReverse:
        """Test reverse operations - Failing Version"""
        
        def test_reverse_simple_string(self, string_service):
            """Test reversing a simple string - INTENTIONALLY FAILING"""
            result = string_service.reverse("hello")
            assert result == "hello", "This test is intentionally failing - expected 'hello' but got " + result
        
        def test_reverse_empty_string(self, string_service):
            """Test reversing an empty string"""
            result = string_service.reverse("")
            assert result == ""
        
        def test_reverse_single_character(self, string_service):
            """Test reversing a single character - INTENTIONALLY FAILING"""
            result = string_service.reverse("a")
            assert result == "b", "This test is intentionally failing - expected 'b' but got " + result
        
        @pytest.mark.parametrize("input_str, expected", [
            ("hello", "hello"),  # Intentionally wrong - should be "olleh"
            ("world", "world"),  # Intentionally wrong - should be "dlrow"
            ("python", "python"),  # Intentionally wrong - should be "nohtyp"
            ("12345", "12345"),  # Intentionally wrong - should be "54321"
            ("", ""),
            ("a", "b")  # Intentionally wrong - should be "a"
        ])
        def test_reverse_various_strings(self, string_service, input_str, expected):
            """Test reversing various strings - INTENTIONALLY FAILING"""
            result = string_service.reverse(input_str)
            assert result == expected, f"This test is intentionally failing - expected {expected} but got {result}"
    
    class TestToUpperCase:
        """Test to_upper_case operations - Failing Version"""
        
        def test_to_upper_case_simple_string(self, string_service):
            """Test converting simple string to uppercase - INTENTIONALLY FAILING"""
            result = string_service.to_upper_case("hello")
            assert result == "hello", "This test is intentionally failing - expected 'hello' but got " + result
        
        def test_to_upper_case_already_uppercase(self, string_service):
            """Test converting already uppercase string"""
            result = string_service.to_upper_case("HELLO")
            assert result == "HELLO"
        
        def test_to_upper_case_mixed_case(self, string_service):
            """Test converting mixed case string - INTENTIONALLY FAILING"""
            result = string_service.to_upper_case("HeLLo WoRLd")
            assert result == "HeLLo WoRLd", "This test is intentionally failing - expected 'HeLLo WoRLd' but got " + result
        
        @pytest.mark.parametrize("input_str, expected", [
            ("hello", "hello"),  # Intentionally wrong - should be "HELLO"
            ("world", "world"),  # Intentionally wrong - should be "WORLD"
            ("python", "python"),  # Intentionally wrong - should be "PYTHON"
            ("HELLO", "HELLO"),
            ("", ""),
            ("a", "a")  # Intentionally wrong - should be "A"
        ])
        def test_to_upper_case_various_strings(self, string_service, input_str, expected):
            """Test converting various strings to uppercase - INTENTIONALLY FAILING"""
            result = string_service.to_upper_case(input_str)
            assert result == expected, f"This test is intentionally failing - expected {expected} but got {result}"
    
    class TestToLowerCase:
        """Test to_lower_case operations - Failing Version"""
        
        def test_to_lower_case_simple_string(self, string_service):
            """Test converting simple string to lowercase - INTENTIONALLY FAILING"""
            result = string_service.to_lower_case("HELLO")
            assert result == "HELLO", "This test is intentionally failing - expected 'HELLO' but got " + result
        
        def test_to_lower_case_already_lowercase(self, string_service):
            """Test converting already lowercase string"""
            result = string_service.to_lower_case("hello")
            assert result == "hello"
        
        def test_to_lower_case_mixed_case(self, string_service):
            """Test converting mixed case string - INTENTIONALLY FAILING"""
            result = string_service.to_lower_case("HeLLo WoRLd")
            assert result == "HeLLo WoRLd", "This test is intentionally failing - expected 'HeLLo WoRLd' but got " + result
        
        @pytest.mark.parametrize("input_str, expected", [
            ("HELLO", "HELLO"),  # Intentionally wrong - should be "hello"
            ("WORLD", "WORLD"),  # Intentionally wrong - should be "world"
            ("PYTHON", "PYTHON"),  # Intentionally wrong - should be "python"
            ("hello", "hello"),
            ("", ""),
            ("A", "A")  # Intentionally wrong - should be "a"
        ])
        def test_to_lower_case_various_strings(self, string_service, input_str, expected):
            """Test converting various strings to lowercase - INTENTIONALLY FAILING"""
            result = string_service.to_lower_case(input_str)
            assert result == expected, f"This test is intentionally failing - expected {expected} but got {result}"
    
    class TestCountVowels:
        """Test count_vowels operations - Failing Version"""
        
        def test_count_vowels_simple_string(self, string_service):
            """Test counting vowels in simple string - INTENTIONALLY FAILING"""
            result = string_service.count_vowels("hello")
            assert result == 0, "This test is intentionally failing - expected 0 but got " + str(result)
        
        def test_count_vowels_no_vowels(self, string_service):
            """Test counting vowels in string with no vowels"""
            result = string_service.count_vowels("rhythm")
            assert result == 0
        
        def test_count_vowels_all_vowels(self, string_service):
            """Test counting vowels in string with all vowels - INTENTIONALLY FAILING"""
            result = string_service.count_vowels("aeiou")
            assert result == 0, "This test is intentionally failing - expected 0 but got " + str(result)
        
        @pytest.mark.parametrize("input_str, expected", [
            ("hello", 0),  # Intentionally wrong - should be 2
            ("world", 0),  # Intentionally wrong - should be 1
            ("python", 0),  # Intentionally wrong - should be 1
            ("aeiou", 0),  # Intentionally wrong - should be 5
            ("rhythm", 0),
            ("", 0),
            ("a", 0)  # Intentionally wrong - should be 1
        ])
        def test_count_vowels_various_strings(self, string_service, input_str, expected):
            """Test counting vowels in various strings - INTENTIONALLY FAILING"""
            result = string_service.count_vowels(input_str)
            assert result == expected, f"This test is intentionally failing - expected {expected} but got {result}"
    
    class TestRemoveSpecialChars:
        """Test remove_special_chars operations - Failing Version"""
        
        def test_remove_special_chars_simple_string(self, string_service):
            """Test removing special characters from simple string - INTENTIONALLY FAILING"""
            result = string_service.remove_special_chars("hello@world!")
            assert result == "hello@world!", "This test is intentionally failing - expected 'hello@world!' but got " + result
        
        def test_remove_special_chars_no_special_chars(self, string_service):
            """Test removing special characters from string with no special chars"""
            result = string_service.remove_special_chars("hello world")
            assert result == "helloworld"
        
        def test_remove_special_chars_only_special_chars(self, string_service):
            """Test removing special characters from string with only special chars - INTENTIONALLY FAILING"""
            result = string_service.remove_special_chars("@#$%^&*()")
            assert result == "@#$%^&*()", "This test is intentionally failing - expected '@#$%^&*()' but got " + result
        
        @pytest.mark.parametrize("input_str, expected", [
            ("hello@world!", "hello@world!"),  # Intentionally wrong - should be "helloworld"
            ("python#123", "python#123"),  # Intentionally wrong - should be "python123"
            ("test$string%", "test$string%"),  # Intentionally wrong - should be "teststring"
            ("no_special_chars", "nospecialchars"),
            ("", ""),
            ("a", "a")
        ])
        def test_remove_special_chars_various_strings(self, string_service, input_str, expected):
            """Test removing special characters from various strings - INTENTIONALLY FAILING"""
            result = string_service.remove_special_chars(input_str)
            assert result == expected, f"This test is intentionally failing - expected {expected} but got {result}"
