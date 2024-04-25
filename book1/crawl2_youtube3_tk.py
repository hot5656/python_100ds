# Tk interface YouTube 批次下載(播放清單下載)
import tkinter as tk
from pytube import Playlist
from pytube import YouTube
import os

DEFAULT_PATH = 'download'

def main():
    global video_type
    global tk_video
    global tk_url
    global tk_path
    global tk_label_msg

    # init for window
    win = tk.Tk()

    video_type = '360p'

    tk_url = tk.StringVar()
    tk_path = tk.StringVar()
    tk_video = tk.StringVar()

    # 標題
    win.title("下載Youtube影片 #2")
    # windows size
    win.minsize(width=538, height=280)

    # 網址輸入
    label1 = tk.Label(win, text='Youtube網址：')
    label1.place(x=123, y=30)
    entry_url = tk.Entry(win, textvariable=tk_url)
    entry_url.config(width=40)
    entry_url.place(x=220, y=30)

    # download 路徑
    label2 = tk.Label(win, text='存檔路徑(預設為download資料夾)：')
    label2.place(x=10, y=70)
    entry_path = tk.Entry(win, textvariable=tk_path)
    entry_path.config(width=40)
    entry_path.place(x=220, y=70)

    # download button
    btnDown = tk.Button(win, text="下載影片", command=clickDown)
    btnDown.place(x=200, y=110)

    # radio select
    rb1 = tk.Radiobutton(win, text="360p, mp4", variable=tk_video, value="360p", command=rbVideo)
    rb1.place(x=200, y=150)
    rb1.select()
    rb2 = tk.Radiobutton(win, text="720p, mp4", variable=tk_video, value="720p", command=rbVideo)
    rb2.place(x=200, y=180)

    # message label
    tk_label_msg = tk.Label(win, text="", fg="red")
    tk_label_msg.place(x=200, y=220)

    # 保持顯示 window
    win.mainloop()

# download function
def clickDown():
    global video_type
    global tk_url
    global tk_path
    global tk_label_msg

    # get path
    if len(tk_path.get()) != 0:
        video_path = tk_path.get()
    else:
        video_path = DEFAULT_PATH

    url_head = tk_url.get()

    try :
        playList = Playlist(url_head)

        if len(playList) != 0:
            # create folder
            if not os.path.exists(video_path) :
                os.makedirs(video_path)

            for url in playList:
                yt = YouTube(url)
                yt.streams.filter(subtype='mp4', res=video_type, progressive=True).first().download(video_path)
                print(f'{yt.title} Download complete')

            tk_label_msg.config(text="下載完成！")
    except:
        tk_label_msg.config(text="url not correct...")

# video select
def rbVideo() :
    global video_type
    global tk_video

    video_type = tk_video.get()

if __name__ == '__main__':
    main()