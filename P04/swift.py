import cv2 as cv
import numpy as np

def main():
    image = ["prac04ex01img01.png","prac04ex01img02.png"]

    for x,imageName in enumerate(image):
        img = cv.imread("assets\\"+str(imageName))
        grayScale = cv.cvtColor(img,cv.COLOR_RGB2GRAY)

        sift = cv.xfeatures2d.SIFT_create()
        keypoints = sift.detect(grayScale,None)
        #the length of the keypoints is 100 which makes sense

        img = cv.drawKeypoints(grayScale,keypoints,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        #using .compute method to detect descriptor

        des = sift.compute(grayScale,keypoints)[1]
        #des.shape will output 100,128
        #where 100 means there are 100 keypoints within the image and 128 represents the bin values are available
        print(des.shape)

        cv.imwrite("SIFT\\"+str(imageName)+".png",img)

    return 0

def writeFile(array):
    # writing array des into file:
    with open("descriptors.txt", 'w') as f:
        for item in array:
            f.write("%s\n" % item)

if __name__ == '__main__':
    main()