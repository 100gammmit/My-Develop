package org.example.annotation;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target({ElementType.TYPE})         //클래스, 인터페이스, 어노테이션 타입, enum 선언에 사용될 수 있는 것이 TYPE
@Retention(RetentionPolicy.RUNTIME) //유지 기간 runtime도중으로 설정
public @interface Controller {
}
