from os import link
from pytube import YouTube

print("Enter the link to download")
link = input()
yt = YouTube(link)

print("Title:",yt.title)
print("Views:",yt.views)

yd = yt.streams.first().download(r"C:\Users\ABHISHEK\Desktop\Projects\Downloader\youtube\youtube downloads")

