import os


filepath = "C:/Users/86198/Desktop/1"
filenames = os.listdir(filepath)

for i in range(len(filenames)):
    newname = 'img' + str(i)

    # newname = 'data'+name  # 若想要在名字前面加字符段，可用此语句

    os.rename(filepath + '\\' + filenames[i], filepath + '\\' + newname + '.png')


