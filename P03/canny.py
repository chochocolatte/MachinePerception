import cv2 as cv


def main():
    imageList = ["prac03ex01img01.png", "prac03ex01img02.png", "prac03ex01img03.png","prac03ex02img01.jpg"]
    for x,imageName in enumerate(imageList):
        image = cv.imread("assets\\"+imageName)
        edges = cv.Canny(image,100,200)
        cv.imshow(None,edges)
        cv.waitKey(0)

if __name__ == '__main__':
    main()