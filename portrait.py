from PIL import Image
import matplotlib.pyplot as plt
from composition import background_composition as bg_com
from inference import inference
def portrait(input_path):
  # input_path = 'modnet_image\input\\22861417_s.jpg'
  inference(input_path)
  matte_path = 'static\modnet_image\matte\matte.jpg'
  # output_path = 'static\modnet_image\output\portrait.jpg'
  bg_path = "static\modnet_image\\background\\bg.jpg"
  im = Image.open(input_path)
  img = Image.new("RGB", (im.size), (255, 255, 255))
  img.save(bg_path)
  portrait_img = bg_com(input_path, matte_path, bg_path)
    # 合成画像を保存
 
  return portrait_img


