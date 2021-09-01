import time
import pygame

pygame.mixer.init()


hit = pygame.mixer.Sound('Turtle/sounds/hit.mp3')
hit.play()
time.sleep(2)

print(type(hit))