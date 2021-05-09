## CAROUSEL

### Carousel이란?
- 회전목마(돌고 도는)
- 웹페이지에서 사용자가 많은 정보들을 스크롤 없이,
- 고정된 화면에서 노출 (보통 이미지)
- 흔히 좌, 우 원형큐 구조 이미지 슬라이더

### 구현시 고려해볼 점
- 노출할 이미지들의 (width, height) 측정 필요
- 이미지 사이즈가 동일하지 않을 수 있다.
- 좌, 우측 버튼 클릭시 -> 슬라이더 이미지 이동
- 마지막 이미지에서 버튼 클릭 -> 다시 첫 이미지 표시

### 구현 해야 할 목록
- (슬라이더에 들어갈 이미지: 4개라 가정)
- [ ] 이미지 파일을 js에서 동적으로 html에 띄운다.
- [ ] carousel 메인에는 1개의 이미지만 보여야 한다.
- [ ] 좌, 우 버튼 클릭시 이미지 슬라이더 애니매이션 효과
- (Transition 효과)
- [ ] 이미지 순서 : 4, [1, 2, 3, 4], 1
- [ ] 슬라이더 버튼 (왼쪽, 오른쪽) 구성
- [ ] 맨앞, 맨뒤 이미지는 1,4번 이미지를 클론하여 배치
- [ ] 맨앞 이미지 -> 좌측버튼 -> 4번 이미지로 이동
- [ ] 맨뒤 이미지 -> 우측버튼 -> 1번 이미지로 이동
- (위의 두 경우, Transition 효과 대신 이미지 이동)

### CSS 구조
- .carousel : 현재 이미지를 보여줄 컨테이너
- 보여줄 이미지만 보여주고, 나머지는 숨김
- .carousel-slides: 이미지를 담은 컨테이너
- 이미지 이동 로직, transiton 효과 로직
- 이미지 이동 : <이미지의 사이즈를 모른다 가정>
- 이미지 width 측정 후 움직임 
```CSS
.carousel {
  position: relative;
  margin: 0 auto;
  overflow: hidden;
  /* carousel 요소의 width 셋팅이 완료될 때까지 감춘다. */
  opacity: 0;
}

.carousel-slides {
  --currentSlide: 0;
  --duration: 0;
  
  display: flex;
  transition: transform calc(var(--duration) * 1ms) ease-out;
  transform: translate3D(calc(var(--currentSlide) * -100%), 0, 0);
}
```

```CSS
/* carousel의 prev, next 버튼 */
.carousel-control {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-size: 2em;
  color: #fff;
  background-color: transparent;
  border-color: transparent;
  cursor: pointer;
  z-index: 99;
}

.carousel-control:focus {
  outline: none;
}

/* carousel의 prev 버튼 */
.carousel-control.prev {
  left: 0;
}

/* carousel의 next 버튼 */
.carousel-control.next {
  right: 0;
}
```
---

### javascript 구현
- [ ] 이미지 순서 : 4, [1, 2, 3, 4], 1
- [ ] 맨앞, 맨뒤 이미지는 1,4번 이미지를 클론하여 배치
- [ ] 슬라이더 버튼 (왼쪽, 오른쪽) 구성
```javascript
  const carousel = ($container, images) => {
    ...
    let $carouselSlides = null;
    ...
    document.addEventListener('DOMContentLoaded', () => {
    // 'DOMContentLoaded' : DOM 로드 시
    // html에 carousel-slides div 삽입
      $container.innerHTML = `
        <div class="carousel-slides">
          ${[images[images.length - 1], ...images, images[0]]
          .map(url => `<img src="${url}" />`).join('')}
        </div>
      <button class="carousel-control prev">&laquo;</button>
      <button class="carousel-control next">&raquo;</button>
    `;

      $carouselSlides = document.querySelector('.carousel-slides');
    });

  }
```

- [ ] carousel의 width 계산
- [ ] carousel-slides 이미지 요소 이동
- [ ] 이미지 파일을 js에서 동적으로 html에 띄운다.
```javascript
  ...
  let currentSlide = 0;
  const DURATION = 500;
  let isMoving = false;
  ...

  const move = (currentSlide, duration = 0) => {
    // duration이 0이 아니면 transition이 시작된다. 
    // isMoving은 transionend 이벤트가 발생하면 false가 된다.
    if (duration) isMoving = true;
    $carouselSlides.style.setProperty('--duration', duration);
    $carouselSlides.style.setProperty('--currentSlide', currentSlide);
  };


  window.onload = () => {
    // 슬라이드에 이미지 로드 될때마다 width 측정
    const { offsetWidth } = $carouselSlides.querySelector('img');
    $container.style.width = `${offsetWidth}px`;
    
    // 1번 index 이미지를 처음에 보여줘야 하기 때문에 강제 이동
    // duration = 0 -> transition 효과 없이 순간이동 -> 첫화면 등장
    move(++currentSlide);
    $container.style.opacity = 1;

  };
```

- [ ] 왼쪽, 오른쪽 슬라이드 버튼 클릭시 이미지 이동
```javascript
  $container.onclick = ({ target }) => {
    // carousel-control 버튼 요소가 아니면 return
    // isMoving이 true면(transition 하는 중 -> duration 값이 0 이상) return
    // (동작 꼬임 방지)
    if (!target.classList.contains('carousel-control') || isMoving)
     return;

    const delta = target.classList.contains('prev') ? -1 : 1;
    currentSlide += 1 * delta;
    move(currentSlide, DURATION);
  };
```

- [ ] 맨앞 이미지 -> 좌측버튼 -> 4번 이미지로 이동
- [ ] 맨뒤 이미지 -> 우측버튼 -> 1번 이미지로 이동
- (Transition 효과 대신 이미지 이동)
```javascript
  $container.ontransitionend = () => {
    // trainsition 종료 될때마다 발생
    isMoving = false;

    const delta = currentSlide === 0 ? 1 : currentSlide === images.length + 1 ? -1 : 0;

    // 클론 슬라이드가 아니면(delta === 0) 이동하지 않는다.
    if (!delta) return;

    // 슬라이드 index: 1 -> 0 이동시 -> 5번으로 이동
    // 슬라이드 index: 4 -> 5 이동시 -> 1번으로 이동
    currentSlide += images.length * delta;
    move(currentSlide);
  };
```


### 참고
- [MDN - CSS Set Property](https://developer.mozilla.org/ko/docs/Web/CSS/Using_CSS_custom_properties)
- [MDN - CSS Transition](https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)
- [MDN - CSS Z-index](https://developer.mozilla.org/ko/docs/Web/CSS/z-index)
- [MDN - CSS Transform](https://developer.mozilla.org/ko/docs/Web/CSS/transform)