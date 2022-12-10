# imports are needed to get secondary functions like a timer or operating systems
import ctypes
import os
import pathlib
import time
import schedule
from datetime import datetime

DYNAMIC_FOLDER = "dynamic_wallpaper"
morning = "0711"  # 7 :00
noon = "1200"
evening = "1734"  # 7 :00
night = "2000"
new_night = "0000"
now = (datetime.now()).strftime("%H%M")


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


def change():
    print(now)
    if int(new_night) < int(now) < int(morning):
        set_wallpaper('Outset Island night.jpg')
        print("new night")
    elif int(morning) < int(now) < int(noon):
        set_wallpaper('Outset Island morning.jpg')
        print("morning")
    elif int(noon) < int(now) < int(evening):
        set_wallpaper('Outset Island day.jpg')
        print("noon")
    elif int(evening) < int(now) < int(night):
        set_wallpaper('Outset Island evening.jpg')
        print("evening")
    elif int(night) < int(now) < 2359:
        set_wallpaper('Outset Island night.jpg')
        print("night")


def run():
    # schedule to check if wallpaper should change every hour
    schedule.every(30).minutes.do(change)
    while True:
        schedule.run_pending()
        time.sleep(1)


run()
