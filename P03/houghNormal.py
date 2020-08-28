import numpy as np
import cv2 as cv
import math


def main():
    imageList = ["prac03ex03img01.png", "prac03ex03img02.jpg", "1500x500.png"]
    for x, imageName in enumerate(imageList):
        image = cv.imread("assets\\" + str(imageName))

        canny = cv.Canny(image,100,200)
        cv.imshow(None,canny)

        lines = cv.HoughLines(canny, 1, np.pi / 180, 200)

        if lines is not None:
            print(lines.shape)
            for point in lines:
                r, theta = point[0]
                a = np.cos(theta)
                b = np.sin(theta)
                x = a*r
                y = b*r
                point1 = (int(x+1000*(-b)),int(y+1000*(a)))
                point2 = (int(x-1000*(-b)),int(y-1000*(a)))
                cv.line(image,point1,point2,(255,0,0),1,cv.LINE_AA)
            cv.imshow("Source Image", image)
            cv.waitKey()


if __name__ == '__main__':
    main()
