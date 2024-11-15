import os
import shutil


def rename_and_move_images(src_dir, dest_dir, start_index=3986):
    # 确保目标文件夹存在
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

        # 遍历源文件夹中的所有jpg文件
    for filename in os.listdir(src_dir):
        if filename.endswith('.jpg'):
            # 构造源文件路径和目标文件路径
            src_file = os.path.join(src_dir, filename)
            base, _ = os.path.splitext(filename)  # 去掉文件扩展名
            new_filename = f"{start_index:05d}.jpg"  # 生成新的文件名，例如000 401.jpg
            dest_file = os.path.join(dest_dir, new_filename)

            # 复制文件到新位置并重命名
            shutil.copy2(src_file, dest_file)

            # 更新索引值
            start_index += 1

        # 使用示例


source_folder = r'C:\Users\Administrator\Desktop\SubLane\test_video'  # 源文件夹，包含jpg图片
destination_folder = r'C:\Users\Administrator\Desktop\SubLane\test_video'  # 目标文件夹，将保存重新编号的图片
rename_and_move_images(source_folder, destination_folder)