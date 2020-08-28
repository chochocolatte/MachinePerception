import cv2 as cv
import numpy as np
def imageshow(winname,image,image2):
    compare = np.concatenate((image,image2),axis=1)
    writeImage(winname,compare)
    cv.imshow(str(winname),compare)
    cv.waitKey(0)
def writeImage(winname,image):
    cv.imwrite("morphology\\"+str(winname)+".jpg",image)
def opening(image,kernel):
    open = cv.morphologyEx(image,cv.MORPH_OPEN,kernel)
    return open

def closing(image, kernel):
    close = cv.morphologyEx(image,cv.MORPH_CLOSE,kernel)
    return close

def morphGradient(image,kernel):
    grad = cv.morphologyEx(image,cv.MORPH_GRADIENT,kernel)
    return grad

def blackHat(image,kernel):
    hat = cv.morphologyEx(image,cv.MORPH_BLACKHAT,kernel)
    return hat
def main():
    imageName1 = "prac02ex06img01.png"
    imageName2 = "prac02ex06img02.png"

    image1 = cv.imread("assets\\"+str(imageName1))
    image2 = cv.imread("assets\\"+str(imageName2))

    imageshow("Opening Image1",image1,opening(image1.copy(),cv.getStructuringElement(cv.MORPH_RECT,(5,5))))
    imageshow("Opening Image2", image2, opening(image2.copy(), cv.getStructuringElement(cv.MORPH_RECT, (5, 5))))

    imageshow("Closing Image1", image1, closing(image1.copy(), cv.getStructuringElement(cv.MORPH_RECT, (5, 5))))
    imageshow("Closing Image2", image2, closing(image2.copy(), cv.getStructuringElement(cv.MORPH_RECT, (5, 5))))

    imageshow("Morphological Gradient Image1", image1, morphGradient(image1.copy(), cv.getStructuringElement(cv.MORPH_RECT, (5, 5))))
    imageshow("Morphological Gradient Image2", image2, morphGradient(image2.copy(), cv.getStructuringElement(cv.MORPH_RECT, (5, 5))))

    imageshow("Black Hat Image1", image1, blackHat(image1.copy(), cv.getStructuringElement(cv.MORPH_RECT, (5, 5))))
    imageshow("Black Hat Image2", image2, blackHat(image2.copy(), cv.getStructuringElement(cv.MORPH_RECT, (5, 5))))

if __name__ == '__main__':
    main()