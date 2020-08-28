import numpy as np
import cv2 as cv

prewit_kernels_X = np.matrix("-1,0,1;-1,0,1;-1,0,1")
prewit_kernels_Y = np.matrix("-1,-1,-1;0,0,0;1,1,1")

sobel_kernels_X = np.matrix("-1,0,1;-2,0,2;-1,0,1")
sobel_kernels_Y = np.matrix("-1,-2,-1;0,0,0;1,2,1")

def flipArray(A):
    for i in range(len(A)):
        A[0,i],A[2,2-i]=A[2,2-i],A[0,i]
    A[1,0],A[1,2] = A[1,2],A[1,0]
    return A

def main():
    imageList = ["prac03ex01img01.png", "prac03ex01img02.png", "prac03ex01img03.png"]
    kernelList = [prewit_kernels_X,prewit_kernels_Y,sobel_kernels_X,sobel_kernels_Y]
    for x,imageName in enumerate(imageList):
        image = cv.imread("assets\\"+imageName)
        filter(image,x,imageName,kernelList)

def filter(image,x,imageName,kernelList):
    for y,kernelName in enumerate(kernelList):
        effect = cv.filter2D(image,0,flipArray(kernelName))
        cv.imwrite("edgeDetection\\"+str(x)+str(y)+str(imageName),effect)


if __name__ == '__main__':
    main()