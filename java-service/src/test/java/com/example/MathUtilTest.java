package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MathUtilTest {

    @Test
    void addition_passes() {
        assertEquals(4, 2 + 2); // PASS
    }

    @Test
    void subtraction_fails_intentionally() {
        assertEquals(0, 2 - 1); // FAIL on purpose (2-1 == 1)
    }
}
