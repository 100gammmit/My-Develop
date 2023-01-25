package com.hello.spring.beanfind;

import com.hello.spring.AppConfig;
import com.hello.spring.member.MemberService;
import com.hello.spring.member.MemberServiceImpl;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.NoSuchBeanDefinitionException;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

public class ApplicationContextBasicFindTest {
     AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

     @Test
     @DisplayName("빈 이름으로 조회")
     void findBeanByName() {
          MemberService memberService = ac.getBean("memberService", MemberService.class);
          //현재 AppConfig안의 memberService매서드가 MemberServiceImpl을 리턴하고있음
          assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
     }

     @Test
     @DisplayName("이름없이 타입으로 조회")
     void findBeanByType() {
          MemberService memberService = ac.getBean(MemberService.class);

          assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
     }

     @Test
     @DisplayName("구체 타입으로 조회")
     void findBeanByName2() {
          MemberService memberService = ac.getBean("memberService", MemberServiceImpl.class);
          // MemberService 인터페이스의 구체 타입인 MemberServiceImpl을 반환하는 타입의 빈을 조회

          assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
     }

     @Test
     @DisplayName("빈 이름으로 조회X")
     void findBeanByNameX() {
          // ac.getBean("xxxxx", MemberService.class);
          assertThrows(NoSuchBeanDefinitionException.class,
                  () -> ac.getBean("xxxxx", MemberService.class));

     }
}
