import cv2 as cv
import numpy as np
from matplotlib import pyplot as plot

def main():
    image = ["prac04ex01img01.png","prac04ex01img02.png"]

    for x,imageName in enumerate(image):
        img = cv.imread("assets\\"+str(imageName))
        grayScale = cv.cvtColor(img,cv.COLOR_RGB2GRAY)

        sift = cv.xfeatures2d.SIFT_create()
        keypoints = sift.detect(grayScale,None)
        #the length of the keypoints is x which represent the number of keypoints
        print(keypoints)

        img = cv.drawKeypoints(grayScale,keypoints,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        #using .compute method to detect descriptor

        kp,des = sift.compute(grayScale,keypoints)
        #des.shape will output x,128
        #where x means there are 100 keypoints within the image and 128 represents the bin values are available

        cv.imwrite("SIFT\\"+str(imageName)+".png",img)
        cv.imwrite("descriptor\\des"+str(imageName),des)

    return 0

def writeFile(array):
    # writing array des into file:
    with open("descriptors.txt", 'w') as f:
        for item in array:
            f.write("%s\n" % item)

def printHistogram(des,imageName):
    plot.hist(des, 36)
    plot.title("Histogram For Descriptor" + str(imageName))
    plot.show()

if __name__ == '__main__':
    main()