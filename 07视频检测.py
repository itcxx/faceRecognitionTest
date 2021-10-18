#导入cv模块
import cv2 as cv

def face_detect_demmo(img):
    #获取img的灰度图
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #加载分类器
    face_detect=cv.CascadeClassifier('E:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml')
    #调节
    #face=face_detect.detectMultiScale(gray,1.1,5,0,minSize=(10,10),maxSize=(50,50))
    face=face_detect.detectMultiScale(gray)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(255,0,0),thickness=2)
    cv.imshow('result',img)


#获取摄像头
cap=cv.VideoCapture(0)
#cap=cv.VideoCapture('C:/Users/11261/Pictures/Camera Roll/video.mp4')

#循环
while True:
    flag,frame=cap.read()
    if not flag:
        print(flag)
        break
    face_detect_demmo(frame)
    if ord('q')==cv.waitKey(100):
        break
#释放内存
cv.destroyAllWindows()
#释放摄像头
cap.release()