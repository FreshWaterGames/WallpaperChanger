# imports are needed to get secondary functions like a timer or operating systems
import os, pathlib, random, time, ctypes, schedule

WALLPAPER_FOLDER = "wallpapers"


def get_filenames_from_directory(folder_location):
    # uses parameter to return a list of all files in directory
    files = os.listdir(folder_location)
    return files


def set_wallpaper():
    # gets random file in folder
    wallpaper = get_filenames_from_directory(WALLPAPER_FOLDER)
    random_wallpaper = random.choice(wallpaper)
    full_wallpaper_path = os.path.join(pathlib.Path().absolute(), WALLPAPER_FOLDER, random_wallpaper)
    # change the desktop wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, full_wallpaper_path, 0)
    print("set wallpaper")


def run():
    timer = int(input("seconds between each change: "))
    # setup a schedule to change wallpaper every "time per second"
    schedule.every(timer).seconds.do(set_wallpaper)
    while True:
        schedule.run_pending()
        time.sleep(1)


run()
