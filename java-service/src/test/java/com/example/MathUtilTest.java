package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MathUtilTest {
    
    @Test
    void addition_works() {
        assertEquals(5, MathUtil.add(2, 3));
        assertEquals(0, MathUtil.add(-1, 1));
    }
    
    @Test
    void subtraction_works() {
        assertEquals(2, MathUtil.subtract(5, 3));
        assertEquals(-2, MathUtil.subtract(3, 5));
    }
    
    @Test
    void subtraction_fails_intentionally() {
        // This test will fail intentionally for testing purposes
        assertEquals(0, MathUtil.subtract(2, 1)); // Expected: 0, Actual: 1
    }
    
    @Test
    void multiplication_works() {
        assertEquals(6, MathUtil.multiply(2, 3));
        assertEquals(0, MathUtil.multiply(0, 5));
    }
    
    @Test
    void multiplication_fails_intentionally() {
        // This test will fail intentionally for testing purposes  
        assertEquals(10, MathUtil.multiply(2, 3)); // Expected: 10, Actual: 6
    }
    
    @Test
    void division_works() {
        assertEquals(2.5, MathUtil.divide(5, 2), 0.001);
        assertEquals(-2.0, MathUtil.divide(-4, 2), 0.001);
    }
    
    @Test
    void division_by_zero_throws_exception() {
        assertThrows(IllegalArgumentException.class, () -> {
            MathUtil.divide(5, 0);
        });
    }
}