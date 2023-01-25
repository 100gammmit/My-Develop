package com.hello.spring;

import com.hello.spring.member.Grade;
import com.hello.spring.member.Member;
import com.hello.spring.member.MemberService;
import com.hello.spring.member.MemberServiceImpl;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class MemberApp {
    public static void main(String[] args) {
        // AppConfig appConfig = new AppConfig();
        // MemberService memberService = appConfig.memberService();

        ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class);
        // @Configuration 어노테이션을 적용한 클래스에 대하여 @Bean 이 적용된 객체들을 스프링 컨테이너에 등록함
        MemberService memberService = applicationContext.getBean("memberService", MemberService.class);
        // AppConfig 안에서 MemberService 타입의 memberService 함수를 불러들여옴
        Member member = new Member(1L, "memberA", Grade.VIP);
        memberService.join(member);

        Member findMember = memberService.findMember(1L);
        System.out.println("new member = " + member.getName());
        System.out.println("findMember = " + findMember.getName());
    }
}
