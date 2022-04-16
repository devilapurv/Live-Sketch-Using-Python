'''
Made By :
Akshat Pandey - F07
Abhishek Pandey - F04
Apurv Singh - F15
Namshit Manikpuri - F33
'''
#importing pytube (install by usign pip install pytube)
from pytube import YouTube                        

link = input("Enter the URL of the video : ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
     print(i)

print("Enter the desired option of your choice :- ")
dn_option = int(input("Enter the option : "))
dn_video=videos[dn_option]
dn_video.download()

print("Video downloaded successfully!")
