
import socket
import keyboard

def start_input():
   #starting run to open the commandline
    keyboard.send("windows+r")
    keyboard.write("powershell")
    keyboard.send("enter")
    setup_input()

# inputing command to install ssh server
def setup_input(): 
    keyboard.write("Start-Service ssh-agent")
    keyboard.send("enter")

start_input()
