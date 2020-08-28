import numpy as np
import cv2 as cv
import math

def main():
    imageList = ["prac03ex03img01.png","prac03ex03img02.jpg","1500x500.png"]
    for x, imageName in enumerate(imageList):
        image = cv.imread("assets\\"+str(imageName))
        canny = cv.Canny(image, 50, 200, None, 3)
        cv.imshow("canny", canny)
        lines = cv.HoughLinesP(canny,1,np.pi/180,200,None,40,5)

        if lines is not None:
            for i in range(0,len(lines)):
                line = lines[i][0]
                print(line)
                cv.line(image,(line[0],line[1]),(line[2],line[3]),(0,0,255),1,cv.LINE_AA)
            cv.imshow("Source",image)
            cv.waitKey(0)
if __name__ == '__main__':
    main()