import os
import shutil

input_folder = 'modnet_image\input'
if os.path.exists(input_folder):
  shutil.rmtree(input_folder)
os.makedirs(input_folder)
 
output_folder = 'modnet_image\output'
if os.path.exists(output_folder):
  shutil.rmtree(output_folder)
os.makedirs(output_folder)
 
