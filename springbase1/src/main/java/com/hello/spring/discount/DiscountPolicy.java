package com.hello.spring.discount;

import com.hello.spring.member.Member;

/**
 * 할인 정책의 역할 인터페이스
 */
public interface DiscountPolicy {
    /**
     * @param member
     * @param price
     * @return 할인 대상 금액
     */
    int discount(Member member, int price);
}
