import requests
import wget
import subprocess
import os
import argparse

from urllib.error import HTTPError

def main(): 
    parser = argparse.ArgumentParser(description = 'Download Reddit videos to script directory.')
    parser.add_argument('url', type = str, help = 'Link of Reddit hosted video')
    args = parser.parse_args()

    reddit_vid_downloader(args)

def reddit_vid_downloader(args):
    info = {'user-agent':'vdownloader by /u/panaora'}
    response = requests.get(args.url + '.json', headers = info)
    data = response.json()

    part = data[0]['data']['children']
    title = part[0]['data']['title'] # used in renaming file
    video_link = part[0]['data']['secure_media']['reddit_video']['fallback_url'][:-16] # https://...DASH_1080.mp4 or DASH_240, etc.
    audio_link = video_link.split('_')[0] + '_audio.mp4' # https://...DASH_audio.mp4

    wget.download(video_link) 
    DASH_video = 'DASH' + video_link.split('/DASH')[1] # works for diff DASH_xxx or DASH_1080 

    try:
        wget.download(audio_link)
    except HTTPError: # Reddit video has no audio so DASH_audio.mp4 DNE
        os.rename(DASH_video, title + '.mp4') 
        return

    os.rename(DASH_video, 'video.mp4')
    subprocess.run('ffmpeg -i video.mp4 -i DASH_audio.mp4 -map 0:v -map 1:a -c copy reddit_vid.mp4', shell = True)
    os.remove('video.mp4')
    os.remove('DASH_audio.mp4')
    os.rename('reddit_vid.mp4', title + '.mp4')

if __name__ == '__main__':
    main()
