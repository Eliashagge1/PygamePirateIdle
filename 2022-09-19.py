#Imports and initiations
import pygame, sys, time, math, def1, pickle
from pygame import mixer
from def1 import *

sys.path.append("C:/Users/User/Desktop/PirateIdle_test/def1.py")

pygame.init()
mixer.init()


#Init def (def1.py) and creates fonst
init_screen_and_clock()
fonts = create_fonts([32, 16, 14, 8])


#Display size
screen = [220, 330]
setScreenSize = screen
clock = pygame.time.Clock()


#Variables
lastTimeDisplayed = 0
balance = 100
incomeStand = 100
timerStand = 60
offlineDevaule = 1/3

sails1 = 0
sailsCost1 = 300
sailsStandCost1 = 300
sailsCostMulti1 = 1.5
sailsMulti1 = 1.5
maxSails1 = 5

crew1 = 0
crewCost1 = 20
crewStandCost1 = 20
crewCostMulti1 = 1.1
crewMulti1 = 1.1
crewLifetime1 = 0
maxCrew1 = 15

canons1 = 0
canonsCost1 = 50
canonsStandCost1 = 50
canonsCostMulti1 = 1.2
canonsMulti1 = 1.25
maxCanons1 = 15

captain1 = 0
captainEarn1 = 2500
captain1Cost = 20000

standardVolume = 0.2
musicVolume = standardVolume
SFXVolume = standardVolume


#For the saving
class MyClass():
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


#Start loadingscreen
menu = 0
loadingScreenWait = round(time.time()+2)


#Load saved objects
saved = load_object("savefiles/saved.pickle")
if saved == 1:
    saveList = load_object("savefiles/data.pickle")
    lastTimeDisplayed = saveList[0]
    sails1 = saveList[1]
    crew1 = saveList[2]
    canons1 = saveList[3]
    balance = saveList[4]
    captain1 = saveList[5]
    crewLifetime1 = saveList[6]
    musicVolume = saveList[7]
    SFXVolume = saveList[8]
    setScreenSize = saveList[9]
    screen = setScreenSize
    income = round(incomeStand * (crewMulti1 ** crew1) * (canonsMulti1 ** canons1) + captainEarn1 * captain1)
    timerSpeed = round(timerStand / (sailsMulti1 ** sails1))
    timeNow = round(time.time())
    incomePerSec = round(100 * income/timerSpeed)/100
    if (timeNow - lastTimeDisplayed) <= 7200 and lastTimeDisplayed != 0:
        balance = round(balance + ((timeNow - lastTimeDisplayed) * offlineDevaule * incomePerSec))
    elif (timeNow - lastTimeDisplayed) > 7200 and lastTimeDisplayed != 0:
        balance = round(balance + (7200 * offlineDevaule * incomePerSec))
    print(saveList)
    print(incomePerSec)


#Create window
window = pygame.display.set_mode(screen, pygame.RESIZABLE)


#Background images
background = pygame.image.load('pictures/Design_Mk1.png').convert_alpha()
scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())
statsScreen = pygame.image.load('pictures/Stats.png').convert_alpha()
scaled_stats, stats_rect = transformScaleKeepRatio(statsScreen, window.get_size())
ship1Upgrade = pygame.image.load('pictures/Ship1Upgrade.png').convert_alpha()
scaled_ship1Upgrade, ship1Upgrade_rect = transformScaleKeepRatio(ship1Upgrade, window.get_size())
settingsScreen = pygame.image.load('pictures/Settings.png').convert_alpha()
scaled_settings, settings_rect = transformScaleKeepRatio(settingsScreen, window.get_size())


#Loadingscreen image
loadingScreen1 = pygame.image.load('pictures/loading screen 1.png').convert_alpha()
scaled_ls1, ls1_rect = transformScaleKeepRatio(loadingScreen1, window.get_size())
loadingScreen2 = pygame.image.load('pictures/loading screen 2.png').convert_alpha()
scaled_ls2, ls2_rect = transformScaleKeepRatio(loadingScreen2, window.get_size())


#Songs
song1 = "sound/song1.wav"
song2 = "sound/song2.wav"
song3 = "sound/song3.wav"


#Playlist
playlist = list()
playlist.append(song3)
playlist.append(song2)
playlist.append(song1)
print(playlist)


#Sound
mixer.music.load(playlist.pop())
mixer.music.queue(playlist.pop())
mixer.music.set_endevent(pygame.USEREVENT)
mixer.music.set_volume(musicVolume)
mixer.music.play()
mixer.music.unpause()

buttonPress = mixer.Sound("sound/zapsplat_multimedia_button_click_fast_short_004_79288.mp3")
mixer.Sound.set_volume(buttonPress, SFXVolume)


#Icon and the name of the game
pygame.display.set_caption("Pirate Idle")
icon = pygame.image.load("pictures/IJ.png")
pygame.display.set_icon(icon)


#Text colour
textColour = (50, 50, 50)


if saved == 1:
    height = screen[1]
    width = screen[0]
else:
    height = 330
    width = 220
screenDisplaceW = 0
screenDisplaceH = 0


#Volume slider
sliderPos = musicVolume
slider2Pos = SFXVolume


x = 0
#Loop 1
loop1 = True
while loop1 == True:

    #Fonts
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
                    menu = 4
                    buttonPress.play()

                if menu == 1:
                    ship1UpgradePosition = (screenDisplaceW + width / 1.4, screenDisplaceH + height / 3.3)
                    if ship1UpgradePosition[0] <= mouse[0] <= ship1UpgradePosition[0]+screen[0]/3.7 and ship1UpgradePosition[1] <= mouse[1] <= ship1UpgradePosition[1]+screen[1]/10:
                        menu = 3
                        buttonPress.play()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if menu == 2:
                x=x

            if menu == 3:
                #Purchase of goods
                if screenDisplaceW + screen[0]/1.95 <= mouse[0] <= screenDisplaceW + screen[0]/1.02 and screenDisplaceH + screen[1]/3.3 <= mouse[1] <= screenDisplaceH + screen[1]/2.5:
                    if balance > crewCost1 and crew1 < maxCrew1:
                        balance = balance - round(crewCost1)
                        crew1 = crew1 + 1
                        crewLifetime1 = crewLifetime1 + 1
                        crewCost1 = crewStandCost1 * (crewCostMulti1 ** crewLifetime1)
                        income = round(incomeStand * (crewMulti1 ** crew1) * (canonsMulti1 ** canons1) + captainEarn1 * captain1)
                        buttonPress.play()
                    elif crew1 == maxCrew1:
                        print("Golden button sound\n")
                    else:
                        print("Angry button sound\n")

                if screenDisplaceW + screen[0]/1.95 <= mouse[0] <= screenDisplaceW + screen[0]/1.02 and screenDisplaceH + screen[1]/2.4 <= mouse[1] <= screenDisplaceH + screen[1]/1.94:
                    if balance > sailsCost1 and sails1 < maxSails1:
                        balance = balance - round(sailsCost1)
                        sails1 = sails1 + 1
                        sailsCost1 = sailsStandCost1 * (sailsCostMulti1 ** sails1)
                        timerSpeed = round(timerStand / (sailsMulti1 ** sails1))
                        buttonPress.play()
                    elif sails1 == maxSails1:
                        print("Golden button sounds\n")
                    else:
                        print("Angry button sound\n")

                if screenDisplaceW + screen[0]/1.95 <= mouse[0] <= screenDisplaceW + screen[0]/1.02 and screenDisplaceH + screen[1]/1.875 <= mouse[1] <= screenDisplaceH + screen[1]/1.45:
                    if balance > canonsCost1 and crew1 >= 2 and canons1 < maxCanons1:
                        balance = balance - round(canonsCost1)
                        crew1 = crew1 - 2
                        canons1 = canons1 + 1
                        canonsCost1 = canonsStandCost1 * (canonsCostMulti1 ** canons1)
                        income = round(incomeStand * (crewMulti1 ** crew1) * (canonsMulti1 ** canons1) + captainEarn1 * captain1)
                        buttonPress.play()
                    elif canons1 == maxCanons1:
                        print("Golden button sound\n")
                    else:
                        print("Angry button sound\n")

                if screenDisplaceW + screen[0]/1.95 <= mouse[0] <= screenDisplaceW + screen[0]/1.02 and screenDisplaceH + screen[1]/1.42 <= mouse[1] <= screenDisplaceH + screen[1]/1.16:
                    if balance >= captain1Cost and crew1 == maxCrew1 and canons1 == maxCanons1 and sails1 == maxSails1 and captain1 < 1:
                        balance = balance - captain1Cost
                        captain1 = 1
                        buttonPress.play()
                    elif captain1 != 0:
                        print("Golden button sound\n")
                    else:
                        print("Angry button sound\n")

            if menu == 4:
                #Set screen size
                setScreenSizePosition = (screenDisplaceW + width * 0.0136363636363636, screenDisplaceH + height * 0.6272727272727273)
                if setScreenSizePosition[0] <= mouse[0] <= setScreenSizePosition[0]+screen[0]*0.9727272727272727 and setScreenSizePosition[1] <= mouse[1] <= setScreenSizePosition[1]+screen[1]*0.1151515151515152:
                    setScreenSize = screen
                    buttonPress.play()

                #Full reset
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
                    setScreenSize = [220, 330]
                    buttonPress.play()
                    mixer.music.unpause()

                #Settings reset
                settingsResetPosition = (screenDisplaceW + width * 0.0272727272727273, screenDisplaceH + height * 0.7515151515151515)
                if settingsResetPosition[0] <= mouse[0] <= settingsResetPosition[0]+screen[0]*0.9727272727272727 and settingsResetPosition[1] <= mouse[1] <= settingsResetPosition[1]+screen[1]*0.1151515151515152:
                    musicVolume = standardVolume
                    SFXVolume = standardVolume
                    setScreenSize = [220, 330]


    if pygame.mouse.get_pressed()[0] != 0:
        if menu == 4:
            #Volume slider
            sliderButton = (screenDisplaceW + width/(36.66666666666667*2) + width/66, screenDisplaceH + height * 0.3)
            if sliderButton[0] <= mouse[0] <= sliderButton[0]+screen[0]*0.9272727272727273 and sliderButton[1] <= mouse[1] <= sliderButton[1]+screen[1]*0.1575757575757576:
                sliderPos = (mouse[0]-screenDisplaceW-width/(36.66666666666667*2)-width/66)/(width*0.9272727272727273)
                if musicVolume != round(sliderPos*100)/100:
                    buttonPress.play()
                musicVolume = round(sliderPos*100)/100
                mixer.music.set_volume(musicVolume)

            #SFX slider
            slider2Button = (screenDisplaceW + width/(36.66666666666667*2) + width/66, screenDisplaceH + height * 0.4575757575757576)
            if slider2Button[0] <= mouse[0] <= slider2Button[0]+screen[0]*0.9272727272727273 and slider2Button[1] <= mouse[1] <= slider2Button[1]+screen[1]*0.1575757575757576:
                slider2Pos = (mouse[0]-screenDisplaceW-width/(36.66666666666667*2)-width/66)/(width*0.9272727272727273)
                if SFXVolume != round(slider2Pos*100)/100:
                    buttonPress.play()
                SFXVolume = round(slider2Pos*100)/100
                mixer.Sound.set_volume(buttonPress, SFXVolume)



    #The timer that pays
    income = round(incomeStand * (crewMulti1 ** crew1) * (canonsMulti1 ** canons1) + captainEarn1 * captain1)
    timerSpeed = round(timerStand / (sailsMulti1 ** sails1))
    timeNow = round(time.time())
    incomePerSec = round(100 * income/timerSpeed)/100
    if timeNow % timerSpeed == 0 and timeNow != lastTimeDisplayed:
        balance = balance + income
        print("Time right now: "+str(timeNow))
        lastTimeDisplayed = timeNow
        print("Balance: "+str(balance))
        print("Income per second: "+str(incomePerSec)+"\n")

    sailsCost1 = sailsStandCost1 * (sailsCostMulti1 ** sails1)
    crewCost1 = crewStandCost1 * (crewCostMulti1 ** crewLifetime1)
    canonsCost1 = canonsStandCost1 * (canonsCostMulti1 ** canons1)


    #Loadingscreen
    if loadingScreenWait < timeNow and loadingScreenWait != 0:
        menu = 1
        loadingScreenWait = 0

    if menu == 0 and saved != 1:
        window.blit(scaled_ls1, ls1_rect)

    elif menu == 0 and saved == 1:
        window.blit(scaled_ls2, ls2_rect)


    #Graphics
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


        if menu == 3:
            window.blit(scaled_ship1Upgrade, ship1Upgrade_rect)

            crewShip1Position = (screenDisplaceW + screen[0]/3.3, screenDisplaceH + screen[1]/3.25)
            textCrewShip1 = mediumFont.render(str(crew1), True, textColour)
            window.blit(textCrewShip1, crewShip1Position)
            crewShip1CostPosition = (screenDisplaceW + screen[0]/1.75, screenDisplaceH + screen[1]/3.25)
            if crew1 >= maxCrew1:
                textCrewShip1Cost = mediumFont.render("Max", True, textColour)
            elif crewCost1 < 1000:
                textCrewShip1Cost = mediumFont.render(str(round(crewCost1)), True, textColour)
            elif crewCost1 >= 1000:
                textCrewShip1Cost = mediumFont.render(str(round(crewCost1 / 1000)) + "K", True, textColour)
            window.blit(textCrewShip1Cost, crewShip1CostPosition)

            sailsShip1Position = (screenDisplaceW + screen[0]/3.3, screenDisplaceH + screen[1]/2.4)
            textSailsShip1 = mediumFont.render(str(sails1), True, textColour)
            window.blit(textSailsShip1, sailsShip1Position)
            sailsShip1CostPosition = (screenDisplaceW + screen[0]/1.75, screenDisplaceH + screen[1]/2.4)
            if sails1 >= maxSails1:
                textSailsShip1Cost = mediumFont.render("Max", True, textColour)
            elif sailsCost1 < 1000:
                textSailsShip1Cost = mediumFont.render(str(round(sailsCost1)), True, textColour)
            elif sailsCost1 >= 1000:
                textSailsShip1Cost = mediumFont.render(str(round(sailsCost1 / 1000)) + "K", True, textColour)
            window.blit(textSailsShip1Cost, sailsShip1CostPosition)

            canonsShip1Position = (screenDisplaceW + screen[0]/30, screenDisplaceH + screen[1]/1.7)
            textCanonsShip1 = mediumFont.render(str(canons1), True, textColour)
            window.blit(textCanonsShip1, canonsShip1Position)
            canonsShip1CostPosition = (screenDisplaceW + screen[0]/1.75, screenDisplaceH + screen[1]/1.85)
            if canons1 >= maxCanons1:
                textCanonsShip1Cost = mediumFont.render("Max", True, textColour)
            elif canonsCost1 < 1000:
                textCanonsShip1Cost = mediumFont.render(str(round(canonsCost1)), True, textColour)
            elif canonsCost1 >= 1000:
                textCanonsShip1Cost = mediumFont.render(str(round(canonsCost1 / 1000)) + "K", True, textColour)
            window.blit(textCanonsShip1Cost, canonsShip1CostPosition)

            captain1Position = (screenDisplaceW + screen[0]/30, screenDisplaceH + screen[1]/1.3)
            if captain1 >= 1:
                textCaptain1 = mediumFont.render("Yes", True, textColour)
            elif captain1 < 1:
                textCaptain1 = mediumFont.render("No", True, textColour)
            window.blit(textCaptain1, captain1Position)


        if menu == 4:
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


        if menu == 5:
            print("")

        balancePosition = (screenDisplaceW + width / 1.85, screenDisplaceH + height / 10.5)

        if 1000000 > balance >= 1000:
            textBalance = smallFont.render((str(round(balance/1000))+"K"), True, textColour)
        elif balance >= 1000000:
            textBalance = smallFont.render((str(round(balance/1000000))+"M"), True, textColour)
        else:
            textBalance = smallFont.render((str(balance)), True, textColour)
        window.blit(textBalance, balancePosition)


    pygame.display.flip() #Display update

#Save data
saved = 1
saveList = [lastTimeDisplayed, sails1, crew1, canons1, balance, captain1, crewLifetime1, musicVolume, SFXVolume, setScreenSize]
save_object(saveList)
save_saved(saved)

pygame.quit()
