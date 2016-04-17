import urllib2
import json
//opens a website
response= urllib2.urlopen("https://rumobile.rutgers.edu/1/rutgers-dining.txt")
//reads the response and then load as json, [0] because it first loads as a list, so we want
//the first and only object in there. so now diningHall is a dict
diningHall = json.loads(response.read())[0]
print  json.dumps(diningHall, sort_keys=True, indent=4, separators=(',', ': '))
print type(diningHall)
