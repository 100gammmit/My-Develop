스프링 스케줄러(@EnableScheduling, @Scheduled)
==================

## Spring Scheduler
- 스프링에서 제공하는 특정 주기로 Task(매서드) 자동 실행을 가능하게 하는 스케줄링 기능
- ### 사용법
  - 매서드에 **@Scheduled()** 어노테이션을 추가하고, 어노테이션의 파라미터로 주기 설정
  - 기본적으로 **@Component**를 사용하여 **스프링 빈으로 등록된 클래스의 매서드**만 사용 가능
  - **해당 매서드를 가진 클래스** or **@SpringBootApplication**을 가진 스프링 프로젝트 실행 클래스에 **@EnableScheduling** 어노테이션 추가하여 Scheduler 활성화
- ### 주의점
  - 스케줄링을 사용하는 매서드는 파라미터를 사용할수 없으며, void타입이어야 한다.
  - 스케줄러로 인한 매서드 실행은 하나의 스레드안에서 실행됨
  - 여러 작업을 동시에 실행할 시 스레드를 추가로 부여하는 등의 추가 설정 필요
</br></br></br>
## @Scheduled() 파라미터
- cron
  - cron 표현식을 이용하여 설정한 시간에 작업 자동실행
  - cron 표현식
    - 유닉스/리눅스 기반의 스케줄러에서 사용되는 스케줄링 파라미터 표현식
    - ("초(0~59) 분(0~59) 시(0~23) 일(1~31) 월(1~12) 요일(0~6 or SUN ~ SAT)")
  - (cron="00 00 19 * * *") : 매일 오후 7시에 작업 실행
- fixedDelay
  - 특정 주기로 작업 실행
  - 작업이 끝난 시점에서 설정한 시간 뒤에 실행
  - (fixedDelay = 1000) : 1초마다 해당 매서드 실행
- fixedRate
  - 특정 주기로 작업 실행
  - fixedDelay와 다르게 작업이 시작한 시점에서 주기가 시작됨
- initialDelay
  - 프로젝트 빌드 후 지정한 시간이 지난 뒤에 최초 매서드 실행
  - 최초로 실행된 후 fixed.. 주기별로 매서드 실행
  - (initialDelay = 1000, fixedRate = 5000) : 빌드 후 1초뒤에 실행, 그뒤로 5초마다 재실행


## SourceCode
``` java 
@Scheduled(cron = "00 53 18 * * *")
    public void SchedulingTest() throws InterruptedException {
        System.out.println("\n");
        System.out.println("=======================================");
        System.out.println("[ArticleService] : [UpdateArticle]");
        System.out.println("[Started] : " + getNowDateTime24());
        System.out.println("=======================================");
        System.out.println("\n");

        crawlAllArticleWithCategory();

        System.out.println("\n");
        System.out.println("=======================================");
        System.out.println("[ArticleService] : [UpdateArticle]");
        System.out.println("[Ended] : " + getNowDateTime24());
        System.out.println("=======================================");
        System.out.println("\n");
    }
```

getNowDateTime24() 
- String타입으로 현재 시간을 "yyyy.MM.dd kk:mm:ss E요일" 형식으로 포멧하여 반환하는 매서드

crawlAllArticleWithCategory() 
- 실행할 크롤링 Task
  
</br>

## 실행 결과
```
=======================================
[ArticleService] : [UpdateArticle]
[Started] : 2023.03.28 18:53:00 화요일
=======================================

Hibernate:
    select
        .........
        ........
        ...........
        .........
        
=======================================
[ArticleService] : [UpdateArticle]
[Ended] : 2023.03.28 18:54:24 화요일
=======================================
```