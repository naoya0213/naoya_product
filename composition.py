import shutil
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def background_composition(image_path, matte_path, bg_image_path):
  foreground = Image.open(image_path)
  matte = Image.open(matte_path)
  background = Image.open(bg_image_path).resize(foreground.size)
  
  composition_img = Image.composite(foreground, background, matte)
 
  return composition_img
# 