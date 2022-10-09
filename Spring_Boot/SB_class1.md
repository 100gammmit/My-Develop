인프런 스프링입문 1
==============
## maven과 gradle
라이브러리를 가져오고 빌드 라이프사이클을 관리하는 툴을 말함 과거엔 maven을 현재는 gradle을 보통 주로 사용하는편
</br></br>
## 의존성 라이브러리
gradle은 의존관계가 있는 라이브러리를 함께 다운로드하여 라이브러리간에 의존관계를 신경쓰지 않게 해준다.
### spring-boot-starter-web
* sorubg-boot-start-tomcat: 톰캣 웹서버
* spring-webmvc: 스프링 웹 MVC
### spring-boot-starter(공통): 스프링 부트 + 스프링 코어 + 로깅
* spring-boot: 스프링 핵심 기능
    * spring-core
* spring-boot-starter-logging: 디버깅에 쓰이는 로그를 출력하는 라이브러리
    * logback, slf4j: 현재 표준에 가까운 로깅 인터페이스 라이브러리조합
### thymeleaf 템플릿엔진
</br></br>

## 필요한 기능 찾기
spring.io 페이지 -> Reference Document -> ctrl+f
</br></br>

## Controller 동적 페이지 예제
### HelloController.java
```java
package hello.spring.controller;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.ui.Model;

@Controller
public class HelloController {

    @GetMapping("hello")
    public String hello(Model model){
        model.addAttribute( "data", "hello!!");
        return "hello";
    }
}
```
### hello.html
```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Hello</title>
</head>
<body>
<p th:text="'안녕하세요. ' + ${data}" >안녕하세요. 손님</p>
</body>
</html>
```
## Spring Model 객체
JSP Servlet에서 웹 어플리케이션을 만들 땐 보통 **request**나 **session** 내장객체에 정보를 담아 넘겨주었지만 spring에서는 파라미터로 선언만 해주면 **Model**이라는 객체를 알아서 생성하여 정보를 동적으로 다루는 것을 편리하게 해줌

</br>

Controller에서 리턴 값으로 문자를 반환하면 **viewResolver**가 화면을 찾아서 처리한다.
* 스프링 부트 템플릿엔진 기본 **viewName**매핑
    * `resources:templates/` +{**ViewName**}+`.html`

**웹 브라우저** -> **내장 톰켓 서버**에 localhost:8080hello요청</br>
-> **helloController**에서 ViewName(return "hello";)매핑 및 model(data:"hello!!")생성 </br>
-> **ViewResolver** thymeleaf 템플릿 엔진 처리를 통하여 templates/hello.html로 변환 </br>
-> **웹 브라우저** 출력
</br></br>

## build and run
스프링부트 프로젝트에서 터미널 실행</br>
-> ./gradlew build커맨드로 build파일 생성</br>
-> cd build/libs커맨드로 build/libs파일로 이동</br>
-> java -'jar파일 이름'커맨드로 프로젝트 실행