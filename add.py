from colorama import Fore
from shutil import copy
import os

fullList = []
csgoPath = "D:/games/steamapps/common/Counter-Strike Global Offensive/csgo/cfg" # change me
csgoFile = csgoPath + "/random_bind.cfg"

def addMessage(message):

    print("adding message {0}".format(message))

    print("reading lines..")

    print("attempting to open temp file..")
    if (os.path.isfile("new_cfg.txt")):
        print("found")
        file = open("new_cfg.txt")
    else:
        print("not found, opening master instead..")
        file = open("./random_bind.cfg")

    fullList = file.readlines()
    file.close()
    print("cleaning..")
    fullList = [line.replace("\n", "") for line in fullList]

    messageList = []

    print("scanning for messages..")

    insertLine = 0
    messageCount = 0
    shouldRead = False
    for line in fullList:

        insertLine += 1

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
        
    print("found {0} messages!".format(messageCount))
    print("adding new message..")

    newMessage = 'alias "message_{0}" "say {1}"'.format(messageCount + 1, message)

    print("inserting new message..")
    fullList.insert(insertLine - 1, newMessage)

    print("adding logic..")

    rollCount = 0
    for line in fullList:

        rollCount += 1

        if ('alias "roll_{0}"'.format(messageCount) in line):
            break

    fullList.insert(rollCount - 1, 'alias "roll_{0}" "alias result message_{1}; alias cycle roll_{2}"'.format(messageCount, messageCount, messageCount + 1))
    fullList[rollCount] = fullList[rollCount].replace(str(messageCount), str(messageCount + 1))

    with open('new_cfg.txt', 'w') as f:
        for item in fullList:
            f.write("%s\n" % item)

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

        choice = input("[0] to copy file to csgo dir\n[1] to add new message\n[2] to overwrite old file with new\n[x] to exit\n")

        # copys file to given csgo dir (default is mine, change the csgoPath var if you want it somewhere else)
        if (choice == "0"):
            print("copying..")
            if (os.path.isfile(csgoFile)):
                os.remove(csgoFile)
            copy("./random_bind.cfg", csgoPath)
            print("done")
        
        # adds a given message to the cfg
        elif (choice == "1"):
            message = input("input new message\n")
            addMessage(message)

        elif (choice == "2"):
            print("overwriting..")
            if (os.path.isfile("./random_bind.cfg")):
                os.remove("./random_bind.cfg")
            with open('./random_bind.cfg', 'a') as f1:
                for line in open('new_cfg.txt'):
                    f1.write(line)
            print("done")

        elif (choice == "x"):
            print("exiting..")
            break

        else:
            print("unknown arg")

