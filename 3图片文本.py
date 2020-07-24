import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

# 指定范围进行BGR着色
img[200:300, 100:300] = 255, 0, 0
print(img.shape)

# 线条(图片, (开始x轴, 开始y轴), (结束x轴, 结束y轴), (B, G, R), 宽度)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# 矩形(图片, (开始x轴, 开始y轴), (结束x轴, 结束y轴), (B, G, R), 宽度)，对角线原理，宽度可以换成cv2.FILLED(实心)
cv2.rectangle(img, (0, 0), (250, 300), (0, 0, 255), 2)

# 圆(图片, (圆心x轴, 圆心y轴), 直径, (B, G, R), 宽度)，对角线原理，宽度可以换成cv2.FILLED(实心)
cv2.circle(img, (400, 50), 30, (255, 255, 0), 2)

# 文本(图片, 文本内容, 开始位置, 字体, 比例尺大小, 颜色, 厚度),对中文支持不好
s = ' 中文 '
cv2.putText(img, s.getbytes("utf-8"), (300, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

cv2.imshow("img", img)

cv2.waitKey(0)

