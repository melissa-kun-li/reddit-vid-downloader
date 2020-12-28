import json
import requests

url = input('Please enter the Reddit link which has the Reddit embedded video: ')
info = {'user-agent':'vdownloader by /u/panaora'}
response = requests.get(url + '.json', headers = info)
data = response.json()

def test():
    for item in data: # item = first {'kind':}
        for j in item['data']['children']: # should give us second {'kind':}
            print(j['data']['secure_media']['reddit_video']['fallback_url'][:-16]) # video mp4 link
            return 
test()
