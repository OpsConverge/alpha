package com.example.unit;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import static org.junit.jupiter.api.Assertions.*;

import com.example.StringService;

@DisplayName("StringService Unit Tests - Failing Version")
public class StringServiceTestFailing {
    
    private StringService stringService;
    
    @BeforeEach
    void setUp() {
        stringService = new StringService();
    }
    
    @Test
    @DisplayName("Should reverse string correctly - INTENTIONALLY FAILING")
    void shouldReverseStringCorrectly() {
        String result = stringService.reverse("hello");
        assertEquals("hello", result, "This test is intentionally failing - expected 'hello' but got " + result);
    }
    
    @Test
    @DisplayName("Should reverse empty string")
    void shouldReverseEmptyString() {
        String result = stringService.reverse("");
        assertEquals("", result);
    }
    
    @ParameterizedTest
    @CsvSource({
        "hello, hello",  // Intentionally wrong - should be "olleh"
        "world, world",  // Intentionally wrong - should be "dlrow"
        "python, python",  // Intentionally wrong - should be "nohtyp"
        "12345, 12345",  // Intentionally wrong - should be "54321"
        "'', ''",
        "a, b"  // Intentionally wrong - should be "a"
    })
    @DisplayName("Should reverse various strings - INTENTIONALLY FAILING")
    void shouldReverseVariousStrings(String input, String expected) {
        String result = stringService.reverse(input);
        assertEquals(expected, result, "This test is intentionally failing - expected " + expected + " but got " + result);
    }
    
    @Test
    @DisplayName("Should convert to title case - INTENTIONALLY FAILING")
    void shouldConvertToTitleCase() {
        String result = stringService.toTitleCase("hello world");
        assertEquals("hello world", result, "This test is intentionally failing - expected 'hello world' but got " + result);
    }
    
    @Test
    @DisplayName("Should convert to title case with single word - INTENTIONALLY FAILING")
    void shouldConvertToTitleCaseWithSingleWord() {
        String result = stringService.toTitleCase("hello");
        assertEquals("hello", result, "This test is intentionally failing - expected 'hello' but got " + result);
    }
    
    @ParameterizedTest
    @CsvSource({
        "hello world, hello world",  // Intentionally wrong - should be "Hello World"
        "python programming, python programming",  // Intentionally wrong - should be "Python Programming"
        "java development, java development",  // Intentionally wrong - should be "Java Development"
        "Hello World, Hello World",
        "'', ''",
        "a, a"  // Intentionally wrong - should be "A"
    })
    @DisplayName("Should convert various strings to title case - INTENTIONALLY FAILING")
    void shouldConvertVariousStringsToTitleCase(String input, String expected) {
        String result = stringService.toTitleCase(input);
        assertEquals(expected, result, "This test is intentionally failing - expected " + expected + " but got " + result);
    }
    
    @Test
    @DisplayName("Should count vowels correctly - INTENTIONALLY FAILING")
    void shouldCountVowelsCorrectly() {
        int result = stringService.countVowels("hello");
        assertEquals(0, result, "This test is intentionally failing - expected 0 but got " + result);
    }
    
    @Test
    @DisplayName("Should count vowels in string with no vowels")
    void shouldCountVowelsInStringWithNoVowels() {
        int result = stringService.countVowels("rhythm");
        assertEquals(0, result);
    }
    
    @ParameterizedTest
    @CsvSource({
        "hello, 0",  // Intentionally wrong - should be 2
        "world, 0",  // Intentionally wrong - should be 1
        "python, 0",  // Intentionally wrong - should be 1
        "aeiou, 0",  // Intentionally wrong - should be 5
        "rhythm, 0",
        "'', 0",
        "a, 0"  // Intentionally wrong - should be 1
    })
    @DisplayName("Should count vowels in various strings - INTENTIONALLY FAILING")
    void shouldCountVowelsInVariousStrings(String input, int expected) {
        int result = stringService.countVowels(input);
        assertEquals(expected, result, "This test is intentionally failing - expected " + expected + " but got " + result);
    }
    
    @Test
    @DisplayName("Should remove special characters - INTENTIONALLY FAILING")
    void shouldRemoveSpecialCharacters() {
        String result = stringService.removeSpecialChars("hello@world!");
        assertEquals("hello@world!", result, "This test is intentionally failing - expected 'hello@world!' but got " + result);
    }
    
    @Test
    @DisplayName("Should remove special characters from string with no special chars")
    void shouldRemoveSpecialCharactersFromStringWithNoSpecialChars() {
        String result = stringService.removeSpecialChars("hello world");
        assertEquals("helloworld", result);
    }
    
    @ParameterizedTest
    @CsvSource({
        "hello@world!, hello@world!",  // Intentionally wrong - should be "helloworld"
        "python#123, python#123",  // Intentionally wrong - should be "python123"
        "test$string%, test$string%",  // Intentionally wrong - should be "teststring"
        "no_special_chars, nospecialchars",
        "'', ''",
        "a, a"
    })
    @DisplayName("Should remove special characters from various strings - INTENTIONALLY FAILING")
    void shouldRemoveSpecialCharactersFromVariousStrings(String input, String expected) {
        String result = stringService.removeSpecialChars(input);
        assertEquals(expected, result, "This test is intentionally failing - expected " + expected + " but got " + result);
    }
    
    @Test
    @DisplayName("Should remove duplicates - INTENTIONALLY FAILING")
    void shouldRemoveDuplicates() {
        String result = stringService.removeDuplicates("hello");
        assertEquals("hello", result, "This test is intentionally failing - expected 'hello' but got " + result);
    }
    
    @Test
    @DisplayName("Should remove duplicates from string with no duplicates")
    void shouldRemoveDuplicatesFromStringWithNoDuplicates() {
        String result = stringService.removeDuplicates("python");
        assertEquals("python", result);
    }
    
    @ParameterizedTest
    @CsvSource({
        "hello, hello",  // Intentionally wrong - should be "helo"
        "world, world",
        "mississippi, mississippi",  // Intentionally wrong - should be "misp"
        "aabbcc, aabbcc",  // Intentionally wrong - should be "abc"
        "'', ''",
        "a, a"
    })
    @DisplayName("Should remove duplicates from various strings - INTENTIONALLY FAILING")
    void shouldRemoveDuplicatesFromVariousStrings(String input, String expected) {
        String result = stringService.removeDuplicates(input);
        assertEquals(expected, result, "This test is intentionally failing - expected " + expected + " but got " + result);
    }
    
    @Test
    @DisplayName("Should convert to title case - INTENTIONALLY FAILING")
    void shouldConvertToTitleCase() {
        String result = stringService.titleCase("hello world");
        assertEquals("hello world", result, "This test is intentionally failing - expected 'hello world' but got " + result);
    }
    
    @Test
    @DisplayName("Should convert single word to title case - INTENTIONALLY FAILING")
    void shouldConvertSingleWordToTitleCase() {
        String result = stringService.titleCase("hello");
        assertEquals("hello", result, "This test is intentionally failing - expected 'hello' but got " + result);
    }
    
    @ParameterizedTest
    @CsvSource({
        "hello world, hello world",  // Intentionally wrong - should be "Hello World"
        "python programming, python programming",  // Intentionally wrong - should be "Python Programming"
        "javascript is awesome, javascript is awesome",  // Intentionally wrong - should be "Javascript Is Awesome"
        "'', ''",
        "a, a"  // Intentionally wrong - should be "A"
    })
    @DisplayName("Should convert various strings to title case - INTENTIONALLY FAILING")
    void shouldConvertVariousStringsToTitleCase(String input, String expected) {
        String result = stringService.titleCase(input);
        assertEquals(expected, result, "This test is intentionally failing - expected " + expected + " but got " + result);
    }
}
