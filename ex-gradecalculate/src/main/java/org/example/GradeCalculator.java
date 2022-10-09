package org.example;

import java.util.List;

public class GradeCalculator {
    private final Courses courses;

    public GradeCalculator(List<Course> courses) {
        this.courses = new Courses(courses);
    }

    public double caculateGrade() {
        // (학점수*교과목 평점)의 합계
        double multipliedCreditAndCourseGrade = courses.multiplyCreditAndCourseGrade();
        // 수강신청 총학점
        int totalCompletedCredit = courses.calculatetotalcompletedCredit();

        return multipliedCreditAndCourseGrade / totalCompletedCredit;
    }
}
