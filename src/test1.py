import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant

screen = pygame.display.set_mode((640,480))
img = pygame.image.load(Materials_Constant.background_Molten_Core_filename)

for opacity in range(255, 0, -15):
    work_img = img.copy()
    pygame.draw.rect(work_img, (255,0, 0, opacity),  (0,0, 640,480))
    screen.blit(work_img, (0,0))
    pygame.display.flip()
    pygame.time.delay(100)