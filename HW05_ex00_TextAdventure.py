#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body

def back_room(user_name):
    print(user_name  + " dare to get into this back door filled with awesome PYTHON programmers, rather to stay infinitively in the stairway room.")
    print("Here braveness will be payed with a secret question that only a phyton programer can answer: ")
    print(user_name + ", what is the Zen of Python?")
    next = input("> ")
    if next == 'import this':
        import this
        print ("Good programmer job!!!")
        exit(0)

def infinite_stairway_room(user_name, count=0):
    print(user_name  + " walks through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print(user_name  + ' takes the stairs')
        if (count > 0):
            print("but you're not happy about it")
        infinite_stairway_room(user_name, count + 1)
    # option 2 == ?????
    if next == 'back_door':
        back_room(user_name)
        pass


def gold_room(user_name):
    print("This room is full of gold.  How much does " + user_name  + " take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy goose!")


def bear_room(user_name):
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is " + user_name  + " going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if "take honey".find(next):
            dead("The bear looks at " + s  + " then slaps your face off.")
        elif next == "taunt" and not bear_moved:
            print("The bear has moved from the door. " + user_name  + " can go through it now.")
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif "open door".find(next) and bear_moved:
            gold_room(user_name)
        else:
            print("I got no idea what that means.")


def cthulhu_room(user_name):
    print("Here " + user_name  + " see the great evil Cthulhu.")
    print("He, it, whatever stares at " + user_name  + " and " + user_name  + " go insane.")
    print("Do you flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        infinite_stairway_room(user_name)
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(user_name)


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    user_name = input('What is your name: ')
    # START the TextAdventure game
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one does " + user_name  + " take?")

    next = input("> ")

    if next == "left":
        bear_room(user_name)
    elif next == "right":
        cthulhu_room(user_name)
    else:
        dead(user_name  + " stumble around the room until you starve.")

if __name__ == '__main__':
    main()
