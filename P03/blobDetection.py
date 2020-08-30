import cv2 as cv

def main():
    imageList = ['prac03ex04img01.png','prac03ex04img02.png','prac03ex04img03.png','prac03ex02img01.jpg']

    for imageName in imageList:
        image = cv.imread("assets\\"+str(imageName),cv.IMREAD_GRAYSCALE)
        MSER(image)

def MSER(image):
    if image is not None:
        copy_Image = image.copy()
        mser = cv.MSER_create()

        regions = mser.detectRegions(image)
        hulls = [cv.convexHull(p.reshape(-1,1,2)) for p in regions[0]]

        copy_Image = cv.cvtColor(copy_Image,cv.COLOR_GRAY2BGR)
        cv.polylines(copy_Image,hulls,1,(7,255,0))

        cv.imshow("",copy_Image)
        cv.waitKey()


if __name__ == '__main__':
    main()