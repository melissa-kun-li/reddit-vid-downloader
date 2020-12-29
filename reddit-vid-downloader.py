import requests
import wget
import subprocess
import os
import pathlib

from urllib.error import HTTPError

def reddit_vid_downloader():
    url = input('Please enter the Reddit link which has the Reddit embedded video: ')
    info = {'user-agent':'vdownloader by /u/panaora'}
    response = requests.get(url + '.json', headers = info)
    data = response.json()

    part = data[0]['data']['children']
    title = part[0]['data']['title'] # used in renaming file
    video_link = part[0]['data']['secure_media']['reddit_video']['fallback_url'][:-16] # https://...DASH_1080.mp4 or DASH_240, etc.
    audio_link = video_link.split('_')[0] + '_audio.mp4' # https://...DASH_audio.mp4
    
    script_path = pathlib.Path(__file__).parent.absolute()

    wget.download(video_link) # /Users/melissali/Documents/reddit_vid_downloader/DASH_1080.mp4
    DASH_video = 'DASH' + video_link.split('/DASH')[1] # works for diff DASH_xxx or DASH_1080 
    old_video = os.path.join(script_path, DASH_video)

    try:
        wget.download(audio_link) # /Users/melissali/Documents/reddit_vid_downloader/DASH_audio.mp4
    except HTTPError: # Reddit video has no audio so DASH_audio.mp4 DNE
        new_video = os.path.join(script_path, title + '.mp4')
        os.rename(old_video, new_video) # rename the Reddit video file
        return

    new_video = os.path.join(script_path, 'video.mp4')
    os.rename(old_video, new_video)

    # merge the video and audio file
    subprocess.run('ffmpeg -i video.mp4 -i DASH_audio.mp4 -map 0:v -map 1:a -c copy reddit_vid.mp4', shell = True)

    # delete the old DASH video and DASH_audio files
    path_video = os.path.join(script_path, 'video.mp4')
    path_audio = os.path.join(script_path, 'DASH_audio.mp4')
    os.remove(path_video)
    os.remove(path_audio)

    # rename the merged Reddit video + audio file 
    old_file = os.path.join(script_path, 'reddit_vid.mp4')
    new_file = os.path.join(script_path, title +'.mp4')
    os.rename(old_file,new_file)

reddit_vid_downloader()
