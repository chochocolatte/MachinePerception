import numpy as np
import cv2 as cv

def main():
    imageName = 'prac04ex02img01.png'
    img = cv.imread("assets\\"+str(imageName),cv.IMREAD_GRAYSCALE)
    otsu_threshold,img_result = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    num_labels, label = cv.connectedComponents(img_result)
    img_result=CCL(label)
    cv.imshow(None,img_result)
    cv.waitKey()
    return 0

def CCL(labels):
    image_hue = np.uint8(179*labels/np.max(labels))
    blank_channel = 255*np.ones_like(image_hue)
    labeled_img = cv.merge([image_hue,blank_channel,blank_channel])

    labeled_img = cv.cvtColor(labeled_img,cv.COLOR_HSV2BGR)

    labeled_img[image_hue==0]=0

    return labeled_img


if __name__ == '__main__':
    main()