import cv2 as cv
import numpy as np

def main():
    imageName = "prac02ex03img01.jpg"
    image = cv.imread("assets\\"+str(imageName))
    median = cv.medianBlur(image,5,dst=None)

    cv.imwrite("medianFilteringAssets\\medianFilter"+str(imageName),median)
if __name__ == '__main__':
    main()