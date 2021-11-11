# YOU MAY GET BANNED USING THIS ! DISCORD TOS
# YOU CAN ONLY USE TWITCH AND YOUTUBE LINK !

# Need help ? DM me on discord punch-hax 〄#3174
# https://github.com/punch-hax

import os       ; from os import system
import json     ; from json import load
import time     ; from time import sleep
import discord  ;
import requests ;

def clear():
    system("cls")

def main():

    client = discord.Client()

    if os.path.isdir("config"): # avec le dossier config

        edit = input("Do you want to edit your config? (y/n) ")

        if edit == "y":
            system("cd config & del token.json & del link.json & del streamname.json & cd .. & rd config")

        if edit == "n":

            clear() ; print("Config loaded !") ; sleep(2)

            with open("config/token.json") as f:
                token = load(f)

            token = token.get("token")

            with open("config/streamname.json") as f:
                streamname = load(f)

            streamname = streamname.get("streamname")

            with open("config/link.json") as f:
                link = load(f)

            link = link.get("link")


    if not os.path.isdir("config"): # sans le dossier config

        clear() ; print("We need some info !")

        save = input("Do you want to save your info ? (y/n) ") ; clear()

        token = input("token# ") # mettre le token
        link = input("link# ") # mettre le lien youtube / twitch
        streamname = input("streamname# ") # mettre le nom du stream

        if save == "y":

            system("mkdir config") # créer le dossier config ou les fichiers .jsons se mettront
            system("cd config & echo {\"token\": \"" + token + "\"} > token.json") # créer le fichier token.json
            system("cd config & echo {\"link\": \"" + link + "\"} > link.json") # créer le fichier link.json
            system("cd config & echo {\"streamname\": \"" + streamname + "\"} > streamname.json") # créer le fichier streamname.json

            print("\nInfo saved !")

    def veriftoken():

        headers = { 
                "Content-Type": "application/json", 
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
                "Authorization": token
        }

        r = requests.get("https://discord.com/api/users/@me", headers = headers)

        if r.status_code == 200:
            print("Valid token !") ; sleep(2)
        else:
            print("Invalid token !") ; sleep(2) ; exit

    @client.event
    async def on_ready():

        clear() ; print(f"User : {client.user.name} ({client.user.id})") 
        
        await client.change_presence(activity = discord.Streaming(name = streamname, url = link)) # changement du status

        print() ; print(f"Streaming {link} ! Press CTRL+C to stop.")
        print() ; print("Need help ? DM me on discord punch-hax 〄#3174") ; print("https://github.com/punch-hax")

    veriftoken() ; client.run(token, bot = False) # vérification et connection au token

main()
