package me.hsw0905;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class CalculatorTest {
    private static Calculator cal;

    @BeforeAll
    static void setUp() {
        cal = new Calculator();
    }

    @Test
    void add() {
        assertEquals(9, cal.add(6, 3));
    }

    @Test
    void subtract() {
        assertEquals(5, cal.subtract(9, 4));
    }

    @Test
    void multiply() {
        assertEquals(10, cal.multiply(2, 5));
    }

    @Test
    void divide() {
        assertEquals(2, cal.divide(4, 2));
    }
}