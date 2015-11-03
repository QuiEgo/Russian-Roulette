import random
import time

def rouletteIntro():
    name = input("Hello there brave one! What is your name?\n    ")
    print("You are about to play Russian Roulette!")
    time.sleep(1)
    print("Your goal is to get the highest amount of blank shots without dying!")
    print("So if you get all 7 blanks, you win!")
    time.sleep(2)
    print("So " + name + ". let the games begin..")
    time.sleep(5)

    bulletChamber = random.randint(1,8)

    return bulletChamber

def pickChamber(loadedChamber):
    shot == 0
    chosenChambers = []

    while shot == 0:
        chamberCount = len(chosenChambers)

        if chamberCount == 7:
            print("Congratulations! Your prize is..")
            time.sleep(5)
            print("BANG!")
            break

        if chamberCount > 7:
            chamber = input("Pick a chamber from 1 - 8.")
            chamber = int(chamber)

        if chamber < 1 or chamber > 8:
            print("Fuck off.")

        if chamber == loadedChamber:
            print(...)
            time.sleep(5)
            print("BANG!")
            break

        if chamber != loadedChamber:
            print(...)
            time.sleep(5)
            print("'click'")
            chosenChambers.append(chamber)

    shot = 1

play = "y"
while play == "y" or play == "Y":
    rouletteIntro()

    loadedChamber = rouletteIntro()

    pickChamber(bulletChamber)

    play = input("Would you like to play again?(y/n)\n")