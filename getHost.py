#!/usr/bin/python3

import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

url = "url here"
auth = HTTPBasicAuth("username", "password")
post_request = requests.get(url=url, auth=auth)
soup = BeautifulSoup(post_request.text, "lxml")
HostList = []
print("Printing all the Hosts... \n")
for i in soup.findAll("ci"):
    HostlistDict = dict(i.attrs)
    for eachItem in HostlistDict.itervalues():
        if "Infra/DEV" in eachItem:
            print(eachItem)
            HostList.append(eachItem)
print("Python list populated. Printing it all the host...\n")
print(HostList)
