import struct
from datetime import datetime


def extract_moi_datetime(moi_file):
    """Extracts the recording date and time from a .moi file."""
    try:
        with open(moi_file, "rb") as f:
            f.seek(6)  # Start reading at hex offset 06
            raw_data = f.read(6)  # Read 6 bytes for date and time

            # Unpack the binary data (Year: 2 bytes, Month: 1 byte, Day: 1 byte, Hour: 1 byte, Minute: 1 byte)
            year, month, day, hour, minute = struct.unpack(">HBBBB", raw_data)

            return datetime(year, month, day, hour, minute)
    except Exception as e:
        print(f"Error reading {moi_file}: {e}")
        return None


# Example usage:
moi_filename = "C:/Users/luukw/Documents/Videocamera/backup/SD_VIDEO/PRG001/MOV00A.MOI"
recording_time = extract_moi_datetime(moi_filename)
if recording_time:
    print(f"Recording time: {recording_time}")