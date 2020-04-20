import csv, sys
import re
import urllib2
import base64

username = sys.argv[1]
password = sys.argv[2]


def do_request(url, username, password):
    request = urllib2.Request(url)
    base64string = base64.encodestring("%s:%s" % (username, password))[:-1]
    request.add_header("Authorization", "Basic %s" % base64string)
    return urllib2.urlopen(request).read(300)


depApp = repo.search("adm.DeployApplication")

with open("C:\Ashok\Scripts\Work\Info1.csv", "wb") as new_file:
    fieldnames = [
        "Environment",
        "Full_Environment_Name",
        "Package",
        "VM",
        "Current_Builds",
        "Deployed_Time",
    ]
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    for app in depApp:
        theApp = repo.read(app)
        FullVersion = (
            theApp.version
        )  # getting application full current verion that deployed
        FullEnv = theApp.id  # getting Environment ID
        eachbuild = repo.read(FullVersion)  # reading full current verison
        if eachbuild.type == "adm.CompPackage":  # checking for composite package
            GetEnv = FullEnv.split("/")  # splitting the environment id
            CurrentName = re.sub("^.*/", "", app)  # getting app name
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

            deplotedVM = (
                str(warVMs)
                .replace("[u", "")
                .replace("u", "")
                .replace("]", "")
                .replace("'", "")
            )

            url = "url" + FullEnv

            response = do_request(url, username, password)
            findTime = re.search('last-modified-at="(.+?)">', response)
            getTime = findTime.group(1)

            csv_writer.writerow(
                {
                    "Environment": GetEnv[-2],
                    "Full_Environment_Name": FullEnv,
                    "Package": CurrentName + "(" + CurrentVersion + ")",
                    "VM": deplotedVM,
                    "Current_Builds": str(build).replace("[", "").replace("]", ""),
                    "Deployed_Time": getTime,
                }
            )
