from moviepy.editor import VideoFileClip
from PIL import Image
import os


def extract_frames(video_path, output_folder, every_n_seconds=1, start_time=0):    ###每隔every_n_seconds秒提取一帧###
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    clip = VideoFileClip(video_path)
    frame_count = 1
    current_time = start_time
    duration = clip.duration

    while current_time < duration:
        frame = clip.get_frame(current_time)
        filename = os.path.join(output_folder, f"{'%05d' % frame_count}.jpg")
        image = Image.fromarray(frame)  # 将NumPy数组转换为PIL Image对象
        image.save(filename)  # 使用PIL Image对象的save方法保存图片
        frame_count += 1
        current_time += every_n_seconds

    clip.close()

# 使用示例
video_path = r'C:\Users\Administrator\Desktop\SubLane\test_video\009.mp4'  # 替换为你的视频文件路径
output_folder = r'C:\Users\Administrator\Desktop\SubLane\test_video\333'  # 提取的图片将保存在这个文件夹中
extract_frames(video_path, output_folder)

#----------------------------------------------------------------------------------------#
#这段代码将从video_path指定的MP4视频中每隔every_n_seconds秒提取一帧，
#并将这些帧保存为JPG图片在output_folder指定的文件夹中。文件名将从00001.jpg开始递增。593  3985

#注意：如果你想要从视频的特定时间点开始提取帧，
#可以修改start_time参数（默认为0，表示从视频开始处提取）。
#时间单位是秒。例如，如果你想从视频的第5秒开始提取帧，可以将start_time设置为5。
#----------------------------------------------------------------------------------------#