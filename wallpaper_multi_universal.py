#!/usr/bin/env python3

import subprocess
import os
import time
import random
import shlex

script_dir = os.path.dirname(os.path.realpath(__file__))
screen_check_1 = "DVI-I-1 connected"
screen_check_2 = "DVI-D-0 connected"
screen_check_3 = "HDMI-0 connected"

screen1_picture_dir = "/home/philip/Pictures/Wallpaper/sfw/"
screen2_picture_dir = "/home/philip/Pictures/Wallpaper/sfw/"
screen3_picture_dir = "/home/philip/Pictures/Wallpaper/nsfw/"

span_image = script_dir+"/screenspan.jpeg"

def execute_set(command):
    subprocess.call(["/bin/bash", "-c", command])

def execute_get(command):
    return subprocess.check_output(["/bin/bash", "-c", command]).decode("utf-8").strip()

def switch_screen_count(count):
    set_uri_wallpaper(create_spanimage(count))

def set_uri_wallpaper(uri):
    execute_set("gsettings set org.gnome.desktop.background picture-uri "+uri)
    execute_set("gsettings set org.gnome.desktop.background picture-options spanned")

def get_random(directory):
    for (dirpath, dirnames, filenames) in os.walk(directory):
        file_t = random.choice(filenames)
        break
    return "".join((dirpath, file_t))

def create_spanimage(monitor_count):
    image_1 = shlex.quote(get_random(screen1_picture_dir))
    image_2 = shlex.quote(get_random(screen2_picture_dir))
    image_3 = shlex.quote(get_random(screen3_picture_dir))

    out_file = shlex.quote(span_image)

    print("convert "+image_1+" +append "+out_file)

    if monitor_count == 1:
        execute_set("convert "+image_1+" +append "+out_file)
    elif monitor_count == 2:
        execute_set("convert "+image_1+" "+image_2+" +append "+out_file)
    elif monitor_count == 3:
        execute_set("convert "+image_1+" "+image_2+" "+image_3+" +append "+out_file)

    return out_file

def check_connected_count():
    command = "xrandr"
    check = execute_get(command)
    count = 0
    if screen_check_1 in check:
        print(1)
        count += 1
    if screen_check_2 in check:
        print(2)
        count += 1
    if screen_check_3 in check:
        print(3)
        count += 1

    return count

def main():
    count = check_connected_count()
    print(count)
    set_uri_wallpaper(create_spanimage(count))

if __name__ == "__main__":
    main()
