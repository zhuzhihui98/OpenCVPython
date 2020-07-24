import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


# 获取边缘轮廓函数
def getContours(img):
    # (读取图片，轮廓读取顺序，轮廓输出方式（将所有的连码点，转换成点）)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # 计算轮廓面积
        ares = cv2.contourArea(cnt)
        print("面积:" + str(ares))
        # 设置阈值,防止为很小的噪点画轮廓
        if ares > 500:
            # 在原图片上画出图像轮廓
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # 计算周长
            peri = cv2.arcLength(cnt, True)
            print("周长:" + str(peri))
            # 多变拟合
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)

            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                # 通过长宽比判断是否是正方形
                aspRatio = w / float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            else:
                objectType = "None"

            # 得到包覆此轮廓的最小正矩形
            x, y, w, h = cv2.boundingRect(approx)
            # 绘制矩形边框
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType,
                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)


img = cv2.imread('imgs/shapes.png')
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
# 边缘检测
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

imgblack = np.zeros_like(img)
imgStack = stackImages(0.6, ([img, imgGray, imgBlur],
                             [imgCanny, imgContour, imgblack]))
cv2.imshow('Stack Img', imgStack)
cv2.waitKey(0)
