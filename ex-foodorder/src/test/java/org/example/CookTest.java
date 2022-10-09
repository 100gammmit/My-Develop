package org.example;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThatCode;

public class CookTest {
    @DisplayName("요리를 생성한다.")
    @Test
    void name() {
        assertThatCode(() -> new Cook("만두", 5000))
                .doesNotThrowAnyException();        //요리를 생성하면 어떠한 예외도 발생시키지 않는다.
    }
}
