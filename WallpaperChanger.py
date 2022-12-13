# imports are needed to get secondary functions like a timer or operating systems
import ctypes
import os
import pathlib
import random
import schedule
import time


def get_filenames_from_directory(folder_location):
    # uses parameter to return a list of all files in directory
    files = os.listdir(folder_location)
    return files


def set_wallpaper():
    # gets random file from folder
    wallpaper = get_filenames_from_directory(str(wallpaper_path))
    random_wallpaper = random.choice(wallpaper)
    full_wallpaper_path = os.path.join(pathlib.Path().absolute(), str(wallpaper_path), random_wallpaper)
    # change the desktop wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, full_wallpaper_path, 0)
    print("Wallpaper Set")


def run():
    # schedule to change wallpaper every "time per second"
    schedule.every(int(timer)).seconds.do(set_wallpaper)
    while True:
        schedule.run_pending()
        time.sleep(1)


wallpaper_path = input("Enter path to image folder >>")
timer = input("Enter seconds per change >>")
run()
