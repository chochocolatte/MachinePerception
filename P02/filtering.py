import numpy as np
import cv2 as cv

prewit_Kernels_X = np.matrix("-1,0,1;-1,0,1;-1,0,1")
prewit_Kernels_Y = np.matrix("-1,-1,-1;0,0,0;1,1,1")


sobel_Kernels_X = np.matrix("-1,0,1;-2,0,2;-1,0,1")
sobel_Kernels_Y = np.matrix("-1,-2,-1;0,0,0;1,2,1")


laplacian_kernel = np.matrix("0,1,0;1,-4,1;,0,1,0")

gaussian_constant = 1/273
gaussian_Kernel = gaussian_constant*np.matrix("1,4,7,4,1;4,16,26,16,4;7,26,41,26,7;"
                                              "4,16,26,16,4;1,4,7,4,1")

def flipArray(A):
    for i in range(len(A)):
        A[0,i],A[2,2-i]=A[2,2-i],A[0,i]
    A[1,0],A[1,2] = A[1,2],A[1,0]
    return A

def main():
    imageName = "prac02ex02img01.jpg"
    image = cv.imread("assets\\"+str(imageName),cv.IMREAD_GRAYSCALE)

    prewit_X = cv.filter2D(image,0,flipArray(prewit_Kernels_X))
    prewit_Y = cv.filter2D(image,0,flipArray(prewit_Kernels_Y))

    sobel_Y = cv.filter2D(image,0,flipArray(sobel_Kernels_Y))
    sobel_X = cv.filter2D(image,0,flipArray(sobel_Kernels_X))

    laplacian = cv.filter2D(image,0,flipArray(laplacian_kernel))

    gaussian = cv.filter2D(image,0,gaussian_Kernel)


    cv.imwrite("filteredAssets\\prewitX"+str(imageName),prewit_X)
    cv.imwrite("filteredAssets\\prewitY" + str(imageName), prewit_Y)

    cv.imwrite("filteredAssets\\sobelX"+str(imageName),sobel_X)
    cv.imwrite("filteredAssets\\sobelY"+str(imageName),sobel_Y)

    cv.imwrite("filteredAssets\\laplacian"+str(imageName),laplacian)

    cv.imwrite("filteredAssets\\gaussian"+str(imageName),gaussian)




if __name__ == '__main__':
    main()