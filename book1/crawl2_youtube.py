# YouTube 下載
# pip install pytube
# [pytube document](https://pytube.io/en/latest/)

from pytube import YouTube
import os

FOLDER = "youtube"

def main():
    # create folder
    if not os.path.exists(FOLDER) :
        os.makedirs(FOLDER)

    yt = YouTube('https://www.youtube.com/watch?v=wyHLLzmNje0')

    # show all video format
    yt_streams = yt.streams
    for stream in yt_streams:
        print(stream)
    # <Stream: itag="18" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">
    # <Stream: itag="248" mime_type="video/webm" res="1080p" fps="24fps" vcodec="vp9" progressive="False" type="video">
    # <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">

    # select stream
    print("第一個 stream", yt_streams.first())
    print("最後一個 stream", yt_streams.last())
    # filter(條件1=值1, 條件2=值2, ...)
    # progressive=True 同時具備影像與聲音
    # adaptive=True 只具備影像或聲音
    # subtype='mp4' 影片格式
    # res='720p' 解析度
    # only_audio=True audio only
    # First() 符合條件第一個
    # Last() 符合條件最後一個
    print("指定條件 stream", yt_streams.filter(subtype='mp4'))

    # download 1st
    # yt.streams.first().download(FOLDER)
    # download 3rd
    # yt.streams[2].download(FOLDER)
    # print(f'{yt.title} Download complete')

    # load audio
    print('-- only audio --')
    print(yt.streams.filter(only_audio=True))
    # mime_type 聲音檔格式 'audio/webm', 'audio/mp4'
    audio = yt.streams.filter(only_audio=True, mime_type='audio/webm').first().download(FOLDER)
    print(f'{yt.title} audio Download complete')

if __name__ == '__main__':
    main()