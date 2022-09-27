인프런 스프링입문 2
=============
## 스프링에서의 정적컨텐츠
1. 내장 톰켓 서버에서 웹브라우저로부터 요청을 받음
2. 톰켓 서버에서 요청과 관련된 컨트롤러가 있는지 확인
3. 없으면 resources/static경로에 요청에 대한 파일이 있는지 확인
4. 파일이 확인될 시 웹브라우저에 정보 제공
   
## MVC와 템플릿 엔진
intellij 깨알팁 
 - 'command+p' = parameter 정보
 - 'command+n' = 클래스 자주 사용되는 매서드 간편 정의 ex) Getter, Setter
 - 'shift+f6' = 변수 이름 한꺼번에 변경
 - 'command+option+v' = optional타입 객체 간편 정의
 - 'command+option+/' = 간편 주석처리
 - 'ctrl+r' = 이전 실행한거 재실행
 - 'ctrl+t' = 리팩토링과 관련된 여러 기능 실행 여부 확인(코드 매서드화 등)

## HelloController.java
```java
package hello.spring.controller;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class HelloController {

    @GetMapping("hello")
    public String hello(Model model){
        model.addAttribute( "data", "hello!!");
        return "hello";
    }

    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam(value = "name", required = false) String name, Model model) {
        model.addAttribute("name", name);
        return "hello-template";
    }
}

```

## hello-template.html
```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<p th:text="'hello ' + ${name}">hello empty</p>
</body>
</html>
```

## 처리과정
1. 웹브라우저에서 내장톰켓서버에 localhost:8080/hello-mvc 요청
2. 관련 컨트롤러 확인 과정에서 helloController.java 안에서 'hello-mvc'매핑 되어있는 것을 확인 및 해당 매서드 호출
3. model의 파라미터 값을 확인하고 'hello-template' 를 viewResolver에 처리 요청
4.  viewResolver안에서 thymeleaf 템플릿 엔진이 랜더링 후 html파일 변환
5.  변환된 파일 웹브라우저에 출력

 ## API

### hello-string
```java
@GetMapping("hello-string")
    @ResponseBody
    public String helloString(@RequestParam("name") String name){
        return "hello " + name;
    }
```

### hello-api
```java
@GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name){
        Hello hello = new Hello();
        hello.setName(name);
        return hello;
    }

    static class Hello {
        private String name;

        public String getName() {
            return name;
        };

        public void setName(String name) {
            this.name = name;
        }
    }
```

출력: {"name":name}
- 클래스 return 방식의 매서드 사용 시 JSON타입으로 클래스에 대한 정보가 출력되며, 이를 API방식 통신이라함

### @ResponseBody 어노테이션
- http의 body부분에 문자 내용을 직접 반환하는 기능
- ViewResolver대신에 HttpMessageConverter가 동작
- 클라이언트의 HTTP Accept 헤더와 서버의 컨트롤러 반환 타입 정보 둘을 조합해서 JsonController와 StringController중에 선택됨 


## 일반적인 웹 어플 계층 구조
- 컨트롤러: 웹 MVC의 컨트롤러 역할
- 서비스: 핵심 비지니스 로직 구현
- 레퍼지토리: DB에 접근 고메인 객체를 DB에 저장하고 관리
- 도메인: 주로 DB에 저장하고 관리되는 비지니스 도메인 객체


## 테스트코드 설계 시 주의점
- 매서드간의 의존 관계가 없도록 해야함
- 스프링에서 한번에 여러 매서드를 테스트 할 시 순서를 알아서 정함
- 따라서 공용 데이터가 될 수도 있는 부분은 clear매서드를 통해서(@AfterEach 사용) 의존될 가능성을 지워줘야 함
- 테스트 코드에서 생성한 객체와 메인에서 생성하는 객체는 별개로 존재하기 때문에 상호 객체간의 의존관계를 확실하게 고려해야함(@BeforeEach로 매서드 테스트 전에 객체 관계를 정리할 것)


### ifPresent
- Optional 객체가 값을 가지고 있으면 실행하고, 값이 없으면 skip하는 매서드