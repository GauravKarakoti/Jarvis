import pygame

def jarvis_intro():
    pygame.mixer.init()


    audio_file_path = r"Intro_audio.mp3"


    pygame.mixer.music.load(audio_file_path)


    pygame.mixer.music.play()


    while pygame.mixer.music.get_busy():  
        pygame.time.Clock().tick(10)