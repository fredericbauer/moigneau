import pygame
import time
import threading

def play_audio(file_path):
	pygame.mixer.init()
	pygame.mixer.music.load(file_path)
	pygame.mixer.music.play()


def play_audio_sync(file_path):
	music_thread = threading.Thread(target=play_audio, args=(file_path,))


	music_thread.start()
	time.sleep(0.1)
	while pygame.mixer.music.get_busy():
		time.sleep(0.1)

 