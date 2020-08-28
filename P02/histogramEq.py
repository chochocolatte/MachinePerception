import cv2 as cv
from P02 import affine as show
def main():
    imageName = "prac02ex05img01.png"
    image = cv.imread("assets\\"+str(imageName),cv.IMREAD_GRAYSCALE)
    newImage = cv.equalizeHist(image)

    show.compare(image,newImage)




if __name__ == '__main__':
    main()