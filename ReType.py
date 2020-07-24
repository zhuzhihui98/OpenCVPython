import fnmatch
import os
import pandas as pd
import numpy as np
import sys
import cv2


def ReadSaveAddr(Stra, Strb):
    # print(Stra)
    # print(Strb)
    print("Read :", Stra, Strb)
    a_list = fnmatch.filter(os.listdir(Stra), Strb)
    print("Find = ", len(a_list))
    df = pd.DataFrame(np.arange(len(a_list)).reshape((len(a_list), 1)), columns=['Addr'])
    df.Addr = a_list

    for i in range(len(a_list)):
        path = Stra + '/' + a_list[i]
        # print(path)
        img = cv2.imread(path)
        t = a_list[i]
        t = t[:-4]
        t = 'C:/Users/86198/Desktop/huo_bmp/' + t + '.bmp'
        cv2.imshow("img",img)
        cv2.waitKey(0)
        cv2.imwrite(t, img)

    df.to_csv('Get.lst', columns=['Addr'], index=False, header=False)
    print("Write To Get.lst !")


ReadSaveAddr("C:/Users/86198/Desktop/huo/", "*.png")
