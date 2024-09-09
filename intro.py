import pygame
import os 
current_dir = os.getcwd()
file_name="Intro_audio.mp3"
filepath = os.path.join(current_dir,file_name)
def intro():
    def play_audio(file_path):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    audio_file_path = r"C:\Users\karak\OneDrive\Desktop\JARVIS\Intro_audio.mp3"

    import threading
    audio_thread = threading.Thread(target=play_audio, args=(audio_file_path,))
    audio_thread.start()    