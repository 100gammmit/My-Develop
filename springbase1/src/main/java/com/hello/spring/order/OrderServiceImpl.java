package com.hello.spring.order;

import com.hello.spring.discount.DiscountPolicy;
import com.hello.spring.discount.FixDiscountPolicy;
import com.hello.spring.member.Member;
import com.hello.spring.member.MemberRepository;
import com.hello.spring.member.MemoryMemberRepository;

public class OrderServiceImpl implements OrderService {

    private MemberRepository memberRepository = new MemoryMemberRepository();  // 주문한 멤버를 찾기 위하여 선언
    private DiscountPolicy discountPolicy = new FixDiscountPolicy();  // 해당 멤버의 할인 정책을 확인하기 위하여 선언

    /**
     * 주문 생성 함수
     * @return 주문한 멤버의 정보를 찾아 그에 따른 할인정책을 찾고 이를 적용하여 최종 주문을 생성하여 반환
     */
    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member = memberRepository.findById(memberId);
        int discountPrice = discountPolicy.discount(member, itemPrice);

        return new Order(memberId, itemName, itemPrice, discountPrice);
    }
}
