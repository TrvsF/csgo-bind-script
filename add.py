fullList = []

if __name__ == "__main__":
    print("starting..")

    # read file
    file = open("./random_bind.cfg")
    fullList = file.readlines()

    messageList = []

    print("loading messages..")

    messageCount = 0
    shouldRead = False
    for line in fullList:

        if (shouldRead and line == "\n"):
            shouldRead = False
            print("done loading messages")
            print("found {0} messages".format(messageCount))

        if (shouldRead and line[:2] != "//"):
            messageList.append(line)
            messageCount += 1

        if (line.find("// init the custom messages")):
            shouldRead = True
            print("found message list..")

    for line in messageList:
        print(line)