import cv2 as cv
import numpy as np

def main():
    imageName = 'prac04ex01img01.png'
    print("OpenCV version: "+cv.__version__)
    img = cv.imread("assets\\"+str(imageName))
    grayScale = cv.cvtColor(img,cv.COLOR_RGB2GRAY)

    sift = cv.SIFT_create()
    keypoints = sift.detect(grayScale)

    img = cv.drawKeypoints(grayScale,keypoints,img)

    cv.imshow(None,img)
    cv.waitKey()

    return 0
if __name__ == '__main__':
    main()