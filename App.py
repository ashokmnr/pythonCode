import csv
import re
import urllib2
import base64


def do_request(url, username, password): # funcation for api request 
    request = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
    request.add_header("Authorization", "Basic %s" % base64string)
    return urllib2.urlopen(request).read(245)
