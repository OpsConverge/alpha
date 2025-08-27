package com.example.unit;

import com.example.StringService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("StringService Unit Tests")
class StringServiceTest {

    private StringService stringService;

    @BeforeEach
    void setUp() {
        stringService = new StringService();
    }

    @Nested
    @DisplayName("Reverse Tests")
    class ReverseTests {

        @Test
        @DisplayName("Should reverse a string correctly")
        void shouldReverseStringCorrectly() {
            // Given
            String input = "hello";

            // When
            String result = stringService.reverse(input);

            // Then
            assertEquals("olleh", result);
        }

        @Test
        @DisplayName("Should handle empty string")
        void shouldHandleEmptyString() {
            // Given
            String input = "";

            // When
            String result = stringService.reverse(input);

            // Then
            assertEquals("", result);
        }

        @Test
        @DisplayName("Should handle single character")
        void shouldHandleSingleCharacter() {
            // Given
            String input = "a";

            // When
            String result = stringService.reverse(input);

            // Then
            assertEquals("a", result);
        }

        @Test
        @DisplayName("Should handle null input")
        void shouldHandleNullInput() {
            // Given
            String input = null;

            // When
            String result = stringService.reverse(input);

            // Then
            assertNull(result);
        }

        @ParameterizedTest
        @CsvSource({
            "hello, olleh",
            "world, dlrow",
            "12345, 54321",
            "racecar, racecar",
            "A, A"
        })
        @DisplayName("Should reverse various strings")
        void shouldReverseVariousStrings(String input, String expected) {
            // When
            String result = stringService.reverse(input);

            // Then
            assertEquals(expected, result);
        }
    }

    @Nested
    @DisplayName("Palindrome Tests")
    class PalindromeTests {

        @Test
        @DisplayName("Should identify palindrome correctly")
        void shouldIdentifyPalindromeCorrectly() {
            // Given
            String input = "racecar";

            // When
            boolean result = stringService.isPalindrome(input);

            // Then
            assertTrue(result);
        }

        @Test
        @DisplayName("Should identify non-palindrome correctly")
        void shouldIdentifyNonPalindromeCorrectly() {
            // Given
            String input = "hello";

            // When
            boolean result = stringService.isPalindrome(input);

            // Then
            assertFalse(result);
        }

        @Test
        @DisplayName("Should handle palindrome with spaces and punctuation")
        void shouldHandlePalindromeWithSpacesAndPunctuation() {
            // Given
            String input = "A man, a plan, a canal: Panama";

            // When
            boolean result = stringService.isPalindrome(input);

            // Then
            assertTrue(result);
        }

        @Test
        @DisplayName("Should handle null input")
        void shouldHandleNullInput() {
            // Given
            String input = null;

            // When
            boolean result = stringService.isPalindrome(input);

            // Then
            assertFalse(result);
        }

        @ParameterizedTest
        @ValueSource(strings = {"racecar", "level", "deed", "noon", "civic", "radar"})
        @DisplayName("Should identify various palindromes")
        void shouldIdentifyVariousPalindromes(String input) {
            // When
            boolean result = stringService.isPalindrome(input);

            // Then
            assertTrue(result);
        }

        @ParameterizedTest
        @ValueSource(strings = {"hello", "world", "test", "java", "programming"})
        @DisplayName("Should identify various non-palindromes")
        void shouldIdentifyVariousNonPalindromes(String input) {
            // When
            boolean result = stringService.isPalindrome(input);

            // Then
            assertFalse(result);
        }
    }

    @Nested
    @DisplayName("Count Vowels Tests")
    class CountVowelsTests {

        @Test
        @DisplayName("Should count vowels correctly")
        void shouldCountVowelsCorrectly() {
            // Given
            String input = "hello";

            // When
            int result = stringService.countVowels(input);

            // Then
            assertEquals(2, result);
        }

        @Test
        @DisplayName("Should handle string with no vowels")
        void shouldHandleStringWithNoVowels() {
            // Given
            String input = "rhythm";

            // When
            int result = stringService.countVowels(input);

            // Then
            assertEquals(0, result);
        }

        @Test
        @DisplayName("Should handle null input")
        void shouldHandleNullInput() {
            // Given
            String input = null;

            // When
            int result = stringService.countVowels(input);

            // Then
            assertEquals(0, result);
        }

        @ParameterizedTest
        @CsvSource({
            "hello, 2",
            "world, 1",
            "aeiou, 5",
            "rhythm, 0",
            "programming, 3",
            "TEST, 1"
        })
        @DisplayName("Should count vowels in various strings")
        void shouldCountVowelsInVariousStrings(String input, int expected) {
            // When
            int result = stringService.countVowels(input);

            // Then
            assertEquals(expected, result);
        }
    }

    @Nested
    @DisplayName("Title Case Tests")
    class TitleCaseTests {

        @Test
        @DisplayName("Should convert to title case correctly")
        void shouldConvertToTitleCaseCorrectly() {
            // Given
            String input = "hello world";

            // When
            String result = stringService.toTitleCase(input);

            // Then
            assertEquals("Hello World", result);
        }

        @Test
        @DisplayName("Should handle single word")
        void shouldHandleSingleWord() {
            // Given
            String input = "hello";

            // When
            String result = stringService.toTitleCase(input);

            // Then
            assertEquals("Hello", result);
        }

        @Test
        @DisplayName("Should handle empty string")
        void shouldHandleEmptyString() {
            // Given
            String input = "";

            // When
            String result = stringService.toTitleCase(input);

            // Then
            assertEquals("", result);
        }

        @Test
        @DisplayName("Should handle null input")
        void shouldHandleNullInput() {
            // Given
            String input = null;

            // When
            String result = stringService.toTitleCase(input);

            // Then
            assertNull(result);
        }

        @ParameterizedTest
        @CsvSource({
            "hello world, Hello World",
            "JAVA PROGRAMMING, Java Programming",
            "test case, Test Case",
            "single, Single",
            "multiple   spaces, Multiple   Spaces"
        })
        @DisplayName("Should convert various strings to title case")
        void shouldConvertVariousStringsToTitleCase(String input, String expected) {
            // When
            String result = stringService.toTitleCase(input);

            // Then
            assertEquals(expected, result);
        }
    }

    @Nested
    @DisplayName("Remove Duplicates Tests")
    class RemoveDuplicatesTests {

        @Test
        @DisplayName("Should remove duplicate characters correctly")
        void shouldRemoveDuplicateCharactersCorrectly() {
            // Given
            String input = "hello";

            // When
            String result = stringService.removeDuplicates(input);

            // Then
            assertEquals("helo", result);
        }

        @Test
        @DisplayName("Should handle string with no duplicates")
        void shouldHandleStringWithNoDuplicates() {
            // Given
            String input = "world";

            // When
            String result = stringService.removeDuplicates(input);

            // Then
            assertEquals("world", result);
        }

        @Test
        @DisplayName("Should handle null input")
        void shouldHandleNullInput() {
            // Given
            String input = null;

            // When
            String result = stringService.removeDuplicates(input);

            // Then
            assertNull(result);
        }

        @ParameterizedTest
        @CsvSource({
            "hello, helo",
            "world, world",
            "programming, progamin",
            "test, test",
            "aaaaa, a",
            "abcabc, abc"
        })
        @DisplayName("Should remove duplicates from various strings")
        void shouldRemoveDuplicatesFromVariousStrings(String input, String expected) {
            // When
            String result = stringService.removeDuplicates(input);

            // Then
            assertEquals(expected, result);
        }
    }

    @Nested
    @DisplayName("Find Longest Word Tests")
    class FindLongestWordTests {

        @Test
        @DisplayName("Should find longest word correctly")
        void shouldFindLongestWordCorrectly() {
            // Given
            String input = "hello world programming";

            // When
            String result = stringService.findLongestWord(input);

            // Then
            assertEquals("programming", result);
        }

        @Test
        @DisplayName("Should handle single word")
        void shouldHandleSingleWord() {
            // Given
            String input = "hello";

            // When
            String result = stringService.findLongestWord(input);

            // Then
            assertEquals("hello", result);
        }

        @Test
        @DisplayName("Should handle empty string")
        void shouldHandleEmptyString() {
            // Given
            String input = "";

            // When
            String result = stringService.findLongestWord(input);

            // Then
            assertEquals("", result);
        }

        @Test
        @DisplayName("Should handle null input")
        void shouldHandleNullInput() {
            // Given
            String input = null;

            // When
            String result = stringService.findLongestWord(input);

            // Then
            assertEquals("", result);
        }

        @ParameterizedTest
        @CsvSource({
            "hello world programming, programming",
            "test case example, example",
            "java python javascript, javascript",
            "a bb ccc, ccc",
            "short medium long, medium"
        })
        @DisplayName("Should find longest word in various strings")
        void shouldFindLongestWordInVariousStrings(String input, String expected) {
            // When
            String result = stringService.findLongestWord(input);

            // Then
            assertEquals(expected, result);
        }
    }

    @Nested
    @DisplayName("Count Words Tests")
    class CountWordsTests {

        @Test
        @DisplayName("Should count words correctly")
        void shouldCountWordsCorrectly() {
            // Given
            String input = "hello world programming";

            // When
            int result = stringService.countWords(input);

            // Then
            assertEquals(3, result);
        }

        @Test
        @DisplayName("Should handle single word")
        void shouldHandleSingleWord() {
            // Given
            String input = "hello";

            // When
            int result = stringService.countWords(input);

            // Then
            assertEquals(1, result);
        }

        @Test
        @DisplayName("Should handle empty string")
        void shouldHandleEmptyString() {
            // Given
            String input = "";

            // When
            int result = stringService.countWords(input);

            // Then
            assertEquals(0, result);
        }

        @Test
        @DisplayName("Should handle null input")
        void shouldHandleNullInput() {
            // Given
            String input = null;

            // When
            int result = stringService.countWords(input);

            // Then
            assertEquals(0, result);
        }
    }

    @Nested
    @DisplayName("Anagram Tests")
    class AnagramTests {

        @Test
        @DisplayName("Should identify anagrams correctly")
        void shouldIdentifyAnagramsCorrectly() {
            // Given
            String text1 = "listen";
            String text2 = "silent";

            // When
            boolean result = stringService.isAnagram(text1, text2);

            // Then
            assertTrue(result);
        }

        @Test
        @DisplayName("Should identify non-anagrams correctly")
        void shouldIdentifyNonAnagramsCorrectly() {
            // Given
            String text1 = "hello";
            String text2 = "world";

            // When
            boolean result = stringService.isAnagram(text1, text2);

            // Then
            assertFalse(result);
        }

        @Test
        @DisplayName("Should handle anagrams with spaces")
        void shouldHandleAnagramsWithSpaces() {
            // Given
            String text1 = "conversation";
            String text2 = "voices rant on";

            // When
            boolean result = stringService.isAnagram(text1, text2);

            // Then
            assertTrue(result);
        }

        @Test
        @DisplayName("Should handle null inputs")
        void shouldHandleNullInputs() {
            // Given
            String text1 = null;
            String text2 = "test";

            // When
            boolean result = stringService.isAnagram(text1, text2);

            // Then
            assertFalse(result);
        }

        @ParameterizedTest
        @CsvSource({
            "listen, silent, true",
            "hello, world, false",
            "debit card, bad credit, true",
            "funeral, real fun, true",
            "school master, the classroom, true"
        })
        @DisplayName("Should test various anagram combinations")
        void shouldTestVariousAnagramCombinations(String text1, String text2, boolean expected) {
            // When
            boolean result = stringService.isAnagram(text1, text2);

            // Then
            assertEquals(expected, result);
        }
    }
}
