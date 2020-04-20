import datetime
import re
import urllib2
import base64


def do_request(url, username, password):
    request = urllib2.Request(url)
    base64string = base64.encodestring("%s:%s" % (username, password))[:-1]
    request.add_header("Authorization", "Basic %s" % base64string)
    return urllib2.urlopen(request).read()


username = ""
password = ""

curdate = datetime.datetime.now().strftime("%m-%d-%Y")
print(curdate)

PortalURL = "put-url"
PortalURLresponse = do_request(PortalURL, username, password)
findPortal = (
    re.search("Version : .*?<", PortalURLresponse)
    .group(0)
    .replace("Version : ", "")
    .replace("<", "")
)
print(findPortal)


HomeURL = "put-url"
HomeURLresponse = do_request(HomeURL, username, password)
findHome = (
    re.search("Version : .*?<", HomeURLresponse)
    .group(0)
    .replace("Version : ", "")
    .replace("<", "")
)
print(findHome)

bpath = r"\\ashok\App\05.02.01.0105"
getbBuild = bpath.split("\\")
print(getbBuild[-1])

ppath = r"\\ashok\App\05.02.01.0105"
getpBuild = ppath.split("\\")
print(getpBuild[-1])
