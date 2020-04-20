import csv, os, sys

filePath = sys.argv[1]
prodForce = sys.argv[2].lower()
txt_file = filePath + "\App.txt"

if os.path.exists(txt_file):
    in_txt = open(txt_file, "r")
    packFileContents = in_txt.readlines()
    for i in range(2, len(packFileContents)):
        if not packFileContents[i].strip():
            continue
        fullPath = filePath + "\\" + packFileContents[i].strip()
        print "Passing full path " + fullPath
        infoFileSplit = fullPath.split("\\")
        in_txt.close()
        serverDictMembers = []
        globelAppMembers = []
        remEmptyData = filter(None, infoFileSplit)
        dictName = remEmptyData[4].replace("Build", "")
        domainName = remEmptyData[7].strip().replace(".txt", "")
        folderName = domainName[0]
        serverName = domainName[-2:]
        lineOfBus = domainName[3:-2]

        if lineOfBus == "UDOC":
            lineOfBus = "UM"

        restrictApp = "Applications/Ashok/" + lineOfBus + "/" + dictName

        if repo.exists(restrictApp) != True:
            restrictApp = "Applications/Ashok/EB/" + dictName
        if repo.exists(restrictApp) != True:
            restrictApp = "Applications/Ashok/FT/" + dictName

        if folderName == "D":
            folderName = "DEV"
            if serverName == "01":
                serverName = "Env1"
            else:
                serverName = "Env2"
        elif folderName == "Q":
            folderName = "QA"
            if serverName == "01":
                serverName = "Env1"
            else:
                serverName = "Env2"
        elif folderName == "U":
            folderName = "UAT"
            if serverName == "01":
                serverName = "Env1"
            else:
                serverName = "Env2"
        elif folderName == "P" and prodForce == "prod":
            folderName = "PROD"
            if serverName == "01":
                serverName = "Env1"
            elif serverName == "02":
                serverName = "Env2"
            else:
                serverName = "Env3"
        else:
            print "Please enter prod as parameter"

        globelDictRestrict = globelDict.restrictApplications
        for restrictDict in globelDictRestrict:
            globelAppMembers.append(restrictDict)
            globelAppMembers.append(restrictApp)
            globelDict.restrictApplications = globelAppMembers
            repo.update(globelDict)
            print "Saving Globel members " + folderName + "/" + serverName + "/Dom/" + domainName + "_Dict/a_Global_" + domainName + "_Dict"

        serverDict = serverEnv.dictionaries
        for dict in serverDict:
            serverDictMembers.append(dict)
            serverDictMembers.append(createDict.id)
            serverEnv.dictionaries = serverDictMembers
            repo.update(serverEnv)
            print "Saving Dictionary Members " + folderName + "/" + serverName + "/Dom/" + domainName
else:
    print (txt_file + " File does not exists!!!")
