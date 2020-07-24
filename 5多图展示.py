import cv2
import numpy as np

# 拼接的两张图片必须有相同数量的通道

img = cv2.imread('imgs/poke.jpg')
img2 = cv2.imread('imgs/textone.png')
# 水平方向拼接
imgHor = np.hstack((img, img))
# 垂直方向拼接
imgVer = np.vstack((img2, img2))

cv2.imshow("img", imgHor)
cv2.imshow("imgver", imgVer)

cv2.waitKey(0)
