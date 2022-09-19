import pygame, sys, time, math, FPSdef, pickle
from pygame import mixer
from FPSdef import init_screen_and_clock
from FPSdef import create_fonts
from FPSdef import render
from FPSdef import display_fps

sys.path.append("C:/Users/User/Desktop/PirateIdle_test/FPSdef.py")

pygame.init()
mixer.init()

#Play background music
# mixer.music.load()
# mixer.music.set_volume(0.2)
# mixer.music.play(-1)

#Init def (FPSdef.py) and creates fonst
init_screen_and_clock()
fonts = create_fonts([32, 16, 14, 8])

#Scaling
def transformScaleKeepRatio(image, size):
    iwidth, iheight = image.get_size()
    scale = min(size[0] / iwidth, size[1] / iheight)
    new_size = (round(iwidth * scale), round(iheight * scale))
    scaled_image = pygame.transform.smoothscale(image, new_size)
    image_rect = scaled_image.get_rect(center = (size[0] // 2, size[1] // 2))
    return scaled_image, image_rect

#Display size
window = pygame.display.set_mode((220, 330), pygame.RESIZABLE)
clock = pygame.time.Clock()

#Background images
background = pygame.image.load('Design_Mk1.png').convert_alpha()
scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())
statsScreen = pygame.image.load('Design_Mk1.png').convert_alpha()
scaled_stats, stats_rect = transformScaleKeepRatio(statsScreen, window.get_size())

#Loadingscreen image
loadingScreen1 = pygame.image.load('loading screen 1.png').convert_alpha()
scaled_ls1, ls1_rect = transformScaleKeepRatio(loadingScreen1, window.get_size())
loadingScreen2 = pygame.image.load('loading screen 2.png').convert_alpha()
scaled_ls2, ls2_rect = transformScaleKeepRatio(loadingScreen2, window.get_size())

#Variables
lastTimeDisplayed = 0
balance = 100
incomeStand = 100
timerStand = 60
offlineDevaule = 1/3

sails = 0
sailsCost = 300
sailsStandCost = 300
sailsCostMulti = 1.5
sailsMulti = 1.5
maxSails = 5

crew = 0
crewCost = 20
crewStandCost = 20
crewCostMulti = 1.1
crewMulti = 1.1
crewLifetime = 0
maxCrew = 15

canons = 0
canonsCost = 50
canonsStandCost = 50
canonsCostMulti = 1.2
canonsMulti = 1.25
maxCanons = 15

#For the saving
class MyClass():
    def __init__(self, param):
        self.param = param
def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Failure to save", ex)
def save_saved(obj):
    try:
        with open("saved.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Failure to save", ex)
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Failure to save", ex)

menu = 0
loadingScreenWait = round(time.time()+2)

#Load saved objects
saved = load_object("saved.pickle")
if saved == 1:
    saveList = load_object("data.pickle")
    lastTimeDisplayed = saveList[0]
    sails = saveList[1]
    crew = saveList[2]
    canons = saveList[3]
    balance = saveList[4]
    income = round(incomeStand * (crewMulti ** crew) * (canonsMulti ** canons))
    timerSpeed = round(timerStand / (sailsMulti ** sails))
    timeNow = round(time.time())
    incomePerSec = round(100 * income/timerSpeed)/100
    if (timeNow - lastTimeDisplayed) <= 7200 and lastTimeDisplayed != 0:
        balance = round(balance + ((timeNow - lastTimeDisplayed) * offlineDevaule * incomePerSec))
    elif (timeNow - lastTimeDisplayed) > 7200 and lastTimeDisplayed != 0:
        balance = round(balance + (7200 * offlineDevaule * incomePerSec))
    print(saveList)
    print(incomePerSec)

#Font
smallFont = pygame.font.SysFont('Corbel', 15)
textColour = (100, 100, 100)

screenSizeH = 330
screenDisplaceH = 0
screenSizeW = 220
screenDisplaceW = 0

#Loop 1
loop1 = True
while loop1 == True:
    clock.get_fps()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop1 = False

        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())
            scaled_ls1, ls1_rect = transformScaleKeepRatio(loadingScreen1, window.get_size())
            scaled_ls2, ls2_rect = transformScaleKeepRatio(loadingScreen2, window.get_size())
            if window.get_size()[0]/2 < window.get_size()[1]/3:
                screenSizeH = (window.get_size()[0]/2)*3
                screenDisplaceH = round((window.get_size()[1] - screenSizeH)/2)
                screenDisplaceW = 0
                screenSizeW = window.get_size()[0]
            if window.get_size()[0]/2 > window.get_size()[1]/3:
                screenSizeW = (window.get_size()[1]/3)*2
                screenDisplaceW = round((window.get_size()[0] - screenSizeW)/2)
                screenDisplaceH = 0
                screenSizeH = window.get_size()[1]
            fonts = create_fonts([round(screenSizeW/15)])
            smallFont = pygame.font.SysFont('Corbel', round(screenSizeW/15))


        #Purchase of goods
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if balance > sailsCost and sails < maxSails:
                    balance = balance - round(sailsCost)
                    sails = sails + 1
                    sailsCost = sailsStandCost * (sailsCostMulti ** sails)
                    timerSpeed = round(timerStand / (sailsMulti ** sails))
                    #Printing useful information
                    print("Sails now cost: "+str(round(sailsCost)))
                    print("Number of sails: "+str(sails))
                    print("Timer speed: "+str(timerSpeed))
                    print("Balance: "+str(balance)+"\n")
                elif sails == maxSails:
                    print("You've maxed out on sails!\n")
                else:
                    print("You cant afford this, it costs "+str(round(sailsCost))+", and you only have "+str(balance)+"\n")

            elif event.key == pygame.K_2:
                if balance > crewCost and crew < maxCrew:
                    balance = balance - round(crewCost)
                    crew = crew + 1
                    crewLifetime = crewLifetime + 1
                    crewCost = crewStandCost * (crewCostMulti ** crewLifetime)
                    income = round(incomeStand * (crewMulti ** crew) * (canonsMulti ** canons))
                    #Printing useful information
                    print("Crew now cost: "+str(round(crewCost)))
                    print("Number of crew: "+str(crew))
                    print("Income: "+str(income))
                    print("Balance: "+str(balance)+"\n")
                elif crew == maxCrew:
                    print("You've maxed out on crew!\n")
                else:
                    print("You cant afford this, it costs "+str(round(crewCost))+", and you only have "+str(balance)+"\n")

            elif event.key == pygame.K_3:
                if balance > canonsCost and crew >= 2 and canons < maxCanons:
                    balance = balance - round(canonsCost)
                    crew = crew - 2
                    canons = canons + 1
                    canonsCost = canonsStandCost * (canonsCostMulti ** canons)
                    income = round(incomeStand * (crewMulti ** crew) * (canonsMulti ** canons))
                    #Printing useful information
                    print("Canons now cost: "+str(round(canonsCost)))
                    print("Number of canons: "+str(canons))
                    print("Number of crew: "+str(crew))
                    print("Income: "+str(income))
                    print("Balance: "+str(balance)+"\n")
                elif balance < canonsCost and crew < 2:
                    print("You cant afford this, it costs "+str(round(canonsCost))+", and you only have "+str(balance))
                    print("Also it cost 2 crew, you only have "+str(crew)+"\n")
                elif balance < canonsCost:
                    print("You cant afford this, it costs "+str(round(canonsCost))+", and you only have "+str(balance)+"\n")
                elif crew < 2:
                    print("This costs 2 crew, you only have "+str(crew)+"\n")
                elif canons == maxCanons:
                    print("You've maxed out on canons!\n")

            elif event.key == pygame.K_4:
                print("E Pressed"+"\n")


    #The timer that pays
    income = round(incomeStand * (crewMulti ** crew) * (canonsMulti ** canons))
    timerSpeed = round(timerStand / (sailsMulti ** sails))
    timeNow = round(time.time())
    incomePerSec = round(100 * income/timerSpeed)/100
    if timeNow%timerSpeed == 0 and timeNow != lastTimeDisplayed:
        balance = balance + income
        print("Time right now: "+str(timeNow))
        lastTimeDisplayed = timeNow
        print("Balance: "+str(balance))
        print("Income per second: "+str(incomePerSec)+"\n")

    if loadingScreenWait < timeNow:
        menu = 1

    if menu == 0 and saved != 1:
        window.blit(scaled_ls1, ls1_rect)

    elif menu == 0 and saved == 1:
        window.blit(scaled_ls2, ls2_rect)

    elif menu == 1:
        window.blit(scaled_bg, bg_rect)

        balancePosition = (screenDisplaceW + screenSizeW/3, screenDisplaceH + screenSizeH/5)
        if 1000000 > balance >= 1000:
            textBalance = smallFont.render((str(round(balance/1000))+"K"), True, textColour)
            window.blit(textBalance, balancePosition)
        elif balance >= 1000000:
            textBalance = smallFont.render((str(round(balance/1000000))+"M"), True, textColour)
            window.blit(textBalance, balancePosition)
        else:
            textBalance = smallFont.render((str(balance)), True, textColour)
            window.blit(textBalance, balancePosition)

    elif menu == 2:
        window.blit(scaled_stats, stats_rect)

    pygame.display.flip() #Display update

#Save data
saved = 1
saveList = [lastTimeDisplayed, sails, crew, canons, balance]
save_object(saveList)
save_saved(saved)

pygame.quit()
