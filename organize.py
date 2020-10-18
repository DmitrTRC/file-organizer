import os
import platform
import shutil
import sys

from ext import foldername

FILE_NAME = "organize.py"
EXT_NAME = "ext.py"


def organize_files(drive):
    # check os
    operating_system = platform.system()
    if operating_system == "Windows":  # Windows
        drive = drive + "\\"
    elif operating_system == "Darwin":  # Mac
        drive = os.path.expanduser(drive)
    else:
        print(f"Operating system {operating_system} not currently supported")
        sys.exit(0)
    if not os.path.exists(drive):
        print(f"ERROR! {drive} is not a valid location")
        return
    files = os.listdir(drive)
    extns = {os.path.splitext(file)[1].strip(".") for file in files}

    # Create Folders
    for ext in extns:
        folder = foldername(ext)
        if folder and not os.path.exists(drive + folder):
            os.makedirs(drive + folder)

    # Move Files To Folders
    for file in files:
        if file in [FILE_NAME, EXT_NAME]:
            continue
        ext = os.path.splitext(file)[1].strip(".")
        folder = foldername(ext)
        if not folder:
            continue

        src = drive + file
        dest = drive + folder + "/" + file

        if not os.path.exists(dest):
            shutil.move(src, dest)
            print(f"Moved {file} to {folder}")

        print(f"\nSUCCESS! All files organized in {drive}")


if __name__ == "__main__":
    try:
        # location = sys.argv[1]
        # organize_files(location)
        organize_files('~/Trash')
    except Exception as e:
        print("USAGE: python organize.py <location>")
        print(e)
