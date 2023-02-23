import human

img_fin = human.remove_bg(    
    path = r"C:\Users\81907\Desktop\product\sample_images\20220211_184060.jpg",
    BLUR = 21,
    CANNY_THRESH_1 = 5,
    CANNY_THRESH_2 = 200,
    MASK_DILATE_ITER = 10,
    MASK_ERODE_ITER = 10,
    MASK_COLOR = (0.0,0.0,1.0),
)