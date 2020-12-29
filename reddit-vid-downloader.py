import requests
import wget
import subprocess
import os
import pathlib

url = input('Please enter the Reddit link which has the Reddit embedded video: ')
info = {'user-agent':'vdownloader by /u/panaora'}
response = requests.get(url + '.json', headers = info)
data = response.json()

def reddit_vid_downloader():
    part = data[0]['data']['children']
    video_link = part[0]['data']['secure_media']['reddit_video']['fallback_url'][:-16]
    print(video_link)
    audio_link = video_link.split('_')[0] + '_audio.mp4'
    print(audio_link)
    
    wget.download(video_link) # /Users/melissali/Documents/reddit_vid_downloader/DASH_1080.mp4
    wget.download(audio_link) # /Users/melissali/Documents/reddit_vid_downloader/DASH_audio.mp4

    subprocess.run('ffmpeg -i DASH_1080.mp4 -i DASH_audio.mp4 -map 0:v -map 1:a -c copy reddit_vid.mp4', shell = True)

    script_directory = pathlib.Path(__file__).parent.absolute()
    print(script_directory)
    DASH_video_file, DASH_audio_file = 'DASH_1080.mp4', 'DASH_audio.mp4'
    path_video, path_audio = os.path.join(script_directory, DASH_video_file), os.path.join(script_directory, DASH_audio_file)
    os.remove(path_video)
    os.remove(path_audio)

    old_file = os.path.join(script_directory, 'reddit_vid.mp4')
    title = part[0]['data']['title']
    new_file = os.path.join(script_directory, title +'.mp4')
    os.rename(old_file,new_file)

reddit_vid_downloader()
