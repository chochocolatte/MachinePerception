import cv2 as cv
import numpy as np
import matplotlib.pyplot as pt


def main():
    imageName = "prac04ex02img01.png"
    image = cv.imread("assets\\"+str(imageName),0)

    #preprocessing sobel operators

    gx = cv.Sobel(image,cv.CV_32F,1,0,ksize=1)
    gy = cv.Sobel(image,cv.CV_32F,0,1,ksize=1)

    magnitude, angle = cv.cartToPolar(gx,gy,angleInDegrees=True)

    pt.hist(angle.reshape(-1),bins=36)
    pt.xlabel("Angle in Degrees")
    pt.ylabel("Count")

    pt.show()

if __name__ == '__main__':
    main()