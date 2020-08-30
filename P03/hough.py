import numpy as np
import cv2 as cv
import math

rho = 1
angle = np.pi/180
threshold = 200

def setRho(rhoVal):
    global rho
    rho = rhoVal
    houghTransformP()

def setAngle(angleVal):
    global angle
    angle = angleVal
    houghTransformP()

def setThreshold(newVal):
    global threshold
    threshold = newVal
    houghTransformP()

def main():
    global img, rho, angle, threshold
    imageList = ["prac03ex03img01.png", "prac03ex03img02.jpg"]
    for i, imagename in enumerate(imageList):
        img = cv.imread("assets\\"+str(imagename))
        houghTransformP()
        cv.createTrackbar("Rho Value","Edge Detection",rho,10,setRho)
        cv.createTrackbar("Angle Value","Edge Detection",int(angle),360,setAngle)
        cv.createTrackbar("Threshold value","Edge Detection",threshold,2000,setThreshold)
        cv.waitKey()

def houghTransformP():
    global img,rho,angle,threshold
    print("RHO IS NOW " + str(rho))
    print("ANGLE IS NOW " + str(angle))
    print("THRESHOLD IS NOW " + str(threshold))
    edge = cv.Canny(img,100,300)
    cv.imshow("Edge",edge)
    lines = cv.HoughLines(edge,rho,angle,threshold)

    if lines is not None:
        imgCopy = img.copy()
        for line in lines:
            r,theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x = a * r
            y = b * r

            point1 = (int(x+1000*(-b)),int(y+1000*(a)))
            point2 = (int(x-1000*(-b)),int(y-1000*(a)))
            imgCopy = cv.line(imgCopy,point1,point2,(0,0,255),2)
        cv.imshow("edge Detection",imgCopy)


if __name__ == '__main__':
    main()