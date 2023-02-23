import shutil
def copy_image(image_path):
    shutil.copy(image_path, 'modnet_image\input')

copy_image('sample_images\\22861417_s.jpg')