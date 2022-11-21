# Imports and initiations
import pickle
import os
from pygame import mixer
from def1 import *

startTime = round(time.time())
timeStartSec = 0
timeStartMin = 0

direct1 = os.getcwd()
sys.path.append(str(direct1)+"/def1.py")

pygame.init()
mixer.init()


# Init def (def1.py) and creates fonts
init_screen_and_clock()


# Display size
screen = [220, 330]
setScreenSize = screen
clock = pygame.time.Clock()


# Variables
lastTimeDisplayed = 0
balance = 100
incomeStand = 100
timerStand = 60
offlineDevaule = 1/3

# Sails
sails1 = 0
sailsCost1 = 300
sailsStandCost1 = 300
sailsCostMulti1 = 1.5
sailsMulti1 = 1.2
maxSails1 = 10

# Crew
crew1 = 0
crewCost1 = 20
crewStandCost1 = 20
crewCostMulti1 = 1.1
crewMulti1 = 1.1
crewLifetime1 = 0
maxCrew1 = 20

# Canons
canons1 = 0
canonsCost1 = 50
canonsStandCost1 = 50
canonsCostMulti1 = 1.2
canonsMulti1 = 1.25
maxCanons1 = 20

# Captain
captain1 = 0
captainEarn1 = 2500
captainCost1 = 20000

# Volume
standardVolume = 0.2
musicVolume = standardVolume
SFXVolume = standardVolume

# Dictionary
mainDictionary = {}

# Songs
song1 = "sound/song1.wav"
song2 = "sound/song2.wav"
song3 = "sound/song3.wav"


# Playlist
playlist = list()
playlist.append(song3)
playlist.append(song2)
playlist.append(song1)

# Sound
mixer.music.load(playlist.pop())
mixer.music.queue(playlist.pop())
mixer.music.set_endevent(pygame.USEREVENT)
mixer.music.set_volume(musicVolume)
mixer.music.play()
mixer.music.unpause()

# Text colour
textColour = (50, 50, 50)

# Volume slider
sliderPos = musicVolume
slider2Pos = SFXVolume


def ship(x, y, z):
    f = "ship"+str(x)
    if f in mainDictionary:
        mainDictionary[f][y] = mainDictionary[f].get(y) + int(z)

    else:
        mainDictionary[f] = {
            "sails"+str(x): 0,
            "sailsCost"+str(x): 300,
            "sailsStandCost"+str(x): 300 * 1.5 ** x,
            "sailsCostMulti"+str(x): 1.5,
            "sailsMulti"+str(x): 1.2,
            "maxSails"+str(x): 10,

            "crew"+str(x): 0,
            "crewCost"+str(x): 20,
            "crewStandCost"+str(x): 20 * 1.5 ** x,
            "crewCostMulti"+str(x): 1.1,
            "crewMulti"+str(x): 1.1,
            "crewLifetime"+str(x): 0,
            "maxCrew"+str(x): 20,

            "canons"+str(x): 0,
            "canonsCost"+str(x): 50,
            "canonsStandCost"+str(x): 50 * 1.5 ** x,
            "canonsCostMulti"+str(x): 1.2,
            "canonsMulti"+str(x): 1.25,
            "maxCanons"+str(x): 20,

            "captain"+str(x): 0,
            "captainEarn"+str(x): 500,
            "captainCost"+str(x): 20000
        }
        globals().update(mainDictionary)
        globals().update(mainDictionary[f])
        mainDictionary[f][y] = mainDictionary[f].get(y) + int(z)

    globals().update(mainDictionary)
    globals().update(mainDictionary[f])


def shipMenu(x):
    ship(x, "crew"+str(x), 0)
    globals().update(mainDictionary["ship"+str(x)])
    global balance
    global income
    global timerSpeed

    if screenDisplaceW + screen[0]/1.95 <= mouse[0] <= screenDisplaceW + screen[0]/1.02 and \
            screenDisplaceH + screen[1]/3.3 <= mouse[1] <= screenDisplaceH + screen[1]/2.5:
        if balance > round(mainDictionary["ship" + str(x)].get("crewCost" + str(x))) and \
                mainDictionary["ship" + str(x)].get("crew" + str(x)) < mainDictionary["ship" + str(x)].get("maxCrew" + str(x)):
            balance = balance - round(mainDictionary["ship" + str(x)].get("crewCost" + str(x)))
            ship(x, "crew"+str(x), 1)
            ship(x, "crewLifetime"+str(x), 1)
            mainDictionary["ship" + str(x)]["crewCost" + str(x)] = mainDictionary["ship" + str(x)].get("crewStandCost" + str(x)) * (mainDictionary["ship" + str(x)].get("crewCostMulti" + str(x)) ** mainDictionary["ship" + str(x)].get("crewLifetime" + str(x)))
            income = incomeFunction()
            buttonPress.play()
        elif mainDictionary["ship" + str(x)].get("crew" + str(x)) == mainDictionary["ship" + str(x)].get("maxCrew" + str(x)):
            print("Golden button sound\n")
        else:
            print("Angry button sound\n")

    if screenDisplaceW + screen[0]/1.95 <= mouse[0] <= screenDisplaceW + screen[0]/1.02 and \
            screenDisplaceH + screen[1]/2.4 <= mouse[1] <= screenDisplaceH + screen[1]/1.94:
        if balance > round(mainDictionary["ship" + str(x)].get("sailsCost" + str(x))) and \
                mainDictionary["ship" + str(x)].get("sails" + str(x)) < mainDictionary["ship" + str(x)].get("maxSails" + str(x)):
            balance = balance - round(mainDictionary["ship" + str(x)].get("sailsCost" + str(x)))
            ship(x, "sails"+str(x), 1)
            mainDictionary["ship" + str(x)]["sailsCost" + str(x)] = mainDictionary["ship" + str(x)].get("sailsStandCost" + str(x)) * (mainDictionary["ship" + str(x)].get("sailsCostMulti" + str(x)) ** mainDictionary["ship" + str(x)].get("sails" + str(x)))
            timerSpeed = timerSpeedFunction()
            buttonPress.play()
        elif mainDictionary["ship" + str(x)].get("sails" + str(x)) == mainDictionary["ship" + str(x)].get("maxSails" + str(x)):
            print("Golden button sounds\n")
        else:
            print("Angry button sound\n")

    if screenDisplaceW + screen[0]/1.95 <= mouse[0] <= screenDisplaceW + screen[0]/1.02 and \
            screenDisplaceH + screen[1]/1.875 <= mouse[1] <= screenDisplaceH + screen[1]/1.45:
        if balance > round(mainDictionary["ship" + str(x)].get("canonsCost" + str(x))) and\
                mainDictionary["ship" + str(x)].get("crew" + str(x)) >= 2 and \
                mainDictionary["ship" + str(x)].get("canons" + str(x)) < mainDictionary["ship" + str(x)].get("maxCanons" + str(x)):
            balance = balance - round(mainDictionary["ship" + str(x)].get("canonsCost" + str(x)))
            ship(x, "crew"+str(x), -2)
            ship(x, "canons"+str(x), 1)
            mainDictionary["ship" + str(x)]["canonsCost" + str(x)] = mainDictionary["ship" + str(x)].get("canonsStandCost" + str(x)) * (mainDictionary["ship" + str(x)].get("canonsCostMulti" + str(x)) ** mainDictionary["ship" + str(x)].get("canons" + str(x)))
            buttonPress.play()
        elif mainDictionary["ship" + str(x)].get("canons" + str(x)) == mainDictionary["ship" + str(x)].get("maxCanons" + str(x)):
            print("Golden button sound\n")
        else:
            print("Angry button sound\n")

    if screenDisplaceW + screen[0]/1.95 <= mouse[0] <= screenDisplaceW + screen[0]/1.02 and \
            screenDisplaceH + screen[1]/1.42 <= mouse[1] <= screenDisplaceH + screen[1]/1.16:
        if balance >= round(mainDictionary["ship" + str(x)].get("captainCost" + str(x))) and \
                mainDictionary["ship" + str(x)].get("crew" + str(x)) == mainDictionary["ship" + str(x)].get("maxCrew" + str(x)) and \
                mainDictionary["ship" + str(x)].get("canons" + str(x)) == mainDictionary["ship" + str(x)].get("maxCanons" + str(x)) and \
                mainDictionary["ship" + str(x)].get("sails" + str(x)) == mainDictionary["ship" + str(x)].get("maxSails" + str(x)) and \
                mainDictionary["ship" + str(x)].get("captain" + str(x)) < 1:
            balance = balance - mainDictionary["ship" + str(x)].get("captainCost" + str(x))
            mainDictionary["ship" + str(x)]["captain" + str(x)] = 1
            buttonPress.play()
        elif mainDictionary["ship" + str(x)].get("captain" + str(x)) != 0:
            print("Golden button sound\n")
        else:
            print("Angry button sound\n")


def shipGraphics(x):
    crewShip1Position = (screenDisplaceW + screen[0]/3.3, screenDisplaceH + screen[1]/3.25)
    textCrewShip1 = mediumFont.render(str(mainDictionary["ship" + str(x)].get("crew" + str(x))), True, textColour)
    window.blit(textCrewShip1, crewShip1Position)
    crewShip1CostPosition = (screenDisplaceW + screen[0]/1.75, screenDisplaceH + screen[1]/3.25)
    if mainDictionary["ship" + str(x)].get("crew" + str(x)) >= mainDictionary["ship" + str(x)].get("maxCrew" + str(x)):
        textCrewShip1Cost = mediumFont.render("Max", True, textColour)
    elif mainDictionary["ship" + str(x)].get("crewCost" + str(x)) < 1000:
        textCrewShip1Cost = mediumFont.render(str(round(mainDictionary["ship" + str(x)].get("crewCost" + str(x)))), True, textColour)
    else:
        textCrewShip1Cost = mediumFont.render(str(round(mainDictionary["ship" + str(x)].get("crewCost" + str(x)) / 1000)) + "K", True, textColour)
    window.blit(textCrewShip1Cost, crewShip1CostPosition)

    sailsShip1Position = (screenDisplaceW + screen[0]/3.3, screenDisplaceH + screen[1]/2.4)
    textSailsShip1 = mediumFont.render(str(mainDictionary["ship" + str(x)].get("sails" + str(x))), True, textColour)
    window.blit(textSailsShip1, sailsShip1Position)
    sailsShip1CostPosition = (screenDisplaceW + screen[0]/1.75, screenDisplaceH + screen[1]/2.4)
    if mainDictionary["ship" + str(x)].get("sails" + str(x)) >= mainDictionary["ship" + str(x)].get("maxSails" + str(x)):
        textSailsShip1Cost = mediumFont.render("Max", True, textColour)
    elif mainDictionary["ship" + str(x)].get("sailsCost" + str(x)) < 1000:
        textSailsShip1Cost = mediumFont.render(str(round(mainDictionary["ship" + str(x)].get("sailsCost" + str(x)))), True, textColour)
    else:
        textSailsShip1Cost = mediumFont.render(str(round(mainDictionary["ship" + str(x)].get("sailsCost" + str(x)) / 1000)) + "K", True, textColour)
    window.blit(textSailsShip1Cost, sailsShip1CostPosition)

    canonsShip1Position = (screenDisplaceW + screen[0]/30, screenDisplaceH + screen[1]/1.7)
    textCanonsShip1 = mediumFont.render(str(mainDictionary["ship" + str(x)].get("canons" + str(x))), True, textColour)
    window.blit(textCanonsShip1, canonsShip1Position)
    canonsShip1CostPosition = (screenDisplaceW + screen[0]/1.75, screenDisplaceH + screen[1]/1.85)
    if mainDictionary["ship" + str(x)].get("canons" + str(x)) >= mainDictionary["ship" + str(x)].get("maxCanons" + str(x)):
        textCanonsShip1Cost = mediumFont.render("Max", True, textColour)
    elif mainDictionary["ship" + str(x)].get("canonsCost" + str(x)) < 1000:
        textCanonsShip1Cost = mediumFont.render(str(round(mainDictionary["ship" + str(x)].get("canonsCost" + str(x)))), True, textColour)
    else:
        textCanonsShip1Cost = mediumFont.render(str(round(mainDictionary["ship" + str(x)].get("canonsCost" + str(x)) / 1000)) + "K", True, textColour)
    window.blit(textCanonsShip1Cost, canonsShip1CostPosition)

    captain1Position = (screenDisplaceW + screen[0]/30, screenDisplaceH + screen[1]/1.3)
    if mainDictionary["ship" + str(x)].get("captain" + str(x)) >= 1:
        textCaptain1 = mediumFont.render("Yes", True, textColour)
    else:
        textCaptain1 = mediumFont.render("No", True, textColour)
    window.blit(textCaptain1, captain1Position)
    globals().update()


# For the saving
class MyClass:
    def __init__(self, param):
        self.param = param


def save_object(obj):
    try:
        with open("savefiles/data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Failure to save", ex)


def save_saved(obj):
    try:
        with open("savefiles/saved.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Failure to save", ex)


def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Failure to save", ex)


# Income
def incomeFunction():
    shipList = []
    incomeList = []
    innerIncome = 0
    for i in mainDictionary:
        shipList.append(i)
    for i in range(1, 10):
        if "ship"+str(i) in shipList:
            incomeList.append(
                (mainDictionary["ship"+str(i)].get("crewMulti"+str(i)) **
                 mainDictionary["ship"+str(i)].get("crew"+str(i))) *
                (mainDictionary["ship"+str(i)].get("canonsMulti"+str(i)) **
                 mainDictionary["ship"+str(i)].get("canons"+str(i))) +
                mainDictionary["ship"+str(i)].get("captainEarn"+str(i)) *
                mainDictionary["ship"+str(i)].get("captain"+str(i)) *
                i
                          )
    for i in range(1, incomeList.__len__()+1):
        innerIncome = innerIncome + incomeList[i-1]
    innerIncome = innerIncome * incomeStand
    return round(innerIncome)


# Timer speed
def timerSpeedFunction():
    global timerStand
    timerList = [1]
    innerTimer = 0
    for i in range(1, 10):
        ship(i, "crew"+str(i), 0)
        if (mainDictionary["ship"+str(i)].get("sails"+str(i))) != 0:
            timerList.append(
                (mainDictionary["ship"+str(i)].get("sailsMulti"+str(i)) **
                 mainDictionary["ship"+str(i)].get("sails"+str(i)))
                          )
        else:
            timerList.append(0)
    for i in range(0, timerList.__len__()):
        innerTimer = innerTimer + timerList[i-1]
    timerReturnSpeed = timerStand / innerTimer
    return round(timerReturnSpeed)


# Start loading-screen
menu = 0
loadingScreenWait = round(time.time()+2)


# Load saved objects
saved = load_object("savefiles/saved.pickle")
if saved == 1:
    saveList = load_object("savefiles/data.pickle")
    globals().update(saveList)
    globals().update(mainDictionary)
    screen = setScreenSize
    income = incomeFunction()
    timerSpeed = timerSpeedFunction()
    timeNow = round(time.time())
    incomePerSec = round(100 * income/timerSpeed)/100
    if (timeNow - lastTimeDisplayed) <= 7200 and lastTimeDisplayed != 0:
        balance = round(balance + ((timeNow - lastTimeDisplayed) * offlineDevaule * incomePerSec))
    elif (timeNow - lastTimeDisplayed) > 7200 and lastTimeDisplayed != 0:
        balance = round(balance + (7200 * offlineDevaule * incomePerSec))
    print(saveList)


# Create window
window = pygame.display.set_mode(screen, pygame.RESIZABLE)


# Background images
background = pygame.image.load('pictures/Design_Mk1.png').convert_alpha()
scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())
statsScreen = pygame.image.load('pictures/Stats.png').convert_alpha()
scaled_stats, stats_rect = transformScaleKeepRatio(statsScreen, window.get_size())
ship1Upgrade = pygame.image.load('pictures/Ship1Upgrade.png').convert_alpha()
scaled_ship1Upgrade, ship1Upgrade_rect = transformScaleKeepRatio(ship1Upgrade, window.get_size())
settingsScreen = pygame.image.load('pictures/Settings.png').convert_alpha()
scaled_settings, settings_rect = transformScaleKeepRatio(settingsScreen, window.get_size())


# Loading-screen image
loadingScreen1 = pygame.image.load('pictures/loading screen 1.png').convert_alpha()
scaled_ls1, ls1_rect = transformScaleKeepRatio(loadingScreen1, window.get_size())
loadingScreen2 = pygame.image.load('pictures/loading screen 2.png').convert_alpha()
scaled_ls2, ls2_rect = transformScaleKeepRatio(loadingScreen2, window.get_size())





buttonPress = mixer.Sound("sound/buttonPress.mp3")
mixer.Sound.set_volume(buttonPress, SFXVolume)


# Icon and the name of the game
pygame.display.set_caption("Pirate Idle")
icon = pygame.image.load("pictures/IJ.png")
pygame.display.set_icon(icon)


if saved == 1:
    height = screen[1]
    width = screen[0]
else:
    height = 330
    width = 220
screenDisplaceW = 0
screenDisplaceH = 0


ship(1, "crew1", 0)
wasd = 0
# Loop 1
loop1 = True
while loop1:

    # Fonts
    fonts = create_fonts([round(width / 15)])
    smallFont = pygame.font.SysFont('Corbel', round(height / 22))
    mediumFont = pygame.font.SysFont('Corbel', round(height / 11))
    largeFont = pygame.font.SysFont('Corbel', round(height / 5.5))

    clock.get_fps()
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop1 = False

        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())
            scaled_stats, stats_rect = transformScaleKeepRatio(statsScreen, window.get_size())
            scaled_ls1, ls1_rect = transformScaleKeepRatio(loadingScreen1, window.get_size())
            scaled_ls2, ls2_rect = transformScaleKeepRatio(loadingScreen2, window.get_size())
            scaled_ship1Upgrade, ship1Upgrade_rect = transformScaleKeepRatio(ship1Upgrade, window.get_size())
            scaled_settings, settings_rect = transformScaleKeepRatio(settingsScreen, window.get_size())
            if window.get_size()[0]/2 < window.get_size()[1]/3:
                height = (window.get_size()[0] / 2) * 3
                screenDisplaceH = round((window.get_size()[1] - height) / 2)
                screenDisplaceW = 0
                width = window.get_size()[0]
            if window.get_size()[0]/2 > window.get_size()[1]/3:
                width = (window.get_size()[1] / 3) * 2
                screenDisplaceW = round((window.get_size()[0] - width) / 2)
                screenDisplaceH = 0
                height = window.get_size()[1]
            screen = [width, height]

            fonts = create_fonts([round(width / 15)])
            smallFont = pygame.font.SysFont('Corbel', round(height / 22))
            mediumFont = pygame.font.SysFont('Corbel', round(height / 11))
            largeFont = pygame.font.SysFont('Corbel', round(height / 5.5))

        if event.type == pygame.USEREVENT:
            if len(playlist) > 0:
                mixer.music.queue(playlist.pop())
            else:
                playlist.append(song3)
                playlist.append(song2)
                playlist.append(song1)
                mixer.music.queue(playlist.pop())

        if event.type == pygame.MOUSEBUTTONUP:
            if menu != 0:

                flottaPosition = (screenDisplaceW + width / 32, screenDisplaceH + height / 6)
                if flottaPosition[0] <= mouse[0] <= flottaPosition[0]+screen[0]/2.2 and flottaPosition[1] <= mouse[1] <= flottaPosition[1]+screen[1]/10.25:
                    menu = 1
                    buttonPress.play()

                statsPosition = (screenDisplaceW + width / 1.9, screenDisplaceH + height / 6)
                if statsPosition[0] <= mouse[0] <= statsPosition[0]+screen[0]/2.2 and statsPosition[1] <= mouse[1] <= statsPosition[1]+screen[1]/10.25:
                    menu = 2
                    buttonPress.play()

                settingsPosition = (screenDisplaceW + width * 0.8727272727272727, screenDisplaceH + height * 0.0090909090909091)
                if settingsPosition[0] <= mouse[0] <= settingsPosition[0]+screen[0]*0.1 and settingsPosition[1] <= mouse[1] <= settingsPosition[1]+screen[1]*0.0666666666666667:
                    menu = 3
                    buttonPress.play()

                if menu in (11, 12, 13, 14, 15, 16) and menu != 1:
                    shipMenu(menu-10)

                if menu == 1:
                    ship1UpgradePosition = (screenDisplaceW + width / 1.4, screenDisplaceH + height / 3.3)
                    if ship1UpgradePosition[0] <= mouse[0] <= ship1UpgradePosition[0]+screen[0]/3.7 and ship1UpgradePosition[1] <= mouse[1] <= ship1UpgradePosition[1]+screen[1]/10:
                        menu = 11
                        ship(1, "crew1", 0)
                        buttonPress.play()

                    ship2UpgradePosition = (screenDisplaceW + width / 1.4, screenDisplaceH + height / 2.391304)
                    if ship2UpgradePosition[0] <= mouse[0] <= ship2UpgradePosition[0]+screen[0]/3.7 and ship2UpgradePosition[1] <= mouse[1] <= ship2UpgradePosition[1]+screen[1]/10:
                        menu = 12
                        ship(2, "crew2", 0)
                        buttonPress.play()

                    ship3UpgradePosition = (screenDisplaceW + width / 1.4, screenDisplaceH + height / 1.885714)
                    if ship3UpgradePosition[0] <= mouse[0] <= ship3UpgradePosition[0]+screen[0]/3.7 and ship3UpgradePosition[1] <= mouse[1] <= ship3UpgradePosition[1]+screen[1]/10:
                        menu = 13
                        ship(3, "crew3", 0)
                        buttonPress.play()

                    ship4UpgradePosition = (screenDisplaceW + width / 1.4, screenDisplaceH + height / 1.542056)
                    if ship4UpgradePosition[0] <= mouse[0] <= ship4UpgradePosition[0]+screen[0]/3.7 and ship4UpgradePosition[1] <= mouse[1] <= ship4UpgradePosition[1]+screen[1]/10:
                        menu = 14
                        ship(4, "crew4", 0)
                        buttonPress.play()

                    ship5UpgradePosition = (screenDisplaceW + width / 1.4, screenDisplaceH + height / 1.314741)
                    if ship5UpgradePosition[0] <= mouse[0] <= ship5UpgradePosition[0]+screen[0]/3.7 and ship5UpgradePosition[1] <= mouse[1] <= ship5UpgradePosition[1]+screen[1]/10:
                        menu = 15
                        ship(5, "crew5", 0)
                        buttonPress.play()

                    ship6UpgradePosition = (screenDisplaceW + width / 1.4, screenDisplaceH + height / 1.137931)
                    if ship6UpgradePosition[0] <= mouse[0] <= ship6UpgradePosition[0]+screen[0]/3.7 and ship6UpgradePosition[1] <= mouse[1] <= ship6UpgradePosition[1]+screen[1]/10:
                        menu = 16
                        ship(6, "crew6", 0)
                        buttonPress.play()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if menu == 2:
                wasd = wasd

            if menu == 3:
                # Set screen size
                setScreenSizePosition = (screenDisplaceW + width * 0.0136363636363636, screenDisplaceH + height * 0.6272727272727273)
                if setScreenSizePosition[0] <= mouse[0] <= setScreenSizePosition[0]+screen[0]*0.9727272727272727 and setScreenSizePosition[1] <= mouse[1] <= setScreenSizePosition[1]+screen[1]*0.1151515151515152:
                    setScreenSize = screen
                    buttonPress.play()

                # Full reset
                resetPosition = (screenDisplaceW + width * 0.0136363636363636, screenDisplaceH + height * 0.8787878787878788)
                if resetPosition[0] <= mouse[0] <= resetPosition[0]+screen[0]*0.9727272727272727 and resetPosition[1] <= mouse[1] <= resetPosition[1]+screen[1]*0.1151515151515152:
                    sails1 = 0
                    crew1 = 0
                    canons1 = 0
                    balance = 100
                    captain1 = 0
                    crewLifetime1 = 0
                    musicVolume = standardVolume
                    SFXVolume = standardVolume
                    sliderPos = standardVolume
                    slider2Pos = standardVolume
                    setScreenSize = [220, 330]
                    buttonPress.play()
                    mixer.music.unpause()

                # Settings reset
                settingsResetPosition = (screenDisplaceW + width * 0.0272727272727273, screenDisplaceH + height * 0.7515151515151515)
                if settingsResetPosition[0] <= mouse[0] <= settingsResetPosition[0]+screen[0]*0.9727272727272727 and settingsResetPosition[1] <= mouse[1] <= settingsResetPosition[1]+screen[1]*0.1151515151515152:
                    musicVolume = standardVolume
                    SFXVolume = standardVolume
                    sliderPos = standardVolume
                    slider2Pos = standardVolume
                    setScreenSize = [220, 330]

    if pygame.mouse.get_pressed()[0] != 0:
        if menu == 3:
            # Volume slider
            sliderButton = (screenDisplaceW + width/(36.66666666666667*2) + width/66, screenDisplaceH + height * 0.3)
            if sliderButton[0] <= mouse[0] <= sliderButton[0]+screen[0]*0.9272727272727273 and sliderButton[1] <= mouse[1] <= sliderButton[1]+screen[1]*0.1575757575757576:
                sliderPos = (mouse[0]-screenDisplaceW-width/(36.66666666666667*2)-width/66)/(width*0.9272727272727273)
                if musicVolume != round(sliderPos*100)/100:
                    buttonPress.play()
                musicVolume = round(sliderPos*100)/100
                mixer.music.set_volume(musicVolume)

            # SFX slider
            slider2Button = (screenDisplaceW + width/(36.66666666666667*2) + width/66, screenDisplaceH + height * 0.4575757575757576)
            if slider2Button[0] <= mouse[0] <= slider2Button[0]+screen[0]*0.9272727272727273 and slider2Button[1] <= mouse[1] <= slider2Button[1]+screen[1]*0.1575757575757576:
                slider2Pos = (mouse[0]-screenDisplaceW-width/(36.66666666666667*2)-width/66)/(width*0.9272727272727273)
                if SFXVolume != round(slider2Pos*100)/100:
                    buttonPress.play()
                SFXVolume = round(slider2Pos*100)/100
                mixer.Sound.set_volume(buttonPress, SFXVolume)

    # The timer that pays
    income = incomeFunction()
    timerSpeed = timerSpeedFunction()
    timeNow = round(time.time())
    incomePerSec = round(100 * income/timerSpeed)/100
    if timeNow != lastTimeDisplayed:
        balance = balance + incomePerSec
        if timeStartSec % 60 == 0:
            timeStartSec = 0
            timeStartMin = timeStartMin + 1
        timeStartSec = timeStartSec + 1
        print("Time since start: "+str(timeStartMin-1)+":"+str(timeStartSec-1))
        lastTimeDisplayed = timeNow
        print("Balance: "+str(balance))
        print("Income per second: "+str(incomePerSec)+"\n")

    sailsCost1 = sailsStandCost1 * (sailsCostMulti1 ** sails1)
    crewCost1 = crewStandCost1 * (crewCostMulti1 ** crewLifetime1)
    canonsCost1 = canonsStandCost1 * (canonsCostMulti1 ** canons1)

    # Loading-screen
    if loadingScreenWait < timeNow and loadingScreenWait != 0:
        menu = 1
        loadingScreenWait = 0

    if menu == 0 and saved != 1:
        window.blit(scaled_ls1, ls1_rect)

    elif menu == 0 and saved == 1:
        window.blit(scaled_ls2, ls2_rect)

    # Graphics
    elif menu != 0:

        if menu == 1:
            window.blit(scaled_bg, bg_rect)

        if menu == 2:
            window.blit(scaled_stats, stats_rect)

            incomePerSecPosition = (screenDisplaceW + width*0.3590909090909091, screenDisplaceH + height*0.635)
            if 1000000 > incomePerSec >= 1000:
                textIncomePerSec = mediumFont.render((str(round(incomePerSec/1000))+"K"), True, textColour)
            elif incomePerSec >= 1000000:
                textIncomePerSec = mediumFont.render((str(round(incomePerSec/1000000))+"M"), True, textColour)
            else:
                textIncomePerSec = mediumFont.render((str(incomePerSec)), True, textColour)
            window.blit(textIncomePerSec, incomePerSecPosition)

            balanceStatsPosition = (screenDisplaceW + width*0.2181818181818182, screenDisplaceH + height*0.2995)
            if 1000000 > balance >= 1000:
                textBalanceStats = mediumFont.render((str(round(balance/1000))+"K"), True, textColour)
            elif balance >= 1000000:
                textBalanceStats = mediumFont.render((str(round(balance/1000000))+"M"), True, textColour)

            else:
                textBalanceStats = mediumFont.render((str(balance)), True, textColour)
            window.blit(textBalanceStats, balanceStatsPosition)

            timerSpeedPosition = (screenDisplaceW + width*0.1909090909090909, screenDisplaceH + height*0.52)
            textTimerSpeed = mediumFont.render((str(timerSpeed)), True, textColour)
            window.blit(textTimerSpeed, timerSpeedPosition)

        if menu in (11, 12, 13, 14, 15, 16):
            window.blit(scaled_ship1Upgrade, ship1Upgrade_rect)
            shipGraphics(menu-10)

        if menu == 3:
            window.blit(scaled_settings, settings_rect)

            musicVolumePosition = (screenDisplaceW + width / 1.4, screenDisplaceH + height / 2.8)
            textMusicVolume = smallFont.render((str(round(musicVolume * 100)) + "%"), True, textColour)
            window.blit(textMusicVolume, musicVolumePosition)

            SFXVolumePosition = (screenDisplaceW + width / 1.65, screenDisplaceH + height / 1.9)
            textSFXVolume = smallFont.render((str(round(SFXVolume * 100)) + "%"), True, textColour)
            window.blit(textSFXVolume, SFXVolumePosition)

            sliderPlacement = (screenDisplaceW + (width * 0.9424242424242423) * sliderPos + width / (36.66666666666667 * 2)), screenDisplaceH + round(height * 0.316), round(width / 33), round(height / 8.25)
            pygame.draw.rect(window, (0, 0, 0), pygame.Rect(sliderPlacement))

            slider2Placement = (screenDisplaceW + (width * 0.9424242424242423) * slider2Pos + width / (36.66666666666667 * 2)), screenDisplaceH + round(height * 0.48), round(width / 33), round(height / 8.25)
            pygame.draw.rect(window, (0, 0, 0), pygame.Rect(slider2Placement))

        balancePosition = (screenDisplaceW + width / 1.85, screenDisplaceH + height / 10.5)

        if 1000000 > balance >= 1000:
            textBalance = smallFont.render((str(round(balance/1000))+"K"), True, textColour)

        elif balance >= 1000000:
            textBalance = smallFont.render((str(round(balance/1000000))+"M"), True, textColour)

        else:
            textBalance = smallFont.render((str(round(balance))), True, textColour)
        window.blit(textBalance, balancePosition)

    pygame.display.flip()

# Save data
saved = 1
saveList = {"lastTimeDisplayed": lastTimeDisplayed, "balance": balance, "musicVolume": musicVolume, "SFXVolume": SFXVolume, "setScreenSize": setScreenSize, "mainDictionary": mainDictionary}
save_object(saveList)
save_saved(saved)

pygame.quit()
