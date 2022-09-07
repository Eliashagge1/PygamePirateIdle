import pygame, sys, time

#Init def (8) and creates fonst



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

init_screen_and_clock()
fonts = create_fonts([32, 16, 14, 8])
