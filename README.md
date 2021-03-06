# EyeTracking Interface   

마우스 기기의 사용 없이 **시선추적**과 **[음성인식](https://github.com/confettimimy/EyeTracking-Interface/tree/main/EYE(sound))**(외 [눈 깜빡임](https://github.com/confettimimy/EyeTracking-Interface/tree/main/EYE(blink)), [응시](https://github.com/confettimimy/EyeTracking-Interface/tree/main/EYE(gaze)) 방식)을 이용해 컴퓨터를 사용할 수 있는 인터페이스

### [시연영상 보러가기](https://blog.naver.com/confettimimy/222095713733)  👈🏻😃   

[demo 사진] <img>

포인터의 이동은 눈의 시선으로, 포인터의 실행은 음성명령()으로 진행

클릭과 같은 포인터 실행 방식은 음성인식 외에도 눈 깜빡임, 1초간 응시의 방법이 있습니다. 이를 따로 구현하여 소스코드를 올려놓았습니다.

---

## 순서



1. ts 라이브러리를 import

2. 캘리브레이션 

<캘리브레이션> 얼굴 눈에 맞춰 조정

<img src="./README_img/Calibration.jpg" width="200">



---

## 원리/ 설계도 / 방식

---

+논문정보