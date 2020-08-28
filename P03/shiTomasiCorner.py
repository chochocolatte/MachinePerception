import cv2 as cv
import numpy as np

def saveImage(imageName,image):
    cv.imwrite("shiTomashiAssets\\"+str(imageName),image)
def convert2Gray(image):
    gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    return gray

def shiTomasiCorner(image):
    corner = cv.goodFeaturesToTrack(image,25,0.01,5)
    corner = np.int0(corner)
    return corner

def drawCorner(imageName,image,cornerImage):
    for i in cornerImage:
        x,y = i.ravel()
        cv.circle(image,(x,y),3,(0,0,255),-1)
    cv.imshow(None,image)
    cv.waitKey(0)
    saveImage("shiTomashiCorner"+str(imageName),image)

def main():
    image = ["prac03ex01img01.png","prac03ex01img02.png","prac03ex01img03.png"]

    for y,imageName in enumerate(image):
        image = cv.imread("assets\\"+str(imageName))
        grayScale = convert2Gray(image)
        cornerImage = shiTomasiCorner(grayScale)
        drawCorner(imageName,image,cornerImage)

if __name__ == '__main__':
    main()