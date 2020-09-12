import cv2
import pytesseract
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def cv2ImgAddText(img, text, x, y, textColor=(0, 255, 0), textSize=20):
    img_PIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    font = ImageFont.truetype('./simsun.ttc', textSize, encoding="utf-8")
    fillColor = textColor
    position = (x, y)
    str = text
    draw = ImageDraw.Draw(img_PIL)
    draw.text(position, str, font=font, fill=fillColor)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)


def get_wen(url):
    pytesseract.pytesseract.tesseract_cmd = 'G:\\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread(url)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # print(pytesseract.image_to_boxes(img, lang='chi_sim'))
    print(pytesseract.image_to_string(img, lang='chi_sim'))

    # 获取图片宽高，进行文字标注
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img, lang='chi_sim')

    # 去除无用字符
    for b in boxes.splitlines():
        print(b)
        b = b.split(' ')
        if b[-2] != '0':
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 2)
            img = cv2ImgAddText(img, b[0], x, hImg - y, (255, 0, 0), 20)

    cv2.imshow('test', img)
    cv2.waitKey(0)


if __name__ == '__main__':
   get_wen('./imgs/1.png')
