# 스프링 3일차

## SpringBoot와 DB연동

### 커넥션 풀(Connection Pool)
* Pool 속에 DB와의 연결을 만들어놓은 뒤 DB에 접근시 Pool에 남아있는 연결중 하나를 받아와서 사용한뒤 반환하는 기법
* 다수의 사용자가 DB에 접근할 때마다 연결을 만들지 않고 미리 연결을 만들어 사용자가 요청시 만들어놓은 연결을 주는 방식으로 효과적인 DB연결및 자원사용 가능

### Mapper란
sql문을 정의하고 그 결과를 정의해놓은 모델에 매핑시키는 방식에서 sql문(xml)을 메소드(java)로 매핑시켜주는 것을 의미한다
