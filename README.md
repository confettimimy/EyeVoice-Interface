# EyeTracking Interface   

마우스 기기의 사용 없이 **시선추적**과 **[음성인식](https://github.com/confettimimy/EyeTracking-Interface/tree/main/EYE(sound))**(외 **[눈 깜빡임](https://github.com/confettimimy/EyeTracking-Interface/tree/main/EYE(blink))**, **[1초 응시 방식](https://github.com/confettimimy/EyeTracking-Interface/tree/main/EYE(gaze))**)을 이용해 컴퓨터를 사용할 수 있는 인터페이스

## [시연영상 보러가기](https://blog.naver.com/confettimimy/222095713733)  👈🏻😃   

### < Demo >

<img src="./README_img/demo.PNG" width="800">

포인터의 이동은 **눈의 시선**으로, 

포인터의 실행은 **음성명령**(외 눈 깜빡임, 1초 응시 방식)으로 진행합니다.

​    

---

## 아이트래킹 인터페이스 구동하기

### 1. tobii_research 라이브러리를 import 한 다음, tobii_research.find_all_eyetrackers() 함수를 사용해 사용 가능한 시선 추적기 목록을 가져옵니다. 

```python
import tobii_research
```

```python
found_eyetrackers = tr.find_all_eyetrackers()

eyetracker = found_eyetrackers[0]

print("Address: " + eyetracker.address)
print("Model: " + eyetracker.model)
print("Name (It's OK if this is empty): " + eyetracker.device_name)
print("Serial number: " + eyetracker.serial_number)
```

*find_all_eyetrackers에서 반환 된 객체는 tobii_research.EyeTracker의 인스턴스이다.

​    

### 2. 아이트래커에 연결

1. ts 라이브러리를 import

2. 캘리브레이션 

<캘리브레이션> 얼굴 눈에 맞춰 조정

<img src="./README_img/Calibration.jpg" width="250">



---

## 원리/ 설계도 / 방식

---

+논문정보