
import os, datetime

path = "${package_PATH}"
packFile = open("D:/Ashok/tmp/Daily_${LOB}-${prog}.txt", "r")
packFileContents = packFile.readlines()
dictionaries = {}
for i in range(0, len(packFileContents)):
	splitapp = packFileContents[i].split('/')
	dictionaries[splitapp[0].strip()] = splitapp[1].strip()

packFile.close()

envFile = open("D:/Ashok/env.txt", "r")
envFileContents = envFile.readlines()
envPath = envFileContents[0]
envFile.close()

relVariables['Env'] = "${Env}"

checkLOB = "${LOB}"
 
if checkLOB == "P":
    relVariables['TestParameter'] = ("APP_G_Build:" + dictionaries.get('C_${prog}') + "##APP_G_Build:"
    +dictionaries.get('B_${prog}') + "##APP_G_Build:" + dictionaries.get('P_${prog}'))
    
    fullPath = path + "/" + dictionaries.get('Z_${prog}')
    relVariables['Package'] = fullPath
    
    currentDT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    changeTime = str(currentDT).replace(" ","").replace("-","").replace(":","_")
    dropPath = "\\\\ashok\\App\\Test\\"+fullPath+"/${Env}\\"+changeTime
    relVariables['dropPath'] = dropPath
else:
    print("Env not found")
