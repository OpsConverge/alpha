package com.example;

import org.springframework.stereotype.Service;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class StringService {
    
    /**
     * Reverses a string
     */
    public String reverse(String input) {
        if (input == null) {
            return null;
        }
        return new StringBuilder(input).reverse().toString();
    }
    
    /**
     * Checks if a string is palindrome
     */
    public boolean isPalindrome(String input) {
        if (input == null) {
            return false;
        }
        String cleaned = input.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        return cleaned.equals(reverse(cleaned));
    }
    
    /**
     * Counts vowels in a string
     */
    public int countVowels(String input) {
        if (input == null) {
            return 0;
        }
        return (int) input.toLowerCase().chars()
                .mapToObj(ch -> (char) ch)
                .filter(ch -> "aeiou".indexOf(ch) != -1)
                .count();
    }
    
    /**
     * Converts string to title case
     */
    public String toTitleCase(String input) {
        if (input == null || input.trim().isEmpty()) {
            return input;
        }
        
        String[] words = input.toLowerCase().split("\\s+");
        List<String> titleCaseWords = Arrays.stream(words)
                .map(word -> word.isEmpty() ? word : 
                    Character.toUpperCase(word.charAt(0)) + word.substring(1))
                .collect(Collectors.toList());
        
        return String.join(" ", titleCaseWords);
    }
    
    /**
     * Removes duplicate characters from string
     */
    public String removeDuplicates(String input) {
        if (input == null) {
            return null;
        }
        return input.chars()
                .distinct()
                .mapToObj(ch -> String.valueOf((char) ch))
                .collect(Collectors.joining());
    }
    
    /**
     * Finds the longest word in a string
     */
    public String findLongestWord(String input) {
        if (input == null || input.trim().isEmpty()) {
            return "";
        }
        
        return Arrays.stream(input.split("\\s+"))
                .max((a, b) -> Integer.compare(a.length(), b.length()))
                .orElse("");
    }
    
    /**
     * Counts words in a string
     */
    public int countWords(String input) {
        if (input == null || input.trim().isEmpty()) {
            return 0;
        }
        return input.trim().split("\\s+").length;
    }
    
    /**
     * Checks if two strings are anagrams
     */
    public boolean isAnagram(String text1, String text2) {
        if (text1 == null || text2 == null) {
            return false;
        }
        String cleaned1 = text1.toLowerCase().replaceAll("[^a-zA-Z]", "");
        String cleaned2 = text2.toLowerCase().replaceAll("[^a-zA-Z]", "");
        
        if (cleaned1.length() != cleaned2.length()) {
            return false;
        }
        
        char[] chars1 = cleaned1.toCharArray();
        char[] chars2 = cleaned2.toCharArray();
        Arrays.sort(chars1);
        Arrays.sort(chars2);
        
        return Arrays.equals(chars1, chars2);
    }
}
