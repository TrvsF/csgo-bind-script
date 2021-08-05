from colorama import Fore
from shutil import copy
import os

fullList = []
csgoPath = "D:/games/steamapps/common/Counter-Strike Global Offensive/csgo/cfg" # change me
csgoFile = csgoPath + "/random_bind.cfg"

def addMessage(message):

    print("adding message {0}".format(message))

    print("reading lines..")
    file = open("./random_bind.cfg")
    fullList = file.readlines()
    print("cleaning..")
    fullList = [line.replace("\n", "") for line in fullList]

    messageList = []

    print("scanning for messages..")

    messageCount = 0
    shouldRead = False
    for line in fullList:
        if (line == "// init the custom messages"):
            print("found messages, reading..")
            shouldRead = True

        if (shouldRead and line == ""):
            shouldRead = False
            break

        if (shouldRead):
            if (line[:2] == "//"):
                continue
            messageList.append(line)
            messageCount += 1

    print("found {0} messages".format(messageCount))
    print("adding new message..")

    messageList.append('alias "message_{0}" "{1}"'.format(messageCount + 1, message))

    print("adding logic..")
    

def getBanner():
    banner = f'''


                                               /$$       /$$                 /$$          
                                              | $$      |__/                | $$          
  /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$       | $$$$$$$  /$$ /$$$$$$$   /$$$$$$$  /$$$$$$$
 /$$_____/ /$$_____/ /$$__  $$ /$$__  $$      | $$__  $$| $$| $$__  $$ /$$__  $$ /$$_____/
| $$      |  $$$$$$ | $$  \ $$| $$  \ $$      | $$  \ $$| $$| $$  \ $$| $$  | $$|  $$$$$$ 
| $$       \____  $$| $$  | $$| $$  | $$      | $$  | $$| $$| $$  | $$| $$  | $$ \____  $$
|  $$$$$$$ /$$$$$$$/|  $$$$$$$|  $$$$$$/      | $$$$$$$/| $$| $$  | $$|  $$$$$$$ /$$$$$$$/
 \_______/|_______/  \____  $$ \______/       |_______/ |__/|__/  |__/ \_______/|_______/ 
                     /$$  \ $$                                                            
                    |  $$$$$$/                                                            
                     \______/                                                             

                                            
                           
    '''.replace('█', f'{Fore.BLUE}█{Fore.RESET}')
    return banner

if __name__ == "__main__":
    print(getBanner())
    while(1):

        choice = input("[0] to copy file to csgo dir\n[1] to add new message\n[x] to exit\n")

        # copys file to given csgo dir (default is mine, change the csgoPath var if you want it somewhere else)
        if (choice == "0"):
            print("copying...")
            if (os.path.isfile(csgoFile)):
                os.remove(csgoFile)
            copy("./random_bind.cfg", csgoPath)
            print("done")
        
        # adds a given message to the cfg
        elif (choice == "1"):
            message = input("input new message\n")
            addMessage(message)

        elif (choice == "x"):
            print("exiting...")
            break

        else:
            print("unknown arg")

