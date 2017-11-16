import json
from pprint import pprint

fil = open('stream_INDIA.json','r')
tweets = []


for k in range(100):
    data = fil.readline()
    j = json.loads(data)
    if j['lang'] == 'en':
        tweets.append(j['text'])


for k in range(len(tweets)):
    print tweets[k]
