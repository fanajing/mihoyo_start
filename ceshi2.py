from PIL import Image
import shutil
import os

def filter_and_copy_images_by_size(source_folder, target_folder, target_width, target_height):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            image_path = os.path.join(source_folder, filename)
            image = Image.open(image_path)
            width, height = image.size
            if width == target_width and height == target_height:
                shutil.copy(image_path, target_folder)

source_folder = "C:/Users/梵阿景/Desktop/1"  # 替换为实际的图片文件夹路径
target_folder ="C:/Users/梵阿景/Desktop/2"  # 替换为实际的目标文件夹路径
target_width = 2560  # 替换为目标宽度
target_height = 1440  # 替换为目标高度

filter_and_copy_images_by_size(source_folder, target_folder, target_width, target_height)