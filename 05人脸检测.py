#导入cv模块
import cv2 as cv

def face_detect_demmo():
    #获取img的灰度图
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #加载分类器
    face_detect=cv.CascadeClassifier('E:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    #调节
    #face=face_detect.detectMultiScale(gray,1.1,5,0,minSize=(10,10),maxSize=(50,50))
    face=face_detect.detectMultiScale(gray)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',img)


#获取图像
img=cv.imread('manyFace.jpg')
print("图片大小")
print(img.shape)
#检测函数
face_detect_demmo()
#等待
while True:
    if ord('q')==cv.waitKey(0):
        break
#释放内存
cv.destroyAllWindows()