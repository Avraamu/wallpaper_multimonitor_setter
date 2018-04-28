#!/usr/bin/env python3

import os
from PIL import Image

# With trailing slash
dir = "/home/philip/Pictures/Wallpaper/nsfw/"

images = os.listdir(dir)

for image in images:
    im_o = Image.open(dir + image)
    if im_o.size != (1920, 1080):
        print('Deleting image ' + image)
        os.remove(dir + image)

print('Done.')
