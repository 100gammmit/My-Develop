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

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Index</title>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<script>
		$.ajax({
			type: "GET",
			url: "/testValue",
			success: (data) => {
				console.log(data);
				$('#contents').html(data);
			}
		});
	</script>
</head>
<body>
	<h1>Hello World!</h1>
	<div id="contents">
	</div>
</body>
</html>
```
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

## Rest
“Representational State Transfer” 의 약자로, 자원의 이름으로 구분하고 자원의 상태(정보)를 전달하는 모든 것을 의미한다.</br>
즉 자원(resource)의 표현(representation)에 의한 상태를 전달

### 자원의 표현
* 자원 : 소프트웨어가 관리하는 모든 것 ex)문서 그림 데이터 등
* 자원의 표현 : 자원을 표현하기 위한 이름 ex) DB의 학생 정보가 자원이라면 "Student"를 자원의 표현으로 지정
### 상태 전달
* 데이터가 요청되어지는 시점에서 자원의 상태(정보)를 전달한다.
* 일반적으로 JSON혹은 XML을 통해 정보를 주고받는다.

## Rest의 구체적인 의미
HTTP URI를 통해 자원을 명시하고, HTTP Method(GET, POST, PUT, DELETE)를 통해 해당 자원의 CRUD기능을 적용하도록 하는 것이다.
* Rest는 자원 기반의 설계 구조의 중심에 resource가 있고, Http method를 통하여 해당 resource를 처리하는 아키텍쳐를 의미한다.
* 웹 사이트의 이미지, 텍스트, DB등 모든 자원에 대한 특별한 ID인 HTTP URI를 부여한다.

## URI(통합 자원 식별자)
자원을 구별하기 위해 사용하는 유일한 식별자
### URI의 종류
* URL
  * 자원의 위치로 자원을 식별함
  * 보통 URI로 URL을 사용함
* URN
  * 자원에 이름을 붙여 식별함 
<hr/>

## thymeleaf를 통하여 mvc의 View 설정
### -thymeleafTest.html
```html
<!DOCTYPE html>
<html lang="ko" xmlns:th="http://www.thymeleaf.org">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Hello thymeleaf</title>
</head>
<body>
	<h1>Hello thymeleaf</h1>
	<h2>name = <span th:text="${testMpodel.name}"></span></h2>
	<h2>id = <span th:text="${testMpodel.id}"></span></h2>
</body>
</html>
```

### -application.properties
```
spring.thymeleaf.prefix=classpath:/templates/
spring.thymeleaf.suffix=.html

spring.thymeleaf.cache=false
spring.thymeleaf.check-template-location=true
```
* thymeleaf를 사용하다 수정사항이 생기면 새로고침만으로 반영시키기 위해 cache를 false로 설정

### -TestVo.java
```java
package com.example.demo.vo;

public class TestVo{
	private Long mbrNo;
	private String id;
	private String name;
	
	public TestVo() {	
	}
	

	public TestVo(String id, String name) {
		this.id=id;
		this.name=name;
	}
	
	public Long getMbrNo() {
		return mbrNo;
	}
	
	public void setMbrNo(Long mbrNo) {
		this.mbrNo = mbrNo;
	}
	
	public String getId() {
		return id;
	}
	
	public void setId(String id) {
		this.id = id;
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name=name;
	}
}
```
### -TestController.java
```java
package com.example.demo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import com.example.demo.vo.TestVo;

@Controller
public class TestController{
	@RequestMapping("thymeleafTest")
	public String thymeleafTest(Model model) {
		TestVo testModel = new TestVo("minminhahaha", "201704045");
		model.addAttribute("testModel", testModel);
		return "thymeleafTest";
	}
}
```
localhost:8080/thmeleafTest로 접속해야 가능</br>
그냥 localhost:8080으로 접속 시 whitelabel