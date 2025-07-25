import cv2
import pygame
import time

pygame.init()
pygame.mixer.init()




pygame.mixer.music.load("C:/Users/LassePedersen/Documents/GitHub/RatClock/Alarm_tones/1.mp3")
pygame.mixer.music.play()

time.sleep(15)  # Wait while the music plays (adjust as needed)
pygame.mixer.music.stop()


