from os import link
from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube[link]

print("Title:",yt.title)
print("Views:",yt.views)

yd = yt.streams.first().download(r"C:\Users\ABHISHEK\Desktop\Projects\Downloader\youtube\youtube downloads")

