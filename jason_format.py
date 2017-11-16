import json
from pprint import pprint
from collections import OrderedDict

fil = open('stream_INDIA.txt','r')

class JSONObject:
    def __init__(self , d):
        self.__dict__ = d

##
for k in range(100):
    data = fil.readline()
    resp = json.loads(data.decode('utf-8'))
    #print "-------------"
    #pprint(resp)
    caz = json.loads(data , object_pairs_hook= OrderedDict)
    #print "-------------"
    #print caz
    az = json.loads(data , object_hook= JSONObject)
    #print "-------------"
    b = az.user
    if b.verified == True:
        print pprint(resp)
        break



data = fil.readline()
resp = json.loads(data.decode('utf-8'))
caz = json.loads(data , object_pairs_hook= OrderedDict)
az = json.loads(data , object_hook= JSONObject)
b = az.user
print b.entities
