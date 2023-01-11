package com.hello.spring;

import com.hello.spring.discount.FixDiscountPolicy;
import com.hello.spring.member.MemberService;
import com.hello.spring.member.MemberServiceImpl;
import com.hello.spring.member.MemoryMemberRepository;
import com.hello.spring.order.OrderService;
import com.hello.spring.order.OrderServiceImpl;

public class AppConfig {
    public MemberService memberService() {
        return new MemberServiceImpl(new MemoryMemberRepository());
    }

    public OrderService orderService() {
        return new OrderServiceImpl(new MemoryMemberRepository(), new FixDiscountPolicy());
    }
}
