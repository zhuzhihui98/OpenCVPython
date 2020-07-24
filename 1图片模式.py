import cv2
import numpy as np

# 读取图片信息(图片名称最好使用纯英文，否则容易出错！)
img = cv2.imread('imgs/textone.png')
# numpy内核
kernel = np.ones((5, 5), np.uint8)

# 转换图片灰度
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 图片模糊
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# 图片边缘
imgCanny = cv2.Canny(img, 150, 200)
# 图片膨胀
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# 图片侵蚀
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


cv2.imshow("img", img)
cv2.imshow("Gray Img", imgGray)
cv2.imshow("Blur Img", imgBlur)
cv2.imshow("Canny Img", imgCanny)
cv2.imshow("Dialation Img", imgDialation)
cv2.imshow("Eroded Img", imgEroded)
cv2.waitKey(0)
