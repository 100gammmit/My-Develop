package com.hello.spring.discount;

import com.hello.spring.member.Grade;
import com.hello.spring.member.Member;

/**
 * 할인 정책의 구현스
 */
public class FixDiscountPolicy implements DiscountPolicy{

    private int discountFixAmount = 1000; //1000원 할인
    @Override
    public int discount(Member member, int price) {
        if (member.getGrade() == Grade.VIP){
            return discountFixAmount;
        }
        else {
            return 0;
        }
    }
}
