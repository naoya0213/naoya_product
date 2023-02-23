import fusion
import human
import matplotlib.pyplot as plt

img_fin = human.remove_bg(    
    path = r"C:\Users\naoya\Desktop\product\22861417_s.jpg",
    BLUR = 21,
    CANNY_THRESH_1 = 5,
    CANNY_THRESH_2 = 200,
    MASK_DILATE_ITER = 10,
    MASK_ERODE_ITER = 10,
    MASK_COLOR = (0.0,0.0,1.0),
)
image=fusion.fusion(
    human=img_fin,
    bg=r"bg.jpg"
)
plt.imshow(img_fin)
plt.show()