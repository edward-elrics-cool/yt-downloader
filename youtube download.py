
from pytube import YouTube


url = input("Enter URL for video: ")
location = "C:/Users/mcken/Documents/python scripts/yt_downloader/iles"
yt = YouTube(url).streams.first().download(location)


