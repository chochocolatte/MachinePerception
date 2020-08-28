import cv2 as cv
import numpy as np

from matplotlib import pyplot as plot

def main():
    color = ('b','g','r')
    for x in range(1,6):
        imagename = "prac01ex01img0"+str(x)+".png"
        image = cv.imread('assets\\'+str(imagename))
        (h,w,d) = image.shape
        print(imagename + " width:" + str(w) + ","+ " height:" + str(h))
        cv.imshow("Image0"+str(x),image)

        for y, col in enumerate(color):
            plot.hist(image[:,:,y].reshape(-1),10,color=col)
            plot.title("Histogram for"+str(imagename)+" Channel:"+str(col))
            plot.xlabel("Pixel value.")
            plot.ylabel("Number of pixels.")
            plot.show()
        cv.waitKey(0)

        #scaling
        scale = 0.5
        n_height = int(scale * h)
        n_width = int(scale * w)

        resized = cv.resize(image,(n_width,n_height))
        cv.imwrite("resizedAssets\\Resized"+str(imagename)+".png",resized)


if __name__ == '__main__':
    main()