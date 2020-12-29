import json
import requests
import wget
import subprocess
# import ffmpeg
import os
import pathlib

url = input('Please enter the Reddit link which has the Reddit embedded video: ')
info = {'user-agent':'vdownloader by /u/panaora'}
response = requests.get(url + '.json', headers = info)
data = response.json()

def test():
    part = data[0]['data']['children']
    video_link = part[0]['data']['secure_media']['reddit_video']['fallback_url'][:-16]
    print(video_link)
    audio_link = video_link.split('_')[0] + '_audio.mp4'
    print(audio_link)
    
    wget.download(video_link) # /Users/melissali/Documents/reddit_vid_downloader/DASH_1080.mp4
    wget.download(audio_link) # /Users/melissali/Documents/reddit_vid_downloader/DASH_audio.mp4

    subprocess.run('ffmpeg -i DASH_1080.mp4 -i DASH_audio.mp4 -map 0:v -map 1:a -c copy reddit_vid.mp4', shell = True)


test()
