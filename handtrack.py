import cv2
import mediapipe as mp
import time
import numpy as np

###############################
wcam,hcam =640,720
###############################

cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime=0
cTime=0

while True:
    success, img=cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                #print(id,lm)
                h,w,c = img.shape
                cx,cy = int(lm.x * w),int(lm.y*h)
                print(id,cx,cy)
                # if id == 4:
                #     cv2.circle(img, (cx, cy), 16, (255, 25, 255), cv2.FILLED)
                if id == 20:
                    cv2.putText(img,"pinkie fing",(cx,cy),cv2.FONT_HERSHEY_PLAIN,2,(255,25,0),3)
                if id == 16:
                    cv2.putText(img,"ring fing",(cx,cy),cv2.FONT_HERSHEY_PLAIN,2,(255,25,0),3)
                if id == 8:
                    cv2.putText(img,"index",(cx,cy),cv2.FONT_HERSHEY_PLAIN,2,(255,25,0),3)
                if id == 4:
                    cv2.putText(img,"thumb",(cx,cy),cv2.FONT_HERSHEY_PLAIN,2,(255,25,0),3)
                if id == 12:
                    cv2.putText(img,"midfing",(cx,cy),cv2.FONT_HERSHEY_PLAIN,2,(255,25,0),3)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cTime=time.time()
    fps= 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{str(int(fps))}',(48,50),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)

    cv2.imshow("image:",img)
    cv2.waitKey(1)
