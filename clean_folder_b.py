import os
import shutil

background_folder = 'modnet_image\\background'
if os.path.exists(background_folder):
  shutil.rmtree(background_folder)
os.makedirs(background_folder)