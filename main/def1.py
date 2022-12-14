import pygame, sys, time
pygame.init()


# FPS counter start
def init_screen_and_clock():
    global screen, display, clock
    pygame.init()
    windowSize = (220, 330)
    pygame.display.set_caption('Game')
    screen = pygame.display.set_mode(windowSize, 0, 32)
    clock = pygame.time.Clock()


# Fonts
def create_fonts(font_sizes_list):
    # Creates different fonts with one list
    fonts = []
    for size in font_sizes_list:
        fonts.append(
            pygame.font.SysFont("Arial", size))
    return fonts


# Render display_fps
def render(fnt, what, color, where):
    # Renders the fonts as passed from display_fps
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)


# Init def (8) and creates fonts
init_screen_and_clock()
fonts = create_fonts([32, 16, 14, 11, 8])


# Scaling
def transformScaleKeepRatio(image, size):
    iwidth, iheight = image.get_size()
    scale = min(size[0] / iwidth, size[1] / iheight)
    new_size = (round(iwidth * scale), round(iheight * scale))
    scaled_image = pygame.transform.smoothscale(image, new_size)
    image_rect = scaled_image.get_rect(center = (size[0] // 2, size[1] // 2))
    return scaled_image, image_rect
