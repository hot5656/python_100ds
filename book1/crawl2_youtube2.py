# YouTube 批次下載(播放清單下載)
from pytube import Playlist
from pytube import YouTube
import os

LIST_URL = 'https://www.youtube.com/watch?v=f_OPjYQovAE&list=PLJicmE8fK0EhtXk4bQAHgyYh8v7-w8L7E'
FOLDER = "youtube"

def main():
    playList = Playlist(LIST_URL)
    # videolist = playList.video_urls
    # print(videolist)

    # create folder
    if not os.path.exists(FOLDER) :
        os.makedirs(FOLDER)

    for url in playList:
        yt = YouTube(url)
        yt.streams.filter(subtype='mp4', res='360p', progressive=True).first().download(FOLDER)
        print(f'{yt.title} Download complete')

if __name__ == '__main__':
    main()