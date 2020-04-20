
import csv, sys, re


depApp = repo.search("adm.DeployApplication") # searching deployed application

with open('C:\Ashok\Scripts\DeploymentInfo1.csv', 'wb') as new_file:
	fieldnames = ['Environment', 'Full_Environment_Name', 'Package', 'VM', 'Current_Builds','Deployed Date', 'Deployed Time' , 'Deployed By']
	csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
	csv_writer.writeheader()
	
	for app in depApp:
		theApp = repo.read(app) # reading all the deployed application 
		FullVersion = theApp.version # getting application full current verion that deployed
		FullEnv = theApp.id #getting Environment ID
		
		eachbuild = repo.read(FullVersion) # reading full current verison 
		if eachbuild.type == 'adm.CompPackage': # checking for composite package
			GetEnv = FullEnv.split('/') # splitting the environment id 
			#CurrentZZName = re.sub("^.*/", "", app) # getting app name
			CurrentVersion = re.sub("^.*/", "", theApp.version) # getting version name
			build = eachbuild.packages  # getting all build that composite package have
			getDeployeds = theApp.deployeds # getting all Infrastructure that these build deployed
			getWar = [i for i in getDeployeds if ".war" in i] # looking for war file only Infrastructure

			res = [] 
			for i in getWar:
				res.append(i.split('/'))
			
			VMs = []
			for i in range(0, len(res)):
				VMs.append(res[i][-4])
			
			warVMs = list(set(VMs))
			
			warVMs.sort()
			build.sort()
			
			builds = str(build).replace('App/', '').replace('[', '').replace(']','')
			deplotedVM = str(warVMs).replace("[u","").replace("u",'').replace("]",'').replace("'",'')
			
			appid = repo.read(FullEnv)
			attributes = appid.attributes
			getTime = attributes.ModifiedAt
			getUser = attributes.ModifiedBy	
			timeStamp = str(getTime).replace('T', '').replace('Z', '')
			getdate = timeStamp[0:10]
			gettime = timeStamp[10:-4]
			
			csv_writer.writerow({'Environment':GetEnv[-2],'Full_Environment_Name':FullEnv.replace('Env/', ''),'Package': CurrentVersion,'VM': deplotedVM, 'Current_Builds': builds, 'Deployed Date': getdate, 'Deployed Time': gettime,'Deployed By':getUser})
			
