__author__ = 'Les Pounder'

#The lines below import modules of code into our game, in particular these import time functions to allow us to pause and stop the game, and random provides a method of choosing random numbers or characters.
from time import *
from random import *
import os,sys

#This is a function, we use it to do lots of things and then call it by it's name later on
#To create a function we use "def name():" where name can be anything.

def clear_screen():  #Simple function that clears the screen
    os.system('cls' if os.name=='nt' else 'clear')

def title():
     print ("   __                           _          __                                  ")
     print ("  / /  ___  __ _  ___ _ __   __| |   ___  / _|   /\  /\___ _ __ ___   ___  ___ ")
     print (" / /  / _ \/ _` |/ _ \ '_ \ / _` |  / _ \| |_   / /_/ / _ \ '__/ _ \ / _ \/ __|")
     print ("/ /__|  __/ (_| |  __/ | | | (_| | | (_) |  _| / __  /  __/ | | (_) |  __/\__ \ ")
     print ("\____/\___|\__, |\___|_| |_|\__,_|  \___/|_|   \/ /_/ \___|_|  \___/ \___||___/")
def castle():

    print ("*                                 |>>>                    +        ")
    print ("+          *                      |                   *       +")
    print ("                    |>>>      _  _|_  _   *     |>>>		   ")
    print ("           *        |        |;| |;| |;|        |                 *")
    print ("     +          _  _|_  _    \\.    .  /    _  _|_  _       +")
    print (" *             |;|_|;|_|;|    \\: +   /    |;|_|;|_|;|")
    print ("               \\..      /    ||:+++. |    \\.    .  /           *")
    print ("      +         \\.  ,  /     ||:+++  |     \\:  .  /")
    print ("                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *")
    print ("          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +")
    print ("                 ||+++ ||.    .     .      . ||+++.|   *")
    print ("+   *            ||: . ||:.     . .   .  ,   ||:   |               *")
    print ("         *       ||:   ||:  ,     +       .  ||: , |      +")
    print ("  *              ||:   ||:.     +++++      . ||:   |         *")
    print ("     +           ||:   ||.     +++++++  .    ||: . |    +")
    print ("           +     ||: . ||: ,   +++++++ .  .  ||:   |             +")
    print ("                 ||: . ||: ,   +++++++ .  .  ||:   |        *")
    print ("                 ||: . ||: ,   +++++++ .  .  ||:   |")

def north():
    print ("To go north press n then enter")
def east():
    print ("To go east press e then enter")
def south():
    print ("to go south press s then enter")
def west():
    print ("To go west press w then enter")


def setup():
    #global is used to create variables that can be used throughout our game
    global name
    global HP
    global MP
    #Our variable "name" is used to store our name, captured by keyboard input.
    name = input("What is your name warrior? ")
    #randint is a great way of adding some variety to your players statistics.
    HP = randint(5,20)
    MP = randint(5,20)

def villager():
    #This will create a randomly named Villager to interact with
    global npcname
    global response
    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = ["Hi", "Are you a hero?", "Are you from this village?", "There has been a dark shadow cast across the village"]
    npcnamechoice = ["Roger", "Dexter", "Sarah", "Susan"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
    print ("\n["+npcname+":] Hello, my name is "+npcname+", Would you like to talk to me?\n")
    shuffle(responses)
    print ("Press y to talk to the villager")
    if input() == "y":
        print ("["+npcname+":] " +responses[0])
    else:
        print("["+npcname+":] Goodbye")

def enemy():
    global enemyHP
    global enemyMP
    global enemyname
    
    
    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemynamechoice = ["Ogre", "Drac"]
    shuffle(enemynamechoice)
    enemyname = enemynamechoice[0]   
    if enemyname == "Drac":
       enemyHP = randint(10,30)
       enemyMP = randint(8,25)
    else:
       enemyHP = randint(5,20)
       enemyMP = randint(5,15)
    print ("\nSuddenly you hear a roar, and from the shadows you see an "+enemyname+" coming straight at you....")
    #print enemyname
    print ("Your enemy has " + " " + str(enemyHP) + " " + "Health Points")
    print ("Your enemy has " + " " + str(enemyMP) + " " + "Magic Points")

def heal():
    global HP  
    global MP
    print ("\nYour Helth Points are: " + str(HP) + " do you want a doctor? If you want type y")
    if input() == "y":
        print ("\nHello I'm Dr. Goozilla, I can heal you, but it costs 3 MP! Do you want this?")
        if input() == "y" and MP > 0:
           MP  = MP -3
           HP = randint (5,20)
           print ("\nYou are now healed! Your Health Points:" + " " + str(HP) + " " + "Your Magic Skill :" + " " + str(MP))
        else:
           print ("\nI can't heal you, because your Magic Skill is too less!")
           HP = 0
    else:
          print ("\n so you must die!")
          HP = 0
		  
		  def move():
	
#We now use our functions in the game code, we call the title, the castle picture and then ask the game to run the setup for our character.
clear_screen()
title()
castle()
setup()
global name
global HP
global MP
global move
global enemyHP
print ("Welcome to the land of Narule, "+name)
#Sleep is Python's way of pausing the game for a specified number of seconds
sleep(2)
#Below we are using the helper functions to join a string of text to an integer via the str() helper.
print ("\nYour health is" + " " + str(HP))
print ("Your magic skill is" + " " + str(MP))



print ("Would you like to venture out into the land? Press y then enter to continue")
#Below we use raw_input to ask for user input, and if it is equal to y, then the code underneath is run.
if input() == "y":
    print ("You are in your home, with a roaring fireplace in front of you, above the fire you can see your sword and shield")
    print ("Would you like to take your sword and shield? Press y then enter to continue")
    if input() == "y":
        #This is a list, and it can store many items, and to do that we "append" items to the list.
        weapons = []
        weapons.append("sword")
        weapons.append("shield")
        print ("You are now carrying your" + " " + weapons[0] + " " + "and your" + " " + weapons[1])
        print ("Armed with your " + weapons[0] + " " + "and " + weapons[1] + " you swing open the door to your home and see a green valley gleaming in the sunshine.")
    else:
        print ("You choose not to take your weapons")
        print ("Armed with your sense of humour, You swing open the door to see a green valley full of opportunity awaiting you.")
else:
    print ("You stay at home, sat in your favourite chair watching the fire grow colder. The land of Narule no longer has a hero.")
    print ("Game Over")
    sys.exit(0)
	
print ("In the distance to the north you can see a small village, to the east you can see a river and to the west a field of wild flowers.")

#Remember those functions we created at the start of the code? Well here we are using them in the game.
print ("\n")
north()
east()
south()
west()
m = input("Where would you like to go? ")
if m == 'n':
    print ("\nYou move to the north, walking in the sunshine.")
    print ("A villager is in your path and greets you")
#elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
elif m == 'e':
    print ("\nYou walk to the river which lies to the east of your home.")
    print ("A villager is in your path and greets you")
elif m == 'w':
    print ("\nYou walk to the field of wild flowers, stopping to take in the beauty")
    print ("A villager is in your path and greets you\n")
elif m == 's':
    print ("\nYou walk in too a deep and dark forest, and you are a little bit angshious")
	print ("\A villagert is in your path and greets you\n")
else 
	print ("\n You are staying here! The game ends.")
	sys.exit(0)
villager()
enemy()
sleep(3)

fight = input("Do you wish to fight?" )

if fight == "y":
    while HP > 0 and enemyHP >0:
#This loop will only work while our characters HP is greater than 0.
        hit = randint(0,5)
        print ("You swing your sword and cause " + str(hit) + " of damage")
        enemyHP = enemyHP - hit
        if enemyHP < 1:
          mp = randint(5,20)
          hp = randint(5,20)
          print("\nGratulation! You won and got:" + " " + str(mp) + " " + "Magic Points and: " + " " + str(hp) + " " + "Health Points")
          HP = HP + hp
          MP = MP + mp
          print ("\n You have:" + " " + str(HP) + " Health Points and: " + str(MP) + " Magic Points")
        else:   
          print ("\n The enemy has " + str(enemyHP) + "Helthpoints")
          enemyhit = randint(0,5)
          print ("\nThe " + enemyname + " swings a club at you and causes " + str(enemyhit) + " of damage")
          HP = HP - enemyhit
          print ("\nYou have: " + str(HP) + "Healthpoints")
        if HP < 0:
          heal()
else:
    print ("You turn and run away from the ogre")

print ("This is where this template ends, this is now YOUR world, build your adventure and share it with the world")

print ("   _       _                 _")
print ("  /_\   __| |_   _____ _ __ | |_ _   _ _ __ ___")
print (" //_\\ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ ")
print ("/  _  \ (_| |\ V /  __/ | | | |_| |_| | | |  __/")
print ("\_/ \_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|")

print ("                     _ _")
print ("  __ ___      ____ _(_) |_ ___")
print (" / _` \ \ /\ / / _` | | __/ __|")
print ("| (_| |\ V  V / (_| | | |_\__ \ ")
print (" \__,_| \_/\_/ \__,_|_|\__|___/")

print (" _   _  ___  _   _")
print ("| | | |/ _ \| | | |")
print ("| |_| | (_) | |_| |")
print (" \__, |\___/ \__,_|")
print (" |___/")
