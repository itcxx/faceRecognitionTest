#导入cv模块
import cv2 as cv

cap=cv.VideoCapture(0)

while True:
    flag, frame = cap.read()
    cv.imshow('video',frame)
    #等待100ms,循环一次，读取一次图片
    if ord('q')==cv.waitKey(100):
        break
cap.release()
