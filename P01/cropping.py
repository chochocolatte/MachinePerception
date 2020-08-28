import cv2 as opencv

def readFile(file_path):
    file = open(file_path, "r")
    content = file.readline().split()
    file.close()

    return content

def main():
    image_name = "prac01ex02img01.png"
    image = opencv.imread("assets\\" + str(image_name))
    file_path = "assets\\prac01ex02crop.txt"
    x_l, y_l, x_r, y_r = readFile(file_path)
    cropped_image = image[int(y_l):int(y_r), int(x_l):int(x_r)]
    opencv.imwrite("resizedAssets\\cropped" + str(image_name), cropped_image)



if __name__ == '__main__':
    main()
