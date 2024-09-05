from moviepy.editor import VideoFileClip

def separate_audio_video(video_path, output_audio_path, output_video_path):

    video_clip = VideoFileClip(video_path)

  
    audio_clip = video_clip.audio
    video_clip_without_audio = video_clip.set_audio(None)

    
    audio_clip.write_audiofile(output_audio_path)
    video_clip_without_audio.write_videofile(output_video_path)

    
    audio_clip.close()
    video_clip_without_audio.close()


video_path = input("Enter the Clip : ")
output_audio_path = "Output_audio.wav"
output_video_path = "Output_video_without_audio.mp4"

separate_audio_video(video_path, output_audio_path, output_video_path)