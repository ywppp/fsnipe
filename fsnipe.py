# fsnipe is created by @ywp#6969 -- do not distrubute this code for monetary gain, though feel
# free to use anything from here in your own snipers.
# imports
import os
import sys
import re
import requests
import datetime
import time
import json
from threading import *
from colored import fg, bg, attr

# colors w/ colored package
green = fg('green')
error = fg('light_red')
text = fg('light_yellow')
logo = fg('light_cyan')
ntext = fg('white')
p = fg('deep_pink_4c')
skyblue = fg('sky_blue_2')
orchid = fg('orchid')
blue = fg('cadet_blue_2')

# create user input lists
yes = {'yes', 'y', 'YES', 'Y', 'ye', 'YE'}
no = {'no', 'n', 'NO', 'N'}

# define variables
firstEmail = ""
firstPass = ""
firstBearer = ""
firstID = ""
secondEmail = ""
secondPass = ""
secondBearer = ""
secondID = ""
thirdEmail = ""
thirdPass = ""
thirdBearer = ""
thirdID = ""
fourthEmail = ""
fourthPass = ""
fourthBearer = ""
fourthID = ""


# fsnipe logo:
os.system('clear') # mac users
os.system('cls') # windows users
print("")
print(p + "███████╗███████╗███╗   ██╗██╗██████╗ ███████╗")
print(p + "██╔════╝██╔════╝████╗  ██║██║██╔══██╗██╔════╝")
print(p + "█████╗  ███████╗██╔██╗ ██║██║██████╔╝█████╗  ")
print(p + "██╔══╝  ╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ")
print(p + "██║     ███████║██║ ╚████║██║██║     ███████╗")
print(p + "╚═╝     ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝")
print(error + "v1.0 | STABLE | " + orchid + "made by " + skyblue + "@ywp#6969")
print("")
print("")


# Gather information:
wanted_name = input(logo + "[INFO] " + ntext + "Desired Name | " + text + "")
dropTime = input(logo + "[INFO] " + ntext + "Drop Time [2 seconds prior to drop] | " + text + "")
choice = input(logo + "[INFO] " + ntext + "Scan accounts (yes/no) | " + text + "")
if choice in yes: # if the choice is in the list, scan accounts
    f = open("accounts.txt", "r") # open "accounts.txt" file from snipes folder
    accounts = f.read() # read the file and label as "accounts"
    accounts_split = re.split(':|\n', accounts) # use regex to split the accounts at ":" and "\n" for parsing
    firstEmail = accounts_split[0] 
    firstPass = accounts_split[1] 
    secondEmail = accounts_split[2] 
    secondPass = accounts_split[3]
    thirdEmail = accounts_split[4]
    thirdPass = accounts_split[5]
    fourthEmail = accounts_split[6]
    fourthPass = accounts_split[7]
    # log in with accounts here
    url2 = 'https://authserver.mojang.com/authenticate'
    secure = 'https://api.mojang.com/user/security/challenges'
    # account 1:
    # get authentication bearer
    responseJSON = requests.post(url2, json={"agent": {"name": "Minecraft", "version": 1},"username": firstEmail,"password": firstPass}) # get info from mojang's servers
    print(logo + "[CHECK] " + ntext + "Response from Mojang | " + error + str(responseJSON))
    parsedJSON = json.loads(responseJSON.text) # parse through info to get the response from json to string
    token = parsedJSON['accessToken'] # get only the accessToken
    firstBearer = "Bearer " + token # create bearer
    firstID = parsedJSON['availableProfiles'][0]['id'] # get UUID
    firstName = parsedJSON['availableProfiles'][0]['name'] # get username
    securereq = requests.get(secure, headers={'Authorization': firstBearer})

    # account 2:
    # get authentication bearer
    responseJSON = requests.post(url2, json={"agent": {"name": "Minecraft", "version": 1},"username": secondEmail,"password": secondPass}) # get info from mojang's servers
    print(logo + "[CHECK] " + ntext + "Response from Mojang | " + error + str(responseJSON))
    parsedJSON = json.loads(responseJSON.text) # parse through info to get the response from json to string
    token = parsedJSON['accessToken'] # get only the accessToken
    secondBearer = "Bearer " + token # create bearer
    secondID = parsedJSON['availableProfiles'][0]['id'] # get UUID
    secondName = parsedJSON['availableProfiles'][0]['name'] # get username
    securereq = requests.get(secure, headers={'Authorization': secondBearer})
    

    # account 3:
    # get authentication bearer
    responseJSON = requests.post(url2, json={"agent": {"name": "Minecraft", "version": 1},"username": thirdEmail,"password": thirdPass}) # get info from mojang's servers
    print(logo + "[CHECK] " + ntext + "Response from Mojang | " + error + str(responseJSON))
    parsedJSON = json.loads(responseJSON.text) # parse through info to get the response from json to string
    token = parsedJSON['accessToken'] # get only the accessToken
    thirdBearer = "Bearer " + token # create bearer
    thirdID = parsedJSON['availableProfiles'][0]['id'] # get UUID
    thirdName = parsedJSON['availableProfiles'][0]['name'] # get username
    securereq = requests.get(secure, headers={'Authorization': thirdBearer})

    # account 4:
    # get authentication bearer
    responseJSON = requests.post(url2, json={"agent": {"name": "Minecraft", "version": 1},"username": fourthEmail,"password": fourthPass}) # get info from mojang's servers
    print(logo + "[CHECK] " + ntext + "Response from Mojang | " + error + str(responseJSON))
    parsedJSON = json.loads(responseJSON.text) # parse through info to get the response from json to string
    token = parsedJSON['accessToken'] # get only the accessToken
    fourthBearer = "Bearer " + token # create bearer
    fourthID = parsedJSON['availableProfiles'][0]['id'] # get UUID
    fourthName = parsedJSON['availableProfiles'][0]['name'] # get username
    securereq = requests.get(secure, headers={'Authorization': fourthBearer})

    # print success statements
    print(logo + "[INFO] " + ntext + "Finished scanning accounts")
    print(logo + "[INFO] " + ntext + "Logging in...")
    print(green + "[SUCCESS] " + ntext + "Successfully logged in as: " + firstEmail + " (" + firstName + ")")
    print(green + "[SUCCESS] " + ntext + "Successfully logged in as: " + secondEmail + " (" + secondName + ")")
    print(green + "[SUCCESS] " + ntext + "Successfully logged in as: " + thirdEmail + " (" + thirdName + ")")
    print(green + "[SUCCESS] " + ntext + "Successfully logged in as: " + fourthEmail + " (" + fourthName + ")")

elif choice in no: # exit fsnipe
    sys.exit(logo + "[INFO] " + ntext + "Exiting...\n")
else: # give error to respond with proper format
    sys.exit(error + "[ERROR] " + ntext + "Please respond with 'yes' or 'no'\n" + text + "")

time.sleep(0.5)
print("")
print(orchid + "[INFO] " + ntext + "Locked in with | " + text + wanted_name)
print("")
print(orchid + "[INFO] " + ntext + "Dropping Time | " + text + dropTime)

# Threads: Running 4 threads - 1 for each account - with 20 requests in each - 4x1x20 = 80 requests total

class firstSniper(Thread):
    def run(self):
        for i in range (20):
            url = 'http://api.mojang.com/user/profile/' + firstID + '/name'
            req = requests.post(url, headers={'Authorization': firstBearer}, json={"name": wanted_name,"password": firstPass})
            if req.status_code == 204:
                sys.exit(green + "[SUCCESS] " + ntext + "Succesfully sniped account | " + text + wanted_name + " | " + ntext + fourthEmail)
            else:
                print(error + "[ERROR] " + ntext + "Failed to snipe " + text + wanted_name)

class secondSniper(Thread):
    def run(self):
        for i in range (20):
            url = 'http://api.mojang.com/user/profile/' + secondID + '/name'
            req = requests.post(url, headers={'Authorization': secondBearer}, json={"name": wanted_name,"password": secondPass})
            if req.status_code == 204:
                sys.exit(green + "[SUCCESS] " + ntext + "Succesfully sniped account | " + text + wanted_name + " | " + ntext + fourthEmail)
            else:
                print(error + "[ERROR] " + ntext + "Failed to snipe " + text + wanted_name)

class thirdSniper(Thread):
    def run(self):
        for i in range (20):
            url = 'http://api.mojang.com/user/profile/' + thirdID + '/name'
            req = requests.post(url, headers={'Authorization': thirdBearer}, json={"name": wanted_name,"password": thirdPass})
            if req.status_code == 204:
                sys.exit(green + "[SUCCESS] " + ntext + "Succesfully sniped account | " + text + wanted_name + " | " + ntext + fourthEmail)
            else:
                print(error + "[ERROR] " + ntext + "Failed to snipe " + text + wanted_name)

class fourthSniper(Thread):
    def run(self):
        for i in range (20):
            url = 'http://api.mojang.com/user/profile/' + fourthID + '/name'
            req = requests.post(url, headers={'Authorization': fourthBearer}, json={"name": wanted_name,"password": fourthPass})
            if req.status_code == 204:
                sys.exit(green + "[SUCCESS] " + ntext + "Succesfully sniped account | " + text + wanted_name + " | " + ntext + fourthEmail)
            else:
                print(error + "[ERROR] " + ntext + "Failed to snipe " + text + wanted_name)

while True:
    time_str = datetime.datetime.now().strftime("%H:%M:%S")
    if time_str == dropTime:
        threadFirst = firstSniper()
        threadFirst.start()
        threadSecond = secondSniper()
        threadSecond.start()
        threadThird = thirdSniper()
        threadThird.start()
        threadFourth = fourthSniper()
        threadFourth.start()