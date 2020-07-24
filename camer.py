import cv2   # pip install opencv-python
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def cv2ImgAddText(img, text, x, y, textColor=(0, 255, 0), textSize=20):
    cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_PIL = Image.fromarray(cv2img)
    draw = ImageDraw.Draw(img_PIL)
    font = ImageFont.truetype('./simsun.ttc', textSize, encoding="utf-8")
    fillColor = textColor
    position = (x, y)
    draw.text(position, text, font=font, fill=fillColor)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)


def Start():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        success, img = cap.read()
        faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            img = cv2ImgAddText(img, "人脸", x, y, (255, 0, 0), 20)
            # cv2.putText(img, ' OpenCV ', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
            cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    Start()
