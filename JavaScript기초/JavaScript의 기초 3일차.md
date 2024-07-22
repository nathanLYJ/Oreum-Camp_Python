# JavaScript의 기초 3일차

## 목차

1. [반복문(for-in)](#반복문for-in)
2. [반복문(for-of)](#반복문for-of)
3. [Map](#map)

## 반복문(for-in)

* for-in 특징  
  1. for in 는  객체의 `Key 혹은 index 값` 기준으로 정열해줌
  2. 모든 브라우저에 지원

    ```js
    for ( 변수 선언 in 객체 ) {
      반복할 코드;
    } 
    ```

## 반복문(for-of)

* for-of 특징  
  1. for of 는 객체의 `value` 값만 정열해줌. `배열`, `문자열`, `Map`, `Set` 등 순회가능한 객체만 가능.
  2. 2014년 6월이후 업데이트 된 브라우저만 지원, internet Explorer 지원 불가.

    ```js
    for ( 변수 선언 of 객체 ) {
      반복할 코드;
    } 
    ```
  [사용 가능 분법 조회](https://caniuse.com/)

## Map()

* Map() 특징
  1. 키와 값 가지는 객체 자료형의 한종류이지만, keys와 values를 바로 사용할 수 없습니다.
  2. 메서드가 제한적.
  3. for-of 순회시, key와 value 함께 순회

* 값 셋팅 방법

  ```js
  let 변수명 = new Map(); // Map 선언

  변수명.set('key', 값); // 값 설정

  console.log(변수명.get('key')); // Map 값 호출
  
  변수명.delete('key'); // Map 값 삭제

  변수명.size // 사이즈 확인

  for (const 변수명4 of 변수명) {
  console.log('변수명을 순회하고 있습니다. ${변수명2}');
  } // for of 순회, key와 값 함께 출력

  for (const [key, val] of 변수명) {
  console.log(`${key}:${val}`);
  } // 디스트럭션 예시

  console.log(변수명.keys());
  console.log(변수명.values()); 
  
  let 변수명2 = new Map(Object.entries({변수명:값})) // Object 자료형을 맵으로 반환하기

  const 변수명3 = Object.fromEntries(변수명2); // Map을 Object로 변환

  ```

* Map 과 Object의 차이
  1. Object의 키는 문자열 타입으로만 지정 .가능, Map의 키는 모든 값을 가질 수 있습니다.
  2. Object는 수동으로 크기 알아낼 수 있다, Map는 size를 통해서 쉽게 얻을 수 있다.
  3. Map은 데이터를 추가, 삭제, 수정하기 쉽다.
  선언이 불편하다.
  
## Set()

* Set()의 특징
  1. Set은 값의 중복을 허용하지않는 객체자료형.
  2. 주로 집합에 자주 사용합니다.
* 값 셋팅 방법

  ```js
  let 변수명 = new Set('abcdeeeeee'); // Set 선언 종복안됨, abcde만 출력
  
  console.log(변수명); // 값 호출

  변수명.add('f'); // 값 추가

  for(let 변수명3 of 변수명){
  순회할 코드;
  }
  
  let 변수명2 = new Set('abcdeee'.split('')); // 값이 배열인 경우

  변수명2.delete('b'); // 값 제거

  변수명2.clear(); //모든 값 제거

  console.log(변수명2.has('a')); // 값 있는지 확인

  let a = new Set('abc');
  let b = new Set('cde');

  let cro = [...a].filter(value => b.has(value)); // 교집합
  let union = new Set([...a].concat([...b])); // 합집합
  let dif = [...a].filter(x => !b.has(x)); // 차집합
  ```

## JSON

* JSON 이란
  * 기존 xml을 업그래이드해서, 데이터를 서로 다른 언어에서 통신 가능하게끔 만들어주는 양식이다.
* JSON.parse()
  * JSON 문자열을 자바스크립트 객체로 변환해줍니다
* JSON.stringify()
  * 자바스크립트 객체를 JSON문자열로 변환
* [JSON 테스트 사이트](https://datagenerator.co.kr/)

## DOM(Document Object Model)

* 명령어
  1. document.head: head 내용 불러오기
  2. document.head.childNodes[]: head 내용 중[]안에 숫자번째줄 불러오기
  3. document.body: body 내용 불러오기
  4. document.body.childNodes: bodt 모든 내용 출력
  5. document.body.childNodes[1]. : .찍으면 사용가능한 애트리뷰트 확인 가능
* DOM 트리 접근
  1. getElementById('아이디명'); 아이디 접근
     * 내용 변경: 아이디명.innerText = 수정할 내용
  2. getElementByTagName('태그명'); 태그에 접근
  3. getElementByClassName('글래스명');
  4. querySelector("요소명"); 단일 요소 접근
  5. querySelectorAll("요소명"); 전체 요소명 접근
      * 리스트로 만들어서 추가 작업 가능
* 이벤트 삽입
  1. target.addEventListener(type, listener)

    ```js
    <button>hello world</button>
    <script>
    const myBtn  = document.querySelector("button");
    myBtn.addEventlistener('click', function(){
      console.classList.add("blue"); // class 추가
      console.classList.remove("blue"); // class 제거
      console.classList.toggle("blue"); // 있으면 없에주고 없으면 만들어주고
      console.log(myBtn.classList.contains("blue")); // 해당 클래스가 있는지 확인
    })
    </script>
    ```

* 요소제어
  1. document.createElement(요소) : 요소 추가
  2. document.createTextNode(요소) : 요소 텍스트를 생성
  3. element.appendChild(요소) : target 요소를 element의 자식으로 위치합니다
  4. element.removeChild(요소) : element의 target 자식 요소를 제거
  5. innerHTML: 테스트형식로 내용추가
  6. target: 속성에는 이벤트가 발생한 진원지의 정보가 담겨 있습니다.
  7. currentTarget: 속성에는 이벤트 리스너가 연결된 요소가 참조 되어 있습니다.
  8. preventDefault(): 브라우저의 기본 이벤트 동작을 취소합니다.


* 주의
  * 이벤트 생성할 때, 해당 이벤트의 부모 까지 영향을 줌으로, 코딩할 때 조심합시다.
  * target,currentTarget 사용.


## 동기 & 비동기

* 동기: 순차적 실행
* 비동기: 비순차적 실행(병력처럼 보이는 순차적 실행)

* promise: 동기를 비동기로 바꿔주는 객체
  * 상태
    * pending(대기상태) - resolve(해결) - fulfilled(성공)
    * pending(대기상태) - reject(거부) - rejected(실패)
* 모놀리식 처리 방식
  * 한개의 서버에서 모든것을 처리하는 것
* 마이크로 서비스 패턴
  * 여러 서버에서 분리하여 관리하고 처리하는 것, 클라인트는 fetch코드 받습니다.

