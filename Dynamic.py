# imports are needed to get secondary functions like a timer or operating systems
import ctypes
import os
import pathlib
import time
import schedule
from datetime import datetime

now = (datetime.now()).strftime("%H")


def set_wallpaper(x):
    # gets file from folder
    full_wallpaper_path = os.path.join(pathlib.Path().absolute(), str(wallpaper_path), x)
    # change the desktop wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, full_wallpaper_path, 0)
    print("set wallpaper")


def dynamic():
    set_wallpaper(now)


def run():
    print("running")
    # schedule to check if wallpaper should change every hour
    schedule.every(1).hours.do(dynamic)
    while True:
        schedule.run_pending()
        time.sleep(1)

print("execute file only at the start of the hour")
wallpaper_path = input("Enter path to image folder >>")
run()
