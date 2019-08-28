background_image_filename = 'main\\resource\\com\\ftd\\wow\\pic\\wow-classic-740x370.jpg'
 
import pygame
from pygame.locals import *
from sys import exit
 
SCREEN_SIZE = (640, 480)
my_font = pygame.font.Font("my_font.ttf", 16)
text_surface = my_font.render("Pygame is cool!", True, (0,0,0), (255, 255, 255))
 
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

background = pygame.image.load(background_image_filename).convert()
 
Fullscreen = False
 
while True:

    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("Window resized to "+str(event.size))

    screen_width, screen_height = SCREEN_SIZE
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))

    pygame.display.update()