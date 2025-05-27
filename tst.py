import pygame

pygame.mixer.init()
pygame.init()

my_sound = pygame.mixer.Sound('tst.wav')
my_sound.play()

# Keep the program alive long enough to hear the sound
import time
time.sleep(5)
