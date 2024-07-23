# JavaScript의 기초 4일차

## 목차

## fetch

* fetch는 JavaScript에서 제공하는 현대적인 비동기 네트워크 통신 API입니다.
  * 주요 특징:
    * Promise 기반으로 구현되어 있습니다.
    * 비동기적으로 HTTP 요청을 보내고 응답을 받을 수 있습니다.
    * XMLHttpRequest의 더 강력하고 유연한 대안입니다.
  * 장점:
    * Promise를 사용하여 비동기 작업을 쉽게 처리할 수 있습니다.
    * .then()과 .catch()를 통해 성공 및 실패 상황을 간편하게 처리합니다.
    * async/await 문법과 함께 사용하면 가독성이 높은 비동기 코드를 작성할 수 있습니다.

## async와 await

* async와 await는 JavaScript에서 비동기 프로그래밍을 더 쉽고 읽기 좋게 만들어주는 문법적 개선사항입니다. ES2017(ES8)에서 도입되었습니다.
  * 주요 특징:
    * async는 함수 앞에 붙이는 키워드입니다.
    * 함수 내부에서 await 키워드를 사용할 수 있게 해줍니다.
  * 장점
    * 비동기 코드를 동기 코드처럼 읽기 쉽게 작성할 수 있습니다.
    * Promise 체인보다 더 직관적입니다.
    * 에러 처리를 try-catch 문을 사용해 더 자연스럽게 할 수 있습니다.

```javascript
async function getUser() {
  try {
    const response = await fetch('https://api.example.com/user');
    const user = await response.json();
    console.log(user);
  } catch (error) {
    console.error('Failed to fetch user:', error);
  }
}
```

## CSS transform 속성

`transform`은 HTML 요소의 형태, 위치, 크기 등을 변형시키는 CSS 속성입니다. 2D 또는 3D 변환을 적용할 수 있으며, 요소의 좌표 공간을 변경합니다.

### 주요 transform 함수들

1. `translate(x,y)`: 요소를 X축과 Y축으로 이동
2. `scale(x,y)`: 요소의 크기를 X축과 Y축으로 조절
3. `rotate(angle)`: 요소를 지정된 각도만큼 회전
4. `skew(x-angle,y-angle)`: 요소를 X축과 Y축으로 기울임

3D 변환을 위한 함수들도 있습니다 (예: `translateZ()`, `rotateX()` 등).

```css
.box {
  transform: translate(50px, 100px) rotate(45deg) scale(1.5);
}
```

이 코드는 요소를 오른쪽으로 50px, 아래로 100px 이동시키고, 45도 회전시킨 뒤, 크기를 1.5배로 확대합니다.

### transform의 장점

* 레이아웃에 영향을 주지 않고 요소를 조작할 수 있습니다.
* GPU 가속을 활용하여 성능이 좋습니다.
* 애니메이션과 결합하여 동적인 효과를 만들 수 있습니다.

## CSS transform의 구현 범위와 3D 변환

CSS transform은 2D와 3D 변환을 모두 지원하며, 매우 다양한 변환 효과를 구현할 수 있습니다.

### 2D 변환

기본적인 2D 변환 함수들:

- `translate(x, y)`
- `scale(x, y)`
- `rotate(angle)`
- `skew(x-angle, y-angle)`
- `matrix(a, b, c, d, tx, ty)`

### 3D 변환

CSS는 다음과 같은 3D 변환 함수들을 제공합니다:

- `translate3d(x, y, z)`
- `scale3d(x, y, z)`
- `rotate3d(x, y, z, angle)`
- `perspective(n)`
- `matrix3d()`

### 3D 변환 예시

```css
.box {
  transform: rotateX(45deg) rotateY(30deg) translateZ(100px);
}
```

## 고급 3D 효과

1. **원근감 (Perspective)**
   ```css
   .container {
     perspective: 1000px;
   }
   .box {
     transform: rotateY(45deg);
   }
   ```

2. **3D 공간 유지 (Preserve-3d)**
   ```css
   .container {
     transform-style: preserve-3d;
   }
   ```

3. **뒷면 가시성 (Backface Visibility)**
   ```css
   .box {
     backface-visibility: hidden;
   }
   ```

## 구현 가능한 효과들

1. 3D 큐브 만들기
2. 카드 뒤집기 효과
3. 회전하는 캐러셀
4. 3D 텍스트 효과
5. 패럴랙스 스크롤링

## 브라우저 지원

대부분의 현대 브라우저들은 2D와 3D transform을 잘 지원합니다. 그러나 일부 오래된 브라우저에서는 3D 효과가 제대로 작동하지 않을 수 있으므로, 필요한 경우 폴백(fallback) 스타일을 제공하는 것이 좋습니다.

## 성능 고려사항

3D 변환은 GPU 가속을 활용하여 성능이 좋지만, 복잡한 3D 효과를 많이 사용하면 성능에 영향을 줄 수 있습니다. 따라서 필요한 경우에만 적절히 사용하는 것이 좋습니다.