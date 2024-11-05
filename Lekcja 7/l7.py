import cv2

def show_image(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def read_image_cv(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    print(img)
    print(img.shape)
    print(type(img))
    #show_image(img)
    return img

image = read_image_cv("image.jpg")

#show_image(cv2.flip(image,0))


show_image(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))