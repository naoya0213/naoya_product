import shutil
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def background_composition(image_path, matte_path, bg_image_path):
  foreground = Image.open(image_path)
  composition_img = Image.composite(foreground, bg_image_path, matte_path)
 
  return composition_img
# 
