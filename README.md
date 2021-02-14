# Reddit Vid Downloader

I created this from a desire to download Reddit hosted videos after realizing there isn't an option to download on the website. Reddit also doesn't make it easy to download videos with sound as the video and audio files are split up in the ```json```. This program merges the video file and audio file of a Reddit video, and downloads Reddit hosted videos to the program directory. 

WORKS FOR: Mac, Linux, Windows

Dependencies: 
- [requests](https://github.com/psf/requests)
- [urllib3](https://github.com/urllib3/urllib3)
- [wget](https://www.gnu.org/software/wget/)
- [ffmpeg](https://ffmpeg.org/)


## How to run

Clone this repository:

``` git clone https://github.com/melissa-kun-li/reddit-vid-downloader.git ```

Install dependencies using: 

```pip3 install -r requirements.txt``` 

Open a terminal in the directory this repository was cloned to and run this command: 

 ```python3 reddit-vid-downloader.py URL``` 

Note: Replace ```URL``` with the link to the post that has the Reddit hosted video! The video will be saved in the program directory. 

If you'd like to test it out, check out this link for Reddit hosted videos: https://old.reddit.com/domain/v.redd.it/




