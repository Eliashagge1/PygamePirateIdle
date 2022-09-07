import pygame, sys, time, math, FPSdef
from pygame import mixer
from FPSdef import init_screen_and_clock
from FPSdef import create_fonts
from FPSdef import render
from FPSdef import display_fps

sys.path.append("C:/Users/User/Desktop/PirateIdle_test/FPSdev f.py")

pygame.init()
mixer.init()


#Init def (FPSdef.py) and creates fonst
init_screen_and_clock()
fonts = create_fonts([32, 16, 14, 8])


#Scaling
def transformScaleKeepRatio(image, size):
    iwidth, iheight = image.get_size()
    scale = min(size[0] / iwidth, size[1] / iheight)
    #scale = max(size[0] / iwidth, size[1] / iheight)
    new_size = (round(iwidth * scale), round(iheight * scale))
    scaled_image = pygame.transform.smoothscale(image, new_size) 
    image_rect = scaled_image.get_rect(center = (size[0] // 2, size[1] // 2))
    return scaled_image, image_rect

#Display size
window = pygame.display.set_mode((220, 330), pygame.RESIZABLE)
clock = pygame.time.Clock()

#Background image
background = pygame.image.load('Design_Mk1.png').convert_alpha()
scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())

#Loop 1
loop1 = True
while loop1 == True:
    clock.tick(100)
    background #Reload Background
    FPSdef.display_fps()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop1 = False

        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())

    clock.tick(144) #Fps limit
    pygame.display.flip() #Fps update
    window.fill((0, 0, 0)) #Background
    window.blit(scaled_bg, bg_rect) #Background
    pygame.display.flip() #Display update

pygame.quit()
