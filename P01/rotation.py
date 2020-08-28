import cv2 as cv
import imutils as imageutility
def main():
    imagename="prac01ex04img01.png"
    image = cv.imread("assets\\"+str(imagename))
    (height,width) = image.shape[:2]
    #image = imageutility.rotate(image,45)
    matrix = cv.getRotationMatrix2D((width/2,height/2),45,1)
    rotatedimage = cv.warpAffine(image,matrix,(width,height))
    cv.imshow("Rotated Image",rotatedimage)
    cv.waitKey(0)
    
if __name__ == '__main__':
    main()