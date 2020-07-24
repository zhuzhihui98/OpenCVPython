import cv2
import numpy as np

img = cv2.imread('imgs/poke.jpg')

# 确定扑克的宽和高
width, height = 250, 350
# 确定获取图片的四个点
pts1 = np.float32([[122, 254], [324, 219], [169, 551], [395, 504]])
# 转换后的图形四角定位
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# 透视变换
matrix = cv2.getPerspectiveTransform(pts1, pts2)
# 投影映射
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('poke', img)
cv2.imshow('pokepoke', imgOutput)
cv2.waitKey(0)

