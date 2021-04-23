# -*- coding: utf-8 -*-
import numpy as np
import os
import matplotlib.image as img
from PIL import Image
import matplotlib.pylab as plt
from PIL import Image
from skimage import img_as_ubyte
import cv2


# 获取当前路径下的所有文件名
def listdir(path):
    list_name = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path)
        elif os.path.splitext(file_path)[1]=='.jpg':
            list_name.append(file_path)
    #print(list_name)
    return list_name

# get all raw image
#
def read_multi_jpg(path):
    return  0


def histogram_stas(path):
    #加载图像
    im = plt.imread(path)
    # srcImg = Image.open(path)

    histogram,_ = np.histogram(im[:,:,1],bins=256,range=(0,255))
    print('直方图：',histogram)

    #r, g, b = srcImg.split()
    r, g, b = im[:,:,0],im[:,:,1],im[:,:,2]

    # plt.figure("histogram")
    # ar = np.array(r).flatten()
    # plt.hist(ar, bins=256, facecolor='r', edgecolor='r')
    # ag = np.array(g).flatten()
    # plt.hist(ag, bins=256, facecolor='g', edgecolor='g')
    # ab = np.array(b).flatten()
    # plt.hist(ab, bins=256, facecolor='b', edgecolor='b')
    # plt.show()
    print(im.shape)
    print(im)
    sigma = np.array([2])
    #imnew = np.divide(im,sigma)
    imnew = np.array(im.shape,dtype=np.uint8)
    imnew = np.array(im).flatten()
    print(imnew)
    for i in range(imnew.shape[0]):
                imnew[i] = imnew[i] - 20
                if imnew[i] < 0:
                    imnew[i] = 0
                elif imnew[i] > 255:
                    imnew[i] = 255


    #imnew = im - 20
    print(imnew)
    imnew2 = imnew.reshape(im.shape)
    print(imnew2)

    img.imsave(r'C:\Users\herman\Desktop\RAW_TEST/new.jpg',imnew2)



if __name__ == '__main__':
    print("rawProcess function test：")
    filepath = r'C:\Users\herman\Desktop\RAW_TEST/IMG_20201130_212344.jpg'

    histogram_stas(filepath)




