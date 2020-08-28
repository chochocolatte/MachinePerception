import cv2 as cv

def main():
    imagename = 'prac02ex01img01.jpg'
    image = cv.imread("assets\\"+str(imagename),cv.IMREAD_COLOR)
    #grayscale
    image_GRAY = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    cv.imshow("Grayscale Image",image_GRAY)
    cv.waitKey(0)

    # RGB TO HSV
    image_HSV = cv.cvtColor(image, cv.COLOR_RGB2HSV)
    cv.imshow("HSV Image", image_HSV)
    cv.waitKey(0)

    # RGB TO LUV
    image_LUV = cv.cvtColor(image, cv.COLOR_RGB2Luv)
    cv.imshow("LUV Image", image_LUV)
    cv.waitKey(0)

    # RGB TO LAB
    image_LAB = cv.cvtColor(image, cv.COLOR_RGB2LAB)
    cv.imshow("LAB Image", image_LAB)
    cv.waitKey(0)

if __name__ == '__main__':
    main()