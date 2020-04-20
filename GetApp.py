import os


def returnDeployVersion(applicationName):
    versions = repo.search("adm.DeployPackage", applicationName)
    sortedVersions = sorted_copy(versions)
    if len(sortedVersions) > 0:
        return sortedVersions[-1]
    else:
        return None


def returnCompVersion(applicationName):
    versions = repo.search("adm.CompPackage", applicationName)
    sortedVersions = sorted_copy(versions)
    if len(sortedVersions) > 0:
        return sortedVersions[-1]
    else:
        return None


path = "/ashok/Sol/Scripts/GetAppPackages/Apps/"
appFolder = "App/at/"
apps = ["Gapp", "Uapp", "Fapp", "Aapp", "Bapp"]
compApp = "App/Gapp/Eapp"
packageName = returnCompoVersion(compApp)
filename = ""

for i in range(0, len(apps)):
    last = returnVersion(appFolder + "/" + apps[i])

    splitAllapp = last.split("/")
    folder = splitAllapp[1]
    folderAdd = splitAllapp[2]
    full_name = folder + folderAdd
    try:
        os.chdir(path)
        filename = full_name + ".txt"
        if os.path.exists(filename):
            state = "a"
        else:
            state = "w"
        file = open(filename, state)
        appName = splitAllapp[-2]
        appId = splitAllapp[-1]
        fileValue = appName + " = " + appId + "\n"
        file.write(fileValue)
        file.close()

    except OSError:
        if not os.path.isdir(path):
            raise
split_char = packageName.split("/")
file2 = open(filename, state)
Comapp = split_char[-2]
ComId = split_char[-1]
comfileValue = Comapp + " = " + ComId + "\n"

file2.write(comfileValue)
file2.close()
