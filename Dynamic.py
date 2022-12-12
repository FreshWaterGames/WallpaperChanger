# imports are needed to get secondary functions like a timer or operating systems
import ctypes
import os
import pathlib
import time
import schedule
from datetime import datetime

DYNAMIC_FOLDER = "dynamic_wallpaper"
now = (datetime.now()).strftime("%H")


def get_filenames_from_directory(folder_location):
    # uses parameter to return a list of all files in directory
    files = os.listdir(folder_location)
    return files


def set_wallpaper(x):
    # gets file from folder
    wallpaper = get_filenames_from_directory(DYNAMIC_FOLDER)
    full_wallpaper_path = os.path.join(pathlib.Path().absolute(), DYNAMIC_FOLDER, x)
    # change the desktop wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, full_wallpaper_path, 0)
    print("set wallpaper")


def dynamic():
    set_wallpaper(now)


def run():
    # schedule to check if wallpaper should change every hour
    schedule.every(1).hours.do(dynamic)
    while True:
        schedule.run_pending()
        time.sleep(1)


run()
