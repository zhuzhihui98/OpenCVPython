import cv2


def open_cv(imgURL):
    faceCascade = cv2.CascadeClassifier("Resources/Xiaozhuan_huo.xml")
    img = cv2.imread(imgURL)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    get_X = 0
    temp = 0
    for (x, y, w, h) in faces:
        if w * h > temp:
            xz = x
            yz = y
            wz = w
            hz = h
            temp = w * h
            get_X = x
    cv2.rectangle(img, (xz, yz), (xz + wz, yz + hz), (0, 255, 0), 2)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    return get_X


if __name__ == '__main__':
    url = 'C:/Users/86198/Desktop/huo/img20.png'
    x = open_cv(url)
    print(x)
