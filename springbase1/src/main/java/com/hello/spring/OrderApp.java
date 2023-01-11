package com.hello.spring;

import com.hello.spring.member.Grade;
import com.hello.spring.member.Member;
import com.hello.spring.member.MemberService;
import com.hello.spring.member.MemberServiceImpl;
import com.hello.spring.order.Order;
import com.hello.spring.order.OrderService;
import com.hello.spring.order.OrderServiceImpl;

public class OrderApp {
    public static void main(String[] args) {
        AppConfig appConfig = new AppConfig();
        MemberService memberService = appConfig.memberService();
        //MemberService memberService = new MemberServiceImpl();

        OrderService orderService = appConfig.orderService();
        //OrderService orderService = new OrderServiceImpl();

        Long memberId = 1L;
        Member member = new Member(memberId, "MemberA", Grade.VIP);
        memberService.join(member);

        Order order = orderService.createOrder(memberId, "itemA", 10000);

        System.out.println("order = " + order.toString());
    }
}
