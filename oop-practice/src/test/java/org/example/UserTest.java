package org.example;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class UserTest {

    @DisplayName("패스워드를 초기화한다.")
    @Test
    void passwordTest() {
        // Given
        User user = new User();

        // When
        user.initPassword(new CorrectFixedPasswordGenerator());

        // Then
        assertThat(user.getPassword()).isNotNull();
    }

    @DisplayName("패스워드가 요구사항에 부합하지 않아 초기화되지 않는다.")
    @Test
    void passwordTest2() {
        // Given
        User user = new User();

        // When
        user.initPassword(new WrongFixedPasswordGenerator());

        // Then
        assertThat(user.getPassword()).isNull();
    }
}