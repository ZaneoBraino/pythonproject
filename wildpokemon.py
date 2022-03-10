#!/usr/bin/python3
import json
import requests
import random
import time

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    for i in range(1):
        randomnumber = random.randint(1, 948)
        print(randomnumber)
        #searches the random pokmon from the randim number from above
        #pokemon = requests.get(f"{POKEURL}?limit=948")
        #pokemon = pokemon.json()

        #Iterate over the result and show the pokemon
        #allpokemon = [0]
        #for poke in pokemon["results"][randomnumber]:
            
            #print("A wild " + poke.get("name") + " appears!")
        req = requests.get('http://pokeapi.co/api/v2/pokemon/' + str(randomnumber)  + '/')
        #print("HTTP Status Code: " + str(req.status_code))
        #print(req.headers)
        json_response = json.loads(req.content)
        pokename = json_response['name']
        print("A wild " + pokename + " appears!")
        print(f"1. Throw ball \n 2. Run away \n")
        userchoice = int(input("What will you do?\n"))
        if (userchoice == 1):
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
                    print("Good job!  You caught " + pokename + "!")
                if (catchrate < 6):
                    print("Oh no! " + pokename + " got away!")

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
                    print("Good job!  You caught " + pokename + "!")
                if (catchrate < 4):
                    print("Oh no! " + pokename + " got away!")

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
                    print("Good job!  You caught " + pokename + "!")
                if (catchrate < 2):
                    print("Oh no! " + pokename + " got away!")

            if (ballchoice == 4):
                print("You threw a Master ball!")
                print("ding!\n")
                time.sleep(1)
                print("booo-op\n")
                time.sleep(1)
                print("doooo-op\n")
                time.sleep(1)
                print("Ding! You caught" + pokename + "!")
        if (userchoice == 2):
            print("You got away safely!")

if __name__ == "__main__":
    main()

