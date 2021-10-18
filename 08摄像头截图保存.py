#导入模块
import cv2 as cv

#获取摄像头
cap=cv.VideoCapture(0)
num=0

while True:
    flag,frame=cap.read() #读取摄像头，返回值有两个，有值时flag为真，frame为当前帧的值
    cv.imshow("摄像",frame)
    k=cv.waitKey(100)

    if k==ord('s'): #保存
        cv.imwrite("StoreImage/image"+str(num)+".jpg",frame)
        print('success to save image'+str(num)+'.jpg')
        num+=1
    elif k==ord('q'): #退出
        break

#释放摄像头
cap.release()
#释放内存
cv.destroyAllWindows()