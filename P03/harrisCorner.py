import cv2 as cv
import numpy as np

def saveImage(imageName,image):
    cv.imwrite("cornerAssets\\"+str(imageName),image)

def drawCorner(oriImage, harrisConerImage):
    oriImage[harrisConerImage > 0.01 * harrisConerImage.max()] = [0, 0, 255]
    cv.imshow(None, oriImage)
    cv.waitKey(0)
    return oriImage
def harrisDetection(imageGray):
    corner = cv.cornerHarris(imageGray, 3, 5, 0.02)
    corner = cv.dilate(corner, None)
    return corner
def turnGray(image):
    grayscale = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    grayscale = np.float32(grayscale)
    return grayscale
def main():
    imageName = "prac03ex01img03.png"
    image = cv.imread("assets\\"+str(imageName))
    grayscale = turnGray(image)
    corner = harrisDetection(grayscale)
    image=drawCorner(image,corner)
    saveImage("cornerDetection"+str(imageName),image)




if __name__ == '__main__':
    main()