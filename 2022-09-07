import pygame, sys, time, math
from pygame import mixer

pygame.init()
mixer.init()


def transformScaleKeepRatio(image, size):
    iwidth, iheight = image.get_size()
    scale = min(size[0] / iwidth, size[1] / iheight)
    #scale = max(size[0] / iwidth, size[1] / iheight)
    new_size = (round(iwidth * scale), round(iheight * scale))
    scaled_image = pygame.transform.smoothscale(image, new_size) 
    image_rect = scaled_image.get_rect(center = (size[0] // 2, size[1] // 2))
    return scaled_image, image_rect

pygame.init()
window = pygame.display.set_mode((220, 330), pygame.RESIZABLE)
clock = pygame.time.Clock()

background = pygame.image.load('Design_Mk1.png').convert_alpha()
scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())

run = True
while run == True:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())

    window.fill((127, 127, 127))
    window.blit(scaled_bg, bg_rect)
    pygame.display.flip()

pygame.quit()
