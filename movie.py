from moviepy.editor import VideoFileClip
import os 
current_dir = os.getcwd()
intro_name="Intro.mp4"
intro_path = os.path.join(current_dir,intro_name)
def j():
    video_file =intro_path

    video_clip = VideoFileClip(video_file)

    video_clip.preview()

    video_clip.close()