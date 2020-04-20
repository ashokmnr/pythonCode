import os
import sys


def deleteFile(path, full_name):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filename.endswith(full_name + ".txt"):
                os.chdir(path)
                os.remove(filename)


def getAppName(path, CompPackage, full_name):
    filename = ""
    compPY = repo.read(CompPackage)
    childNames = compPY.packages
    for i in range(0, len(childNames)):
        # splitAllapp = compApp.split("/")
        # folder = splitAllapp[1]
        # folderAdd = splitAllapp[2]
        # full_name = folder + folderAdd
        # full_name = sys.argv[0]
        try:
            os.chdir(path)
            filename = full_name + ".txt"
            if os.path.exists(filename):
                state = "a"
            else:
                state = "w"

            splitAll = childNames[i].split("/")
            file = open(filename, state)
            appName = splitAll[-2]
            appId = splitAll[-1]
            fileValue = appName + "/" + appId + "\n"
            file.write(fileValue)
            file.close()
        except OSError:
            if not os.path.isdir(path):
                raise
    split_char = CompPackage.split("/")
    if len(childNames) == 1:
        CompFile = open(filename, "a")
        Comapp = split_char[-2]
        ComId = split_char[-1]
        comfileValue = Comapp + "/" + ComId
        CompFile.write(comfileValue)
        CompFile.close()
    else:
        CompFile = open(filename, state)
        Comapp = split_char[-2]
        ComId = split_char[-1]
        comfileValue = Comapp + "/" + ComId
        CompFile.write(comfileValue)
        CompFile.close()
    print("Writing Deployment Package and Composite Package in text file !!!!!")
