package org.example;

import com.zaxxer.hikari.HikariDataSource;

import javax.sql.DataSource;

public class ConnectionManager {
    public static DataSource getDataSource() {
        HikariDataSource hikariDataSource = new HikariDataSource();
        hikariDataSource.setDriverClassName("org.h2.Driver");
        hikariDataSource.setJdbcUrl("jdbc:h2:tcp://localhost/~/test");
        hikariDataSource.setUsername("sa");
        hikariDataSource.setPassword("");
        return hikariDataSource;

    }
}
