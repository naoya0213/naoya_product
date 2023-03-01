import matplotlib.pyplot as plt
from composition import background_composition as bg_com
from MODNet.demo.image_matting.colab.inference import inference
# input_path = 'modnet_image\input\\22861417_s.jpg'
# bg_path = "modnet_image\\background\\bg.jpg"

def composit(input_path,bg_path):
    inference(input_path)
    matte_path = 'static\modnet_image\matte\matte.png'
    output_path = 'static\modnet_image\output\composit.jpg'
    compos_img = bg_com(input_path, matte_path, bg_path)
    plt.imshow(compos_img)
    plt.show()
    print(input_path, '\n')

    # 合成画像を保存
    compos_img.save((output_path))

composit(R'C:\Users\81907\Desktop\product\static\modnet_image\input\\22861417_s.jpg',R'bg.jpg')
