package me.hsw0905;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertNotNull;

class CalculatorTest {
    @Test
    void create() {
        Calculator calculator = new Calculator();
        assertNotNull(calculator);
    }

}