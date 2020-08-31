import numpy as np
import cv2 as cv

np.set_printoptions(linewidth=np.inf)

def main():
    imageName = 'prac04ex02img01.png'
    img = cv.imread("assets\\"+str(imageName),cv.IMREAD_GRAYSCALE)
    img_result = cv.threshold(img,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)[1]
    ret,label = cv.connectedComponents(img_result,connectivity=4)
    img_result=CCL(label)
    MSER(cv.cvtColor(img_result,cv.COLOR_RGB2GRAY))
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

def MSER(image):
    if image is not None:
        (h, w) = image.shape[:2]
        mser = cv.MSER_create()
        mser.setMaxArea(int((h*w)/2))
        mser.setMinArea(10)

        rectangle = mser.detectRegions(image)[1]
        for (x,y,w,h) in rectangle:
            cropped = image[y:y+h,x:x+w]
            cv.imwrite("binary\\"+str(x)+","+str(y)+","+str(w)+","+str(h)+".png",cropped)

def commonHeight(rec):
    result = 0
    i=0
    for height in rec[3]:
        result += height
        i+=1
    average = result/i

if __name__ == '__main__':
    main()