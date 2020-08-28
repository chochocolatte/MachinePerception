import cv2 as cv
from P01 import cropping as read

def main():
    imageName = "prac01ex02img01.png"
    image = cv.imread('assets\\'+str(imageName))
    x_l, y_l, x_r, y_r=read.readFile("assets\\prac01ex02crop.txt")
    newImage = cv.rectangle(image,(int(x_l),int(y_l)),(int(x_r),int(y_r)),(0,0,255),2)

    yaxis = [y_l,y_r]
    for y, coord in enumerate(yaxis):
        cv.circle(image,(int(x_l),int(coord)),6,(0,255,0),2)
        cv.circle(image,(int(x_r),int(coord)),6,(0,255,0),2)
    cv.imshow("Drawing",newImage)
    cv.waitKey(0)

if __name__ == '__main__':
    main()