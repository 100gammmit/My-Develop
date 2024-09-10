package com.hello.spring;

import com.hello.spring.discount.DiscountPolicy;
import com.hello.spring.discount.FixDiscountPolicy;
import com.hello.spring.discount.RateDiscountPolicy;
import com.hello.spring.member.MemberRepository;
import com.hello.spring.member.MemberService;
import com.hello.spring.member.MemberServiceImpl;
import com.hello.spring.member.MemoryMemberRepository;
import com.hello.spring.order.OrderService;
import com.hello.spring.order.OrderServiceImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;


@Configuration  //프로젝트 설정을 관리하는 클래스임을 스프링에 알리는 어노테이션
public class AppConfig {
    @Bean
    public MemberService memberService() {
        System.out.println("call AppConfig.memberService");
        return new MemberServiceImpl(memberRepository());
    }
    @Bean
    public MemberRepository memberRepository() {
        System.out.println("call AppConfig.memberRepository");
        return new MemoryMemberRepository();    // 어떠한 멤버 데이터 관리 정책을 사용할 지 관리하는 코드
    }
    @Bean
    public OrderService orderService() {
        System.out.println("call AppConfig.orderService");
        return new OrderServiceImpl(memberRepository(), discountPolicy());
    }
    @Bean
    public DiscountPolicy discountPolicy() {
        return new RateDiscountPolicy();     // 어떠한 할인 정책을 적용할지 관리하는 코드
    }
}
