import os
import shutil

def move_and_rename_files(src_folder, dest_folder):
    # 确保目标文件夹存在，如果不存在则创建
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(src_folder):
        # 构建源文件的完整路径
        current_path = os.path.join(src_folder, filename)

        # 检查是否是文件（而非目录）
        if os.path.isfile(current_path):
            # 构建新的文件名
            new_filename = filename + '.png'
            new_path = os.path.join(dest_folder, new_filename)

            # 移动并重命名文件到目标文件夹
            shutil.move(current_path, new_path)

    print(f"所有文件已移动到 {dest_folder} 并添加 .png 扩展名")

if __name__ == '__main__':
    # 替换为你的源文件夹和目标文件夹路径
    src_folder = r"C:\Users\梵阿景\AppData\Roaming\miHoYo\HYP\1_1\fedata\Cache\Cache_Data"  # 更改为源文件夹路径
    dest_folder = r"C:\Users\梵阿景\Desktop\2"  # 更改为目标文件夹路径

    move_and_rename_files(src_folder, dest_folder)