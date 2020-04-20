import csv
import sys
import re
from org.joda.time import DateTime

depApp = repo.search("adm.DeployApplication")  # searching deployed application

with open("D:\Scripts\Ashok\Report\DeployInfo1.csv", "wb") as new_file:
    fieldnames = [
        "Environment",
        "Full_Environment_Name",
        "Package",
        "VM",
        "Current_Builds",
        "Deployed Date",
        "Deployed Time",
        "Deployed By",
    ]
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    for app in depApp:
        theApp = repo.read(app)  # reading all the deployed application
        FullVersion = (
            theApp.version
        )  # getting application full current verion that deployed
        FullEnv = theApp.id  # getting Environment ID
        eachbuild = repo.read(FullVersion)  # reading full current verison
        if eachbuild.type == "adm.CompoPackage":  # checking for composite package
            GetEnv = FullEnv.split("/")  # splitting the environment id
            # CurrentZZName = re.sub("^.*/", "", app) # getting app name
            CurrentVersion = re.sub("^.*/", "", theApp.version)  # getting version name
            build = eachbuild.packages  # getting all build that composite package have
            getDeployeds = (
                theApp.deployeds
            )  # getting all Infrastructure that these build deployed
            getWar = [
                i for i in getDeployeds if ".war" in i
            ]  # looking for war file only Infrastructure

            res = []
            for i in getWar:
                res.append(i.split("/"))

            VMs = []
            for i in range(0, len(res)):
                VMs.append(res[i][-4])

            warVMs = list(set(VMs))

            warVMs.sort()
            build.sort()

            builds = (
                str(build)
                .replace("Applications/", "")
                .replace("[", "")
                .replace("]", "")
            )
            deplotedVM = (
                str(warVMs)
                .replace("[u", "")
                .replace("u", "")
                .replace("]", "")
                .replace("'", "")
            )

            appid = repo.read(FullEnv)
            attributes = appid.attributes
            getTime = attributes.lastModified
            getUser = attributes.lastModified
            time = str(getTime).replace("T", "").replace("Z", "")
            getdate = time[0:10]
            gettime = time[10:-4]

            csv_writer.writerow(
                {
                    "Environment": GetEnv[-2],
                    "Full_Environment_Name": FullEnv.replace("Environments/", ""),
                    "Package": CurrentZZVersion,
                    "VM": deplotedVM,
                    "Current_Builds": builds,
                    "Deployed Date": getdate,
                    "Deployed Time": gettime,
                    "Deployed By": getUser,
                }
            )
