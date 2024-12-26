import os
from moviepy import VideoFileClip

# Get file names from folder
folder = "C:/Users/luukw/Pictures/videocamera/Dickens Festijn Deventer/"
files = os.listdir(folder)
files = [file for file in files if file[-4:] == ".MOD"]

# Make new mp4 directory
if not os.path.exists(folder + "mp4"):
    os.mkdir(folder + "mp4")
save_folder = folder + "mp4/"

for file in files:
    clip = VideoFileClip(folder + file)
    clip.write_videofile(save_folder + file[:-4] + ".mp4", codec="mpeg4", bitrate="5M")