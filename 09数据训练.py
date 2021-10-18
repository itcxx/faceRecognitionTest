import os
import cv2
from cv2 import face
from PIL import Image
import numpy as np

def getImageAndLabels(path):
    #储存人脸数组
    facesSamples=[]
    #储存姓名数组
    ids=[]
    #储存图片信息
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #加载分类器
    face_detector=cv2.CascadeClassifier('E:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml')
    #遍历列表中的图像
    for imagePath in imagePaths:
        #打开图片，灰度化， PLI有九种不同的模式,1,L,P,RGB,RGBA,CMYK,YCbCr,I,F,
        PIL_img=Image.open(imagePath).convert('L')
        #将图像转换为数组，以灰度图
        img_numpy=np.array(PIL_img,'uint8')
        #获取图片人脸特征
        faces=face_detector.detectMultiScale(img_numpy)
        #获取每张图片的id和姓名
        id=int(os.path.split(imagePath)[1].split('.')[0])
        #预防无面容照片
        for x,y,w,h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y+h,x:x+w])
        #打印脸部特征id
    print('id:',id)
    print('fs:',facesSamples)
    return facesSamples,ids

if __name__=='__main__':
    #图片路径
    path='./data'
    #获取图像数组和id标签数据和姓名
    faces,ids=getImageAndLabels(path)
    #加载识别器
    recognizer=face.LBPHFaceRecognizer_create()
    #训练
    recognizer.train(faces,np.array(ids))
    #保存文件
    recognizer.write('./trainer/trainer.yml')