import time
import pygame
pygame.init()

fps = 144
fpsClock = pygame.time.Clock()
lastTimeDisplayed = 0
crew = int(input("Input number of crew\n"))
income = int(input("Input income\n"))
balance = 0

while True:
    timerSpeed = round(60 / (1 + (0.1*crew)))
    fpsClock.tick(fps)
    timeNow = round(time.time())
    if timeNow%timerSpeed == 0 and timeNow != lastTimeDisplayed:
        balance = balance + income
        print("Time right now = "+str(timeNow))
        lastTimeDisplayed = timeNow
        print("Balance = "+str(balance))
