import os
import struct
import subprocess
import sys


def extract_moi_datetime(moi_file):
    """Extracts the recording date and time from a .moi file."""
    try:
        print("Extracting moi file: ", moi_file)
        with open(moi_file, "rb") as f:
            f.seek(6)  # Start reading at hex offset 06
            raw_data = f.read(6)  # Read 6 bytes for date and time

            # Unpack the binary data (Year: 2 bytes, Month: 1 byte, Day: 1 byte, Hour: 1 byte, Minute: 1 byte)
            year, month, day, hour, minute = struct.unpack(">HBBBB", raw_data)

            # return datetime(year, month, day, hour, minute)
            return f"{year}-{month}-{day}_{hour}-{minute}"
    except Exception as e:
        print(f"Error reading {moi_file}: {e}")
        return None

if __name__ == "__main__":
    try:
        import tkinter as tk
        from tkinter import filedialog
        from moviepy import VideoFileClip
    except ImportError as e:
        print("Missing dependencies. Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "moviepy", "tk"])
        import tkinter as tk
        from tkinter import filedialog
        from moviepy import VideoFileClip

    # Get file names from folder
    root = tk.Tk()
    root.withdraw()

    folder = filedialog.askdirectory(mustexist=True) + "/"
    files = os.listdir(folder)
    new_folder = folder + "mp4/"
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # Filter .MOD files
    files = [file for file in files if file.upper()[-4:] == ".MOD"]

    for file in files:
        try:
            time_string = extract_moi_datetime(folder + file[:-4] + ".MOI")
            new_filename = new_folder + "video_" + time_string + ".mp4"

            if os.path.exists(new_filename):
                # count number of files with same time string
                new_files = [f for f in os.listdir(new_folder) if f.startswith("video_" + time_string)]

                # append number of files to new file name to avoid overwriting
                new_filename = new_folder + "video_" + time_string + "_" + str(len(new_files)) + ".mp4"

            clip = VideoFileClip(folder + file)
            clip.write_videofile(new_filename, codec="mpeg4", bitrate="5M")
            clip.close()
        except Exception as e:
            print(f"Error converting {file}: {e}")