import os
import subprocess
import platform
import glob
import tobii_research as tr
import time
import numpy as np
import win32api


import pyautogui

from transcribe_streaming_mic2 import *




found_eyetrackers = tr.find_all_eyetrackers()

eyetracker = found_eyetrackers[0]

print("Address: " + eyetracker.address)
print("Model: " + eyetracker.model)
print("Name (It's OK if this is empty): " + eyetracker.device_name)
print("Serial number: " + eyetracker.serial_number)



xlist = []
ylist = []
xlist2=[]
ylist2=[]

count=1  #콜백함수를 루프처럼 활용하기 위해
count2=0
index=0





x_control = 0
y_control = 0
x1=965
y1=540
x2=965
y2=540
x3=965
y3=540
x4=965
y4=540
x=0
y=0





def gaze_data_callback(gaze_data):
    gaze_left_eye = gaze_data['left_gaze_point_on_display_area']
    gaze_right_eye = gaze_data['right_gaze_point_on_display_area']

    xs = (gaze_left_eye[0], gaze_right_eye[0])
    ys = (gaze_left_eye[1], gaze_right_eye[1])

    # if all of the axes have data from at least one eye
    if all([x != -1.0 for x in xs]) and all([y != -1.0 for y in ys]):
        # take x and y averages
        gaze_data_callback = (np.nanmean(xs), np.nanmean(ys))
    else:
        # or if no data, hide points by showing off screen
        gaze_data_callback = (np.nan(xs), np.nan(ys))



    x = int(np.nanmean(xs) * 1920)
    y = int(np.nanmean(ys) * 1080)



    global x1, y1, x2, y2, x3, y3, x4, y4, x, y

    x=int((x*3+x1*3+x2*2+x3*1+x4*1)/10)
    y=int((y*3+y1*3+y2*2+y3*1+y4*1)/10)

    x4 = x3
    y4 = y3
    x3 = x2
    y3 = y2
    x2 = x1
    y2 = y1
    x1 = x
    y1 = y





    global count  #30번 째 절단을 위한 count
    global count2   #16번 검증을 위한 count
    global index    #비교할 기준 값의 인덱스

    if (count%30==1):
        win32api.SetCursorPos((x, y))
        xlist.append(x)    #30번 째 들어 오는 값을 추가
        ylist.append(y)

        x_control=xlist[index]   #비교할 기준 값의 인덱스로 기준 값을 알 수 있음
        y_control=ylist[index]

        if (count2==4):   #X개가 다 범위 안에 들 경우
            xlist2.append(x_control)
            ylist2.append(y_control)
            count2=0   #다음 검증을 위해 카운트 값 0으로 리셋
            index+=4 #값이 들어 올 때마다 계산 하는 것이기 때문에 X개가 끝나면 다음 기준 값은 새로 들어오는 값
            print(xlist2,ylist2)
            pyautogui.doubleClick()

        elif (x_control-50<=x<=x_control+50 and y_control-50<=y<=y_control+50): #x,y 값이 처음 들어온 경우에는 control 값과 x, y의 값이 같기때문에 이 경우에 든다.
            count2+=1   #범위 안에 들면 카운트를 증가 시킴
        else:
            index+=1    #범위안에 안 들 경우는 기준값을 현재 기준값의 다음 값으로 변하게 하기 위해 index 1증가
            x_control=xlist[index]
            y_control=ylist[index]

            count2=0    #카운트 리셋
    count += 1#30개 자르는 카운트
    


if __name__ == "__main__":
    # execute(eyetracker)
    eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
    time.sleep(60)
    eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)

    #    win32api.SetCursorPos((xlist,ylist))
    
