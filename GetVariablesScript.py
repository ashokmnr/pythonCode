import datetime
import re
import urllib2


def do_request(url):  # funcation for url request
    request = urllib2.Request(url)
    return urllib2.urlopen(request).read()


curdate = datetime.datetime.now().strftime("%m-%d-%Y")
relVariables["Releasedate"] = curdate

PortalURL = ""
PortalURLresponse = do_request(PortalURL)
findPortal = (
    re.search("Version : .*?<", PortalURLresponse)
    .group(0)
    .replace("Version : ", "")
    .replace("<", "")
)
relVariables["PortalBuild"] = findPortal

HomeURL = ""
HomeURLresponse = do_request(HomeURL)
findHome = (
    re.search("Version : .*?<", HomeURLresponse)
    .group(0)
    .replace("Version : ", "")
    .replace("<", "")
)
relVariables["HomeBuild"] = findHome


bpath = r"\\ashok\Build\05.04.01.0012"
getbBuild = bpath.split("\\")
relVariables["BBuild"] = getbBuild[-1]
