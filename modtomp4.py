import os
from moviepy import VideoFileClip
import time


if __name__ == "__main__":
    # Get file names from folder
    folder = input("Enter folder path: ")
    new_folder = input("Enter path for new mp4 files (leave blank for same folder): ")
    # Validate folder path
    if folder == "":
        folder = "./"
    if folder[-1] != "/":
        folder += "/"

    if new_folder == "":
        new_folder = folder
    if new_folder[-1] != "/":
        new_folder += "/"

    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # Ask user if they want to delete .MOD and .MOI files after finish
    delete_mod_after_finish = input("Delete .MOD files after finish? (y/n): ") == "y"
    delete_moi_files = input("Delete .MOI files? (y/n): ") == "y"
    files = os.listdir(folder)

    # Delete .MOI files
    try:
        if delete_moi_files:
            [os.remove(folder + file) for file in files if file.upper()[-4:] == ".MOI"]
    except Exception as e:
        print(f"Error deleting .MOI files: {e}")

    # Filter .MOD files
    files = [file for file in files if file.upper()[-4:] == ".MOD"]

    for file in files:
        try:
            time_of_video = os.path.getmtime(folder + file)
            time_string = time.strftime("%Y%m%d_%H%M%S", time.gmtime(time_of_video))
            new_filename = new_folder + "video_" + time_string + ".mp4"

            clip = VideoFileClip(folder + file)
            clip.write_videofile(new_filename, codec="mpeg4", bitrate="5M")
            clip.close()
        except Exception as e:
            print(f"Error converting {file}: {e}")

    try:
        if delete_mod_after_finish:
            [os.remove(folder + file) for file in files]
    except Exception as e:
        print(f"Error deleting .MOD files: {e}")