import pygame
import random
import time

#THIS CODE WAS MADE BY GITHUB USER asdfKC
#Any use of this code without giving any info about asdfKC will result in a strike. I think.


pygame.init()
pygame.mixer.init()
 
coords = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10",
          "B1","B2","B3","B4","B5","B6","B7","B8","B9","B10",
          "C1","C2","C3","C4","C5","C6","C7","C8","C9","C10",
          "D1","D2","D3","D4","D5","D6","D7","D8","D9","D10",
          "E1","E2","E3","E4","E5","E6","E7","E8","E9","E10",
          "F1","F2","F3","F4","F5","F6","F7","F8","F9","F10",
          "G1","G2","G3","G4","G5","G6","G7","G8","G9","G10",
          "H1","H2","H3","H4","H5","H6","H7","H8","H9","H10",
          "I1","I2","I3","I4","I5","I6","I7","I8","I9","I10",
          "I1","I2","I3","I4","I5","I6","I7","I8","I9","I10",
          "J1","J2","J3","J4","J5","J6","J7","J8","J9","J10",]

tries = 0
bot_score = 0
score = 0
used = []
bots_used = []
player_ships = []
bot_ships = []
directions = ["right","left","up","down"]

def get_coord():
    C = random.choice(coords)
    if C in used:
        get_coord()
    
    else: 
        coords.append(C)
        

print("time to figure out where you want to put the ships! You have 8 ships! The are ALL one pin large. IK weird shape ;)")
print("if you repeat the same coordinate again... ya. People go BOO BOOM")
print("however, the bot have supa tech. It is possible to have all 8 of their ships on 1 coord!")
print("some valids coordinates are", coords)
time.sleep(5)
def ships():
    for i in range(5):
        destroyer = input("Enter a VALID cordinate")
        if destroyer not in coords:
            print("try again")
            print("Rip. That is not a valid coordinate")
            print("some valids coordinates are", coords)
        elif destroyer in player_ships:
            print("try again")
            print("OHNO THe SHIP CRASHED INTO YOUR OWN. Te AI HAS A ADVANTAGE")
        else:
            player_ships.append(destroyer)
            
            
def bots():
    ship1 = random.choice(coords)
    bot_ships.append(ship1)
    ship2 = random.choice(coords)
    bot_ships.append(ship2)
    ship3 = random.choice(coords)
    bot_ships.append(ship3)
    ship4 = random.choice(coords)
    bot_ships.append(ship4)
    ship5 = random.choice(coords)
    bot_ships.append(ship5)
    ship6 = random.choice(coords)
    bot_ships.append(ship6)
    ship7 = random.choice(coords)
    bot_ships.append(ship7)
    ship8 = random.choice(coords)
    bot_ships.append(ship8)
ships()

bots()

print("THEY WILL GET THE TURN FIRST")
def botturn():
   global bot_score
   global tries
   while True:
       if tries == 31:
           if score > bot_score:
               print("Bots: WE LOST!!")
           else:
               print("Bots: The humans will now all DIE")
       hmm = random.choice(coords)
       if hmm in bots_used:
           pygame.mixer.music.load("HA.mp3")
           pygame.mixer.music.play()
           print("Looks like the bots failed...")
           playerturn()
           
       elif hmm in player_ships:
           pygame.mixer.music.load("Uhoh.mp3")
           pygame.mixer.music.play() 
           time.sleep(18)
           pygame.mixer.music.load("BOOM.mp3")
           pygame.mixer.music.play()
           print("They hit us.")
           bots_used.append(hmm)
           bot_score += 1
           playerturn()
           break
       else:
           print("Ha! They Missed us!")
           bots_used.append(hmm)
           playerturn()
           break
def playerturn():
    global score
    global tries
    while True:
        turn= input(" Your TURN. A VALID COORD PLS(or loose a chance)")
        if turn in used:
            print("We have tried that one")
            tries += 1
            botturn()
            break
        elif turn in bot_ships:
            pygame.mixer.music.load("BOOM.mp3")
            pygame.mixer.music.play()
            print("good work, captain!")
            used.append(turn)
            score += 1
            tries += 1
            botturn()
            break
        else:
            print("A miss")
            botturn()
            tries += 1
            used.append(turn)
            break
botturn()
