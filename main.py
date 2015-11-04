import random
import time

def rouletteIntro():
    name = input("Hello there brave one! What is your name?\n    ")
    print("You are about to play Russian Roulette!")
    time.sleep(1)
    print("Your goal is to get the highest amount of blank shots without dying!")
    print("So if you get all 7 blanks, you win!")
    time.sleep(1)
    print("So " + name + ". let the games begin..")

    bulletChamber = random.randint(1,8)

    return bulletChamber

def pickChamber(loadedChamber):
    dead = 0
    chosenChambers = set()

    while dead == 0:
        chamberCount = len(chosenChambers)
        chambersLeft = 8 - chamberCount
        chambersLeft = str(chambersLeft)
        score = str(chamberCount)
        print("There are " + chambersLeft + " chambers left.")


        if chamberCount == 7:
            print("Congratulations! Your prize is..")
            time.sleep(3)
            print("BANG!")
            time.sleep(2)
            print("You've survived " + score + " shots.")
            shot = 1

        else:
            chamber = input("Pick a chamber from 1 - 8.\n")
            chamber = int(chamber)

            if chamber < 1 or chamber > 8:
                print("Fuck off.")

            elif chamber == loadedChamber:
                print("...")
                time.sleep(3)
                print("BANG!")
                time.sleep(2)
                print("You've survived " + score + " shots.")
                dead = 1

            elif chamber != loadedChamber:
                print("...")
                time.sleep(5)
                print("'click'")
                chosenChambers.add(chamber)



play = "y"
while play == "y" or play == "Y":

    chamber = rouletteIntro()

    pickChamber(chamber)

    play = input("Would you like to play again?(y/n)\n")
