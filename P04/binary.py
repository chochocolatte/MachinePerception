import numpy as np
import cv2 as cv

np.set_printoptions(linewidth=np.inf)

def main():
    imageName = 'prac04ex02img01.png'
    img = cv.imread("assets\\"+str(imageName),cv.IMREAD_GRAYSCALE)
    img_result = cv.threshold(img,0,255,cv.THRESH_OTSU)[1]
    output= cv.connectedComponentsWithStats(img_result, cv.CV_32S,connectivity=8)
    #connectedComponents returns:
    #1 - the number of label
    #2 - labels matrix
    #where as connected components with stats returns
    #1 - number of labels
    #2 - labels matrix
    #3 - stats matrix
    #4 - centroid matrix
    img_result=CCL(output[1])
    contours(cv.cvtColor(img_result,cv.COLOR_BGR2GRAY),img_result.copy())
    return 0

def CCL(labels):
    image_hue = np.uint8(179*labels/np.max(labels))
    blank_channel = 255*np.ones_like(image_hue)
    labeled_img = cv.merge([image_hue,blank_channel,blank_channel])

    labeled_img = cv.cvtColor(labeled_img,cv.COLOR_HSV2BGR)

    labeled_img[image_hue==0]=0

    return labeled_img

def contours(image,oriimage):

    con,hier= cv.findContours(image,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2:]
    index=1

    for i in con:
        x,y,w,h = cv.boundingRect(i)
        cv.rectangle(image, (x, y), (x + w, y + h), (7, 0, 255), 2)
        ROI = oriimage[y:y+h,x:x+w]
        cv.imwrite("binary\\"+str(index)+".png",ROI)
        index+=1
    cv.imshow('image', image)
    cv.waitKey()


if __name__ == '__main__':
    main()