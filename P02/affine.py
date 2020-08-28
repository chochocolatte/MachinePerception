import cv2 as cv
import numpy as np

def main():
    brightness = 2;
    contrast = 2;

    imagename="prac02ex04img01.png"

    image = cv.imread("assets\\"+str(imagename))
    imageGray = cv.imread("assets\\"+str(imagename),cv.IMREAD_GRAYSCALE)

    copy = image.copy()
    copygray=imageGray.copy()

    affinePixel =affine(copy,contrast,brightness)
    affinePixelGray = affineGray(copygray,contrast,brightness)

    compare(image,affinePixel)

    cv.imwrite("affineAssets\\affinePixelGray.jpg",affinePixelGray)
    cv.imwrite("affineAssets\\affinePixel.jpg",affinePixel)

def affine(image,A,B):
    for layer in range(0,image.shape[2]): #RGB
        for x in range(0,image.shape[0]):
            for y in range(0, image.shape[1]):
                image[x,y,layer] = np.clip(image[x,y,layer]*A+B,0,255)
    return image

def affineGray(image,A,B):
    for x in range(0,image.shape[0]):
        for y in range(0, image.shape[1]):
            image[x,y] = np.clip(image[x,y]*A+B,0,255)
    return image


def affine2(image,A,B):
    newImage = np.clip(A*image+B,0,255)
    return newImage

def compare(image,image2):
    compare = np.concatenate((image,image2))
    cv.imshow("",compare)
    cv.waitKey(0)





if __name__ == '__main__':
    main()