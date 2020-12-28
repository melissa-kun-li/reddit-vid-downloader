import json
import requests

url = input('Please enter the Reddit link which has the Reddit embedded video: ')
info = {'user-agent':'vdownloader by /u/panaora'}
response = requests.get(url + '.json', headers = info)
data = response.json()

def test():
    parse = data[0]['data']['children']
    video_link = parse[0]['data']['secure_media']['reddit_video']['fallback_url'][:-16]
    print(video_link)
    
test()
