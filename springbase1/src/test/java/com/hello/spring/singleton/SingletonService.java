package com.hello.spring.singleton;

public class SingletonService {
    private static final SingletonService instance = new SingletonService();    // 멤버로써 자신 클래스를 정적 상수로 선언

    public static SingletonService getInstance() {
        return instance;
    }

    private SingletonService() {

    }

    public void logic() {
        System.out.println("싱글톤 객체 로직 호출");
    }
}
