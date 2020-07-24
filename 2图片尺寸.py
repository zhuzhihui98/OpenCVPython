import cv2

img = cv2.imread('imgs/textone.png')
# 输出图片尺寸
print(img.shape)

# 规定图片尺寸读取
imgResize = cv2.resize(img, (500, 300))
print(imgResize.shape)

# 图片剪裁,Y轴开始像素:结束像素;X轴开始像素:结束像素
imgCropped = img[0:80, 20:200]

cv2.imshow('Img', img)
cv2.imshow('imgResize', imgResize)
cv2.imshow('imgCropped', imgCropped)

cv2.waitKey(0)

