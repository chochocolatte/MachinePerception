import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

prewit_kernels_X = np.matrix("-1,0,1;-1,0,1;-1,0,1")
prewit_kernels_Y = np.matrix("-1,-1,-1;0,0,0;1,1,1")

sobel_kernels_X = np.matrix("-1,0,1;-2,0,2;-1,0,1")
sobel_kernels_Y = np.matrix("-1,-2,-1;0,0,0;1,2,1")

gaussian_constant = 1/273
gaussian_Kernel = gaussian_constant*np.matrix("1,4,7,4,1;4,16,26,16,4;7,26,41,26,7;"
                                              "4,16,26,16,4;1,4,7,4,1")

def flipArray(A):
    for i in range(len(A)):
        A[0,i],A[2,2-i]=A[2,2-i],A[0,i]
    A[1,0],A[1,2] = A[1,2],A[1,0]
    return A

def main():
    imageList = ["prac03ex01img01.png", "prac03ex01img02.png", "prac03ex01img03.png"]
    for x,imageName in enumerate(imageList):
        image = cv.imread("assets\\"+imageName)
        image = cv.filter2D(image,0,gaussian_Kernel)
        cannyMethod(image,sobel_kernels_X,sobel_kernels_Y)

def cannyMethod(image,kernelX,kernelY):
    x = cv.filter2D(image,0,flipArray(kernelX))
    y = cv.filter2D(image,0,flipArray(kernelY))
    G = np.clip(np.float32(np.hypot(x,y)),0,1)
    plt.imshow(G,cmap='gray')
    plt.show()





if __name__ == '__main__':
    main()