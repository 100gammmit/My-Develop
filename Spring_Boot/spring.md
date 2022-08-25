# 스프링2일차
## 어노테이션
 어노테이션은 사전적으론 주석이란 의미이지만 자바에선 특별한 기능을 수행하도록 하는 기술이다. 
### 어노테이션의 용도
* 컴파일러에게 코드 작성 문법 에러를 체크하도록 정보 제공
* 소프트웨어 툴이 빌드나 배치 시 코드를 자동으로 생성할 수 있도록 정보 제공
* 실행시 특정 기능을 실행하도록 정보 제공
<hr/>

## @RestController 생성
spring 4.0이상은 @Controller와 @ResponseBody어노테이션을 따로 설정하지 않고 @RestController를 통하여 자동으로 @ResponseBody를 Controller에서 활성화시킬 수 있다.
### 이전코드
```java
package com.example.demo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class TestController{
	@RequestMapping(value="/home")
	public String home() {
		return "index.html";
	}
	
	@ResponseBody
	@RequestMapping("/valueTest")
	public String valueTest() {
		String value = "테스트 string";
		return value;
	}
}
```
### @RestController 사용 코드
```java
package com.example.demo.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController{
	@RequestMapping(value="/testValue", method = RequestMethod.GET)
	public String getTestValue() {
		String TestValue = "RestController test";
		return TestValue;
	}
	
}
```
### @RestController 선언문
```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Controller
@ResponseBody
public @interface RestController {

	@AliasFor(annotation = Controller.class)
	String value() default "";

}
```
-> 메타어노테이션으로 @ResponseBody와 @Controller가 지정되어 있는 것을 확인 가능
<hr/>
