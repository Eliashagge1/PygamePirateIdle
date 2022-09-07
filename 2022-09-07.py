import pygame, sys, time, math
from pygame import mixer

pygame.init()
mixer.init()

#FPS counter start
def init_screen_and_clock():
    global screen, display, clock
    pygame.init()
    windowSize = (220, 330)
    pygame.display.set_caption('Game')
    screen = pygame.display.set_mode(windowSize, 0, 32)
    clock = pygame.time.Clock()
 
#Fonts
def create_fonts(font_sizes_list):
    #Creates different fonts with one list
    fonts = []
    for size in font_sizes_list:
        fonts.append(
            pygame.font.SysFont("Arial", size))
    return fonts
 
#Render display_fps
def render(fnt, what, color, where):
    #Renders the fonts as passed from display_fps
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)
 
 #Displays FPS
def display_fps():
    #Data that will be rendered and blitted in _display
    render(
        fonts[0],
        what=str(int(clock.get_fps())),
        color="white",
        where=(0, 0))
 
#Init def (8) and creates fonst
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
    display_fps()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop1 = False

        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())

    clock.tick(144) #Fps limit
    pygame.display.flip() #Fps
    window.fill((0, 0, 0)) #Background
    window.blit(scaled_bg, bg_rect) #Background
    pygame.display.flip() #Display update

pygame.quit()
