import cv2

def fusion(human, bg, out='new.jpg', top=0, left=0):
    img1 = human
    img2 = cv2.imread(bg)

    height, width = img1.shape[:2]
    img2[top:height + top, left:width + left] = img1

    cv2.imwrite(out, img2)
    return img2


