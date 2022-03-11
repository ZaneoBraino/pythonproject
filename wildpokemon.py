#!/usr/bin/python3
import json
import requests
import random
import time

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

#A function that has different odds based on what ball the user picks
def balloptions(pokename):
    ballchoice = int(input("What kind of ball do you want to use?\n 1.Pokeball\n 2.Great ball\n 3.Ultra ball\n 4.Master ball\n"))
    if (ballchoice == 1):
        print("You threw a pokeball!")
        print("ding!\n")
        time.sleep(1)
        print("booo-op\n")
        time.sleep(1)
        print("doooo-op\n")
        time.sleep(1)
        catchrate = random.randint(1, 10)
        if (catchrate > 6):
            return True
        if (catchrate < 6):
            return False

   

    if (ballchoice == 2):
        print("You threw a Great ball!")
        print("ding!\n")
        time.sleep(1)
        print("booo-op\n")
        time.sleep(1)
        print("doooo-op\n")
        time.sleep(1)
        catchrate = random.randint(1, 10)
        if (catchrate > 4):
            return True
        if (catchrate < 4):
            return False

    if (ballchoice == 3):
        print("You threw a Ultra ball!")
        print("ding!\n")
        time.sleep(1)
        print("booo-op\n")
        time.sleep(1)
        print("doooo-op\n")
        time.sleep(1)
        catchrate = random.randint(1, 10)
        if (catchrate > 2):
            return True
        if (catchrate < 2):
            return False

    if (ballchoice == 4):
        print("You threw a Master ball!")
        print("ding!\n")
        time.sleep(1)
        print("booo-op\n")
        time.sleep(1)
        print("doooo-op\n")
        time.sleep(1)
        return True



def main():
    userchoice = 0
    userspokemon = []
    while(userchoice <= 2):
        userchoice = 0

        print(f"1. Go find a wild pokemon \n 2. Check current pokemon \n 3. Quit game \n")
        userchoice = int(input("Hello trainer, what would you like to do?\n"))
        if(userchoice == 1):
            for i in range(1):
                userchoice = 0
                #Selects a random pokemon from the PokeAPI
                randomnumber = random.randint(1, 948)
                print(randomnumber)
                #Goes to the API itself and gets the same of said pokemon via the random number
                req = requests.get('http://pokeapi.co/api/v2/pokemon/' + str(randomnumber)  + '/')
                json_response = json.loads(req.content)
                pokename = json_response['name']

                print("A wild " + pokename + " appears!")
                print(f"1. Throw ball \n 2. Run away \n")
                userchoice = int(input("What will you do?\n"))
                if (userchoice == 1):
                    #calls a function to ask the user what kind of ball they wish to use
                    #then returns true or false based on the chance of the ball
                    #if successful the pokemon will be stored in a list or they'll get away
                    if (balloptions(pokename) == True):
                        print("Good job!  You caught " + pokename + "!i\n")
                        userspokemon.append(pokename)
                    else:
                        print("Oh no! " + pokename + " got away!\n")

                    if (userchoice == 2):
                        print("You got away safely")
        #prints out the users pokemon theyve caught                
        if(userchoice == 2):
            print("Your current pokemon are: \n")
            print(str(userspokemon))
        #quits out of the program    
        if(userchoice == 3):
            print("Thank you for playing and have a good day")
            break
if __name__ == "__main__":
    main()

