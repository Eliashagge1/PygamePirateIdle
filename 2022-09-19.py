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
screen = [220, 330]
clock = pygame.time.Clock()

#Background images
background = pygame.image.load('Design_Mk1.png').convert_alpha()
scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())
statsScreen = pygame.image.load('Design_Mk1.png').convert_alpha()
scaled_stats, stats_rect = transformScaleKeepRatio(statsScreen, window.get_size())
ship1Upgrade = pygame.image.load('Ship1Upgrade.png').convert_alpha()
scaled_ship1Upgrade, ship1Upgrade_rect = transformScaleKeepRatio(ship1Upgrade, window.get_size())

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
    sails1 = saveList[1]
    crew1 = saveList[2]
    canons1 = saveList[3]
    balance = saveList[4]
    captain1 = saveList[5]
    crewLifetime1 = saveList[6]
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

#Font
smallFont = pygame.font.SysFont('Corbel', 15)
mediumFont = pygame.font.SysFont('Corbel', 30)
largeFont = pygame.font.SysFont('Corbel', 45)
textColour = (200, 200, 200)

height = 330
screenDisplaceH = 0
width = 220
screenDisplaceW = 0

x = 0
#Loop 1
loop1 = True
while loop1 == True:
    clock.get_fps()
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop1 = False

        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            scaled_bg, bg_rect = transformScaleKeepRatio(background, window.get_size())
            scaled_ls1, ls1_rect = transformScaleKeepRatio(loadingScreen1, window.get_size())
            scaled_ls2, ls2_rect = transformScaleKeepRatio(loadingScreen2, window.get_size())
            scaled_ship1Upgrade, ship1Upgrade_rect = transformScaleKeepRatio(ship1Upgrade, window.get_size())
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


        if event.type == pygame.MOUSEBUTTONUP:
            if menu != 0:
                flottaPosition = (screenDisplaceW + width / 32, screenDisplaceH + height / 6)
                if flottaPosition[0] <= mouse[0] <= flottaPosition[0]+screen[0]/2.2 and flottaPosition[1] <= mouse[1] <= flottaPosition[1]+screen[1]/10.25:
                    menu = 1
                statsPosition = (screenDisplaceW + width / 1.9, screenDisplaceH + height / 6)
                if statsPosition[0] <= mouse[0] <= statsPosition[0]+screen[0]/2.2 and statsPosition[1] <= mouse[1] <= statsPosition[1]+screen[1]/10.25:
                    print("This function isn't available yet!")
                    menu = 2

                if menu == 1:
                    ship1UpgradePosition = (screenDisplaceW + width / 1.4, screenDisplaceH + height / 3.3)
                    if ship1UpgradePosition[0] <= mouse[0] <= ship1UpgradePosition[0]+screen[0]/3.7 and ship1UpgradePosition[1] <= mouse[1] <= ship1UpgradePosition[1]+screen[1]/10:
                        print("ship upgrade")
                        menu = 3
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
                            #Printing useful information
                            print("Crew now cost: " + str(round(crewCost1)))
                            print("Number of crew: " + str(crew1))
                            print("Income: "+str(income))
                            print("Balance: "+str(balance)+"\n")
                        elif crew1 == maxCrew1:
                            print("You've maxed out on crew!\n")
                        else:
                            print("You cant afford this, it costs " + str(round(crewCost1)) + ", and you only have " + str(balance) + "\n")

                    if screenDisplaceW + screen[0]/1.95 <= mouse[0] <= screenDisplaceW + screen[0]/1.02 and screenDisplaceH + screen[1]/2.4 <= mouse[1] <= screenDisplaceH + screen[1]/1.94:
                        if balance > sailsCost1 and sails1 < maxSails1:
                            balance = balance - round(sailsCost1)
                            sails1 = sails1 + 1
                            sailsCost1 = sailsStandCost1 * (sailsCostMulti1 ** sails1)
                            timerSpeed = round(timerStand / (sailsMulti1 ** sails1))
                            #Printing useful information
                            print("Sails now cost: " + str(round(sailsCost1)))
                            print("Number of sails: " + str(sails1))
                            print("Timer speed: "+str(timerSpeed))
                            print("Balance: "+str(balance)+"\n")
                        elif sails1 == maxSails1:
                            print("You've maxed out on sails!\n")
                        else:
                            print("You cant afford this, it costs " + str(round(sailsCost1)) + ", and you only have " + str(balance) + "\n")

                    if screenDisplaceW + screen[0]/1.95 <= mouse[0] <= screenDisplaceW + screen[0]/1.02 and screenDisplaceH + screen[1]/1.875 <= mouse[1] <= screenDisplaceH + screen[1]/1.45:
                        if balance > canonsCost1 and crew1 >= 2 and canons1 < maxCanons1:
                            balance = balance - round(canonsCost1)
                            crew1 = crew1 - 2
                            canons1 = canons1 + 1
                            canonsCost1 = canonsStandCost1 * (canonsCostMulti1 ** canons1)
                            income = round(incomeStand * (crewMulti1 ** crew1) * (canonsMulti1 ** canons1) + captainEarn1 * captain1)
                            #Printing useful information
                            print("Canons now cost: " + str(round(canonsCost1)))
                            print("Number of canons: " + str(canons1))
                            print("Number of crew: " + str(crew1))
                            print("Income: "+str(income))
                            print("Balance: "+str(balance)+"\n")
                        elif balance < canonsCost1 and crew1 < 2:
                            print("You cant afford this, it costs " + str(round(canonsCost1)) + ", and you only have " + str(balance))
                            print("Also it cost 2 crew, you only have " + str(crew1) + "\n")
                        elif balance < canonsCost1:
                            print("You cant afford this, it costs " + str(round(canonsCost1)) + ", and you only have " + str(balance) + "\n")
                        elif crew1 < 2:
                            print("This costs 2 crew, you only have " + str(crew1) + "\n")
                        elif canons1 == maxCanons1:
                            print("You've maxed out on canons!\n")

                    if screenDisplaceW + screen[0]/1.95 <= mouse[0] <= screenDisplaceW + screen[0]/1.02 and screenDisplaceH + screen[1]/1.42 <= mouse[1] <= screenDisplaceH + screen[1]/1.16:
                        if balance >= captain1Cost and crew1 == maxCrew1 and canons1 == maxCanons1 and sails1 == maxSails1 and captain1 < 1:
                            balance = balance - captain1Cost
                            captain1 = 1
                        elif captain1 != 0:
                            print("You already have a captain!")
                        else:
                            print("you can't buy this right now!")


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

    if loadingScreenWait < timeNow and loadingScreenWait != 0:
        menu = 1
        loadingScreenWait = 0

    if menu == 0 and saved != 1:
        window.blit(scaled_ls1, ls1_rect)

    elif menu == 0 and saved == 1:
        window.blit(scaled_ls2, ls2_rect)

    elif menu != 0:

        if menu == 1:
            window.blit(scaled_bg, bg_rect)

        if menu == 2:
            window.blit(scaled_bg, bg_rect)

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
            print("")

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
saveList = [lastTimeDisplayed, sails1, crew1, canons1, balance, captain1, crewLifetime1]
save_object(saveList)
save_saved(saved)

pygame.quit()
