import os
import time
import shutil

if __name__ == "__main__":
    # Get file names from folder
    folder = input("Enter folder path: ")
    new_folder = input("Enter path for new image files (leave blank for same folder): ")
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

    # Ask user if they want to delete original image files after finish
    delete_original_files = input("Delete original image files after finish? (y/n): ") == "y"
    files = os.listdir(folder)
    print(files)

    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    for file in files:
        if not file.upper().endswith((".JPG", ".JPEG", ".PNG")):
            continue
        try:
            time_of_image = os.path.getmtime(folder + file)
            time_string = time.strftime("%Y%m%d_%H%M%S", time.gmtime(time_of_image))
            new_filename = new_folder + "image_" + time_string + file[-4:]

            if os.path.exists(new_filename):
                print(f"File image_{time_string + file[-4:]} already exists. There's probably duplicate images. Skipping.")
                continue

            # Save renamed copy of image
            shutil.copy2(folder + file, new_filename)
        except Exception as e:
            print(f"Error converting {file}: {e}")

    try:
        if delete_original_files:
            [os.remove(folder + file) for file in files if file.upper().endswith((".JPG", ".JPEG", ".PNG"))]
    except Exception as e:
        print(f"Error deleting original image files: {e}")