import cv2 as cv
import numpy as np
from matplotlib import pyplot as plot

def main():
    original = "prac04ex01img01.png"
    test = "prac04ex01img02.png"

    originalImage = cv.imread("assets\\"+str(original))
    testImage = cv.imread("assets\\"+str(test))

    #for original image
    training_image = cv.cvtColor(originalImage,cv.COLOR_BGR2RGB)
    grayScale = cv.cvtColor(training_image,cv.COLOR_RGB2GRAY)

    #for testImage
    testImage = cv.cvtColor(testImage,cv.COLOR_BGR2RGB)
    grayScale2 = cv.cvtColor(testImage,cv.COLOR_RGB2GRAY)



    #sift of the training image

    sift = cv.xfeatures2d.SIFT_create()

    keypoints, descriptors = sift.detectAndCompute(grayScale,None)

    kp2,des2 = sift.detectAndCompute(grayScale2,None)

    #draw the keypoints

    train_keypoints = cv.drawKeypoints(grayScale,keypoints,None,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    test_keypoints = cv.drawKeypoints(grayScale2,kp2,None,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    #match the keypoints

    bf_object= cv.BFMatcher(cv.NORM_L1,crossCheck=False)

    matches = bf_object.match(descriptors,des2)
    matches= sorted(matches,key=lambda  x : x.distance)

    result = cv.drawMatches(grayScale,keypoints,grayScale2,kp2,matches,grayScale2,flags=2)

    plot.rcParams['figure.figsize'] = [14.0, 7.0]
    plot.title('Best Matching Points')
    plot.imshow(result)
    plot.show()

if __name__ == '__main__':
    main()